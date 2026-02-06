"""
Web Scraper Module - Fetches real data from YouTube and gaming websites.
Used when a game is not in the local database.
"""

import json
import re
from datetime import datetime

import requests


class WebScraper:
    """Scrapes YouTube and web sources for game data."""

    YOUTUBE_SEARCH_URL = "https://www.youtube.com/results"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
        })

    def search_youtube(self, query, max_results=10):
        """Search YouTube and return parsed video results."""
        try:
            response = self.session.get(
                self.YOUTUBE_SEARCH_URL,
                params={"search_query": query},
                timeout=15,
            )
            response.raise_for_status()
            return self._parse_youtube_page(response.text, max_results)
        except requests.RequestException as e:
            return []

    def _parse_youtube_page(self, html, max_results):
        """Parse YouTube search results HTML."""
        results = []
        match = re.search(r"var ytInitialData = ({.*?});</script>", html)
        if not match:
            return results

        try:
            data = json.loads(match.group(1))
            contents = (
                data.get("contents", {})
                .get("twoColumnSearchResultsRenderer", {})
                .get("primaryContents", {})
                .get("sectionListRenderer", {})
                .get("contents", [{}])[0]
                .get("itemSectionRenderer", {})
                .get("contents", [])
            )

            for item in contents[:max_results]:
                video = item.get("videoRenderer")
                if not video:
                    continue

                title_runs = video.get("title", {}).get("runs", [])
                title = title_runs[0].get("text", "") if title_runs else ""
                views = video.get("viewCountText", {}).get("simpleText", "0 vues")
                published = video.get("publishedTimeText", {}).get("simpleText", "")
                length = video.get("lengthText", {}).get("simpleText", "")
                channel = video.get("ownerText", {}).get("runs", [{}])[0].get("text", "")
                video_id = video.get("videoId", "")

                results.append({
                    "title": title,
                    "views": views,
                    "published": published,
                    "length": length,
                    "channel": channel,
                    "video_id": video_id,
                    "url": "https://youtube.com/watch?v=" + video_id,
                })
        except (json.JSONDecodeError, KeyError, IndexError):
            pass

        return results

    def research_unknown_game(self, game_name):
        """
        Research a game that is NOT in the local database.
        Searches YouTube for multiple queries to build a profile.
        Returns a dict with all discovered info.
        """
        print(f"  [WEB] Recherche YouTube pour '{game_name}'...")

        # Run several targeted searches
        searches = {
            "general": game_name + " gameplay 2025",
            "tips": game_name + " tips tricks guide",
            "funny": game_name + " funny moments",
            "review": game_name + " review avis",
            "fr": game_name + " fr francais gameplay",
        }

        all_results = {}
        all_videos = []
        channels = set()
        titles = []

        for key, query in searches.items():
            print(f"  [WEB] Recherche: {query}")
            videos = self.search_youtube(query, max_results=8)
            all_results[key] = videos
            all_videos.extend(videos)
            for v in videos:
                channels.add(v.get("channel", ""))
                titles.append(v.get("title", ""))

        # Analyze what we found
        total_videos = len(all_videos)
        unique_channels = len(channels - {""})

        # Try to detect genre from titles
        genre = self._detect_genre(titles)

        # Try to detect platforms from titles
        platforms = self._detect_platforms(titles)

        # Analyze popular formats from real video titles
        popular_formats = self._detect_popular_formats(titles, game_name)

        # Detect trending topics from titles
        trending_topics = self._detect_trending_topics(titles, game_name)

        # Estimate popularity based on how many results we found
        if total_videos >= 30:
            popularity = "Eleve"
            popularity_score = 80
        elif total_videos >= 15:
            popularity = "Moyen"
            popularity_score = 60
        elif total_videos >= 5:
            popularity = "Faible-Moyen"
            popularity_score = 40
        else:
            popularity = "Niche / Nouveau"
            popularity_score = 25

        # Check French content availability
        fr_videos = len(all_results.get("fr", []))
        fr_status = "Bonne presence FR" if fr_videos >= 3 else "Peu de contenu FR (OPPORTUNITE !)"

        # Extract best channels covering this game
        top_channels = list(channels - {""})[:10]

        # Build recommended hashtags
        clean_name = game_name.replace(" ", "")
        hashtags = [
            "#" + clean_name,
            "#" + clean_name + "Gameplay",
            "#" + clean_name + "FR",
            "#Gaming",
            "#JeuxVideo",
        ]

        return {
            "source": "web_search",
            "game_name": game_name,
            "genre_detecte": genre,
            "plateformes_detectees": platforms,
            "popularite_estimee": popularity,
            "popularity_score": popularity_score,
            "videos_trouvees": total_videos,
            "chaines_actives": unique_channels,
            "top_chaines": top_channels,
            "contenu_francais": fr_status,
            "formats_populaires_detectes": popular_formats,
            "sujets_tendance_detectes": trending_topics,
            "hashtags_suggeres": hashtags,
            "videos_populaires": [
                {
                    "titre": v["title"],
                    "vues": v["views"],
                    "chaine": v["channel"],
                    "duree": v["length"],
                }
                for v in all_results.get("general", [])[:5]
            ],
            "videos_tips": [
                {
                    "titre": v["title"],
                    "vues": v["views"],
                    "chaine": v["channel"],
                }
                for v in all_results.get("tips", [])[:5]
            ],
            "videos_fr": [
                {
                    "titre": v["title"],
                    "vues": v["views"],
                    "chaine": v["channel"],
                }
                for v in all_results.get("fr", [])[:5]
            ],
            "recommandations": self._generate_web_recommendations(
                game_name, total_videos, unique_channels, fr_videos, popularity_score
            ),
        }

    def _detect_genre(self, titles):
        """Try to detect game genre from video titles."""
        title_text = " ".join(titles).lower()
        genre_keywords = {
            "Action RPG": ["rpg", "build", "level", "boss", "loot", "souls", "elden"],
            "FPS": ["fps", "aim", "headshot", "sniper", "shoot", "gun"],
            "Battle Royale": ["battle royale", "br", "zone", "loot", "drop"],
            "MOBA": ["moba", "lane", "carry", "support", "jungle"],
            "Survie": ["survie", "survival", "craft", "base", "ressource"],
            "Horreur": ["horreur", "horror", "peur", "scary", "ghost"],
            "Sport": ["fifa", "foot", "goal", "match", "equipe", "team"],
            "Strategie": ["strategie", "strategy", "deck", "card", "tower"],
            "Sandbox": ["sandbox", "build", "creative", "world"],
            "Aventure": ["aventure", "adventure", "story", "quest", "explore"],
            "Plateforme": ["plateforme", "platform", "jump", "speedrun"],
            "Simulation": ["simulation", "simulator", "sim"],
        }
        scores = {}
        for genre, keywords in genre_keywords.items():
            score = sum(1 for kw in keywords if kw in title_text)
            if score > 0:
                scores[genre] = score

        if scores:
            return max(scores, key=scores.get)
        return "Non determine (recherche web)"

    def _detect_platforms(self, titles):
        """Try to detect platforms from video titles."""
        title_text = " ".join(titles).lower()
        platforms = []
        platform_keywords = {
            "PC": ["pc", "steam", "epic"],
            "PS5": ["ps5", "playstation", "ps4"],
            "Xbox": ["xbox", "game pass"],
            "Switch": ["switch", "nintendo"],
            "Mobile": ["mobile", "android", "ios", "iphone"],
        }
        for platform, keywords in platform_keywords.items():
            if any(kw in title_text for kw in keywords):
                platforms.append(platform)

        return platforms if platforms else ["Non determine"]

    def _detect_popular_formats(self, titles, game_name):
        """Detect popular content formats from real video titles."""
        formats = []
        title_text = " ".join(titles).lower()
        game_lower = game_name.lower()

        format_patterns = {
            "Guides / Tutoriels": ["guide", "tuto", "tutorial", "how to", "comment", "tips", "astuce"],
            "Gameplay commente": ["gameplay", "let's play", "playthrough", "walkthrough"],
            "Funny Moments": ["funny", "drole", "moments", "wtf", "fails"],
            "Reviews / Avis": ["review", "avis", "test", "vaut le coup"],
            "Top / Classement": ["top", "tier list", "best", "meilleur", "classement"],
            "Actualites / News": ["update", "mise a jour", "patch", "news", "saison", "season"],
            "Challenge / Defi": ["challenge", "defi", "impossible", "hardcore"],
            "Speedrun": ["speedrun", "speed run", "record", "fastest"],
            "Lore / Histoire": ["lore", "histoire", "story", "theorie", "theory"],
            "PvP / Competitif": ["pvp", "ranked", "competitive", "tournoi", "tournament"],
            "Build / Progression": ["build", "loadout", "setup", "progression"],
        }

        for fmt_name, keywords in format_patterns.items():
            count = sum(1 for kw in keywords if kw in title_text)
            if count > 0:
                formats.append(fmt_name)

        return formats if formats else [
            "Gameplay commente",
            "Guides / Tutoriels",
            "Reviews / Avis",
        ]

    def _detect_trending_topics(self, titles, game_name):
        """Extract trending topics from video titles."""
        topics = []
        common_words = {
            "le", "la", "les", "de", "du", "des", "un", "une", "et", "en",
            "sur", "the", "is", "of", "in", "to", "for", "and", "a", "my",
            "this", "that", "with", "on", "at", "i", "you", "it", "ce",
            "qui", "que", "est", "pas", game_name.lower(),
        }

        # Extract unique meaningful phrases from titles
        seen = set()
        for title in titles[:20]:
            # Clean and extract key phrases
            words = title.lower().split()
            for i in range(len(words) - 1):
                bigram = words[i] + " " + words[i + 1]
                if (words[i] not in common_words and
                        words[i + 1] not in common_words and
                        bigram not in seen and
                        len(words[i]) > 2 and len(words[i + 1]) > 2):
                    seen.add(bigram)
                    topics.append(bigram.title())

        # Also add some from single prominent words
        word_freq = {}
        for title in titles:
            for word in title.lower().split():
                if word not in common_words and len(word) > 3:
                    word_freq[word] = word_freq.get(word, 0) + 1

        # Top frequent words as topics
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words[:5]:
            if count >= 2:
                topics.append(word.title())

        return topics[:10] if topics else [
            "Gameplay general",
            "Tips et astuces",
            "Nouveautes",
        ]

    def _generate_web_recommendations(self, game_name, total_videos, channels, fr_videos, score):
        """Generate recommendations based on web research results."""
        recs = []

        if total_videos >= 30:
            recs.append(
                "COMPETITION DETECTEE : Beaucoup de contenu existe deja. "
                "Differenciez-vous avec un angle unique ou une meilleure qualite."
            )
        elif total_videos >= 10:
            recs.append(
                "BONNE OPPORTUNITE : Le jeu a une audience mais n'est pas sursature. "
                "Positionnez-vous rapidement."
            )
        else:
            recs.append(
                "PEU DE CONTENU : Tres peu de videos trouvees. "
                "Si le jeu est nouveau, c'est une ENORME opportunite pour etre premier."
            )

        if fr_videos < 3:
            recs.append(
                "OPPORTUNITE FR : Tres peu de contenu en francais ! "
                "Creer du contenu FR sur ce jeu peut vous donner un avantage enorme."
            )
        else:
            recs.append(
                "Contenu FR existant. Analysez les chaines FR concurrentes "
                "pour trouver ce qui manque."
            )

        recs.append(
            "CONSEIL : Commencez par un guide debutant + review. "
            "Ces formats attirent le trafic de recherche sur les nouveaux jeux."
        )
        recs.append(
            "Publiez de preference entre 17h-20h (heures FR) "
            "pour maximiser l'audience francophone."
        )
        recs.append(
            "Duree recommandee : 10-15 min pour les guides, "
            "8-12 min pour les gameplays, 30-60s pour les Shorts."
        )

        return recs
