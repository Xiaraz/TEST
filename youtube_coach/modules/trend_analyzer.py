"""
Trend Analyzer Module - Analyzes YouTube gaming trends.
Scrapes trending data from YouTube and provides insights.
"""

import json
import re
import time
from datetime import datetime
from urllib.parse import quote_plus

import requests

from youtube_coach.data.games_database import (
    GAMES_DATABASE,
    TRENDING_GAMING_TOPICS,
    VIDEO_FORMATS_DATABASE,
)


class TrendAnalyzer:
    """Analyzes YouTube gaming trends to find viral content opportunities."""

    YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2dhbWluZw%3D%3D"
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

    def get_trending_games(self, top_n=10):
        """Get the top trending games based on our database and current scores."""
        sorted_games = sorted(
            GAMES_DATABASE.items(),
            key=lambda x: x["popularity_score"] if isinstance(x, dict) else x[1]["popularity_score"],
            reverse=True,
        )
        results = []
        for key, game in sorted_games[:top_n]:
            results.append({
                "id": key,
                "name": game["name"],
                "genre": game["genre"],
                "popularity_score": game["popularity_score"],
                "best_formats": game["content_formats"][:5],
                "trending_topics": game["trending_topics"][:3],
            })
        return results

    def search_youtube_trends(self, query, max_results=10):
        """Search YouTube for trending videos related to a query."""
        params = {"search_query": query, "sp": "CAMSAhAB"}  # Sort by view count
        try:
            response = self.session.get(
                self.YOUTUBE_SEARCH_URL,
                params=params,
                timeout=15,
            )
            response.raise_for_status()
            return self._parse_search_results(response.text, max_results)
        except requests.RequestException as e:
            return {"error": str(e), "results": []}

    def _parse_search_results(self, html, max_results):
        """Parse YouTube search page HTML for video data."""
        results = []
        # Extract ytInitialData JSON from the page
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

                title = ""
                title_runs = video.get("title", {}).get("runs", [])
                if title_runs:
                    title = title_runs[0].get("text", "")

                view_text = video.get("viewCountText", {}).get("simpleText", "0 vues")
                published = video.get("publishedTimeText", {}).get("simpleText", "")
                length = video.get("lengthText", {}).get("simpleText", "")
                channel = video.get("ownerText", {}).get("runs", [{}])[0].get("text", "")
                video_id = video.get("videoId", "")

                results.append({
                    "title": title,
                    "views": view_text,
                    "published": published,
                    "length": length,
                    "channel": channel,
                    "video_id": video_id,
                    "url": f"https://youtube.com/watch?v={video_id}",
                })
        except (json.JSONDecodeError, KeyError, IndexError):
            pass

        return results

    def analyze_game_trends(self, game_name):
        """Get comprehensive trend analysis for a specific game."""
        game_key = game_name.lower().replace(" ", "_").replace(":", "")
        game_data = GAMES_DATABASE.get(game_key)

        if not game_data:
            # Try fuzzy match
            for key, data in GAMES_DATABASE.items():
                if game_name.lower() in data["name"].lower() or game_name.lower() in key:
                    game_data = data
                    game_key = key
                    break

        if not game_data:
            return {
                "found": False,
                "message": f"Jeu '{game_name}' non trouve dans la base de donnees.",
                "suggestion": "Essayez avec un des jeux suivants : "
                + ", ".join(d["name"] for d in GAMES_DATABASE.values()),
            }

        # Search for recent trending content
        search_results = self.search_youtube_trends(f"{game_data['name']} 2025")

        analysis = {
            "found": True,
            "game": game_data["name"],
            "genre": game_data["genre"],
            "platforms": game_data["platforms"],
            "audience_cible": game_data["audience"],
            "score_popularite": game_data["popularity_score"],
            "meilleurs_formats": game_data["content_formats"],
            "sujets_tendance": game_data["trending_topics"],
            "duree_recommandee": game_data["best_video_length"],
            "meilleurs_horaires": game_data["best_upload_times"],
            "hashtags_recommandes": game_data["hashtags"],
            "formats_concurrents": game_data["competitors_formats"],
            "videos_tendance": search_results if isinstance(search_results, list) else [],
            "recommandations": self._generate_recommendations(game_data),
        }

        return analysis

    def _generate_recommendations(self, game_data):
        """Generate strategic recommendations based on game data."""
        recs = []
        score = game_data["popularity_score"]

        if score >= 90:
            recs.append(
                "HAUTE COMPETITION : Ce jeu est tres populaire. "
                "Differenciez-vous avec un angle unique ou un format original."
            )
            recs.append(
                "Publiez rapidement apres les mises a jour pour capturer "
                "le trafic de recherche."
            )
        elif score >= 75:
            recs.append(
                "BONNE OPPORTUNITE : Competition moderee avec une audience fidele. "
                "Un bon equilibre risque/recompense."
            )
            recs.append(
                "Concentrez-vous sur la qualite et la regularite pour "
                "construire une communaute."
            )
        else:
            recs.append(
                "NICHE : Moins de competition mais audience plus petite. "
                "Ideal pour se positionner comme expert."
            )
            recs.append(
                "Devenez LA reference sur ce jeu en couvrant tous les aspects."
            )

        recs.append(
            f"Duree recommandee : {game_data['best_video_length']} "
            f"pour maximiser le watch time."
        )
        recs.append(
            f"Publiez de preference a : {', '.join(game_data['best_upload_times'])} "
            f"(heures francaises)."
        )

        return recs

    def get_trending_formats(self):
        """Get analysis of which video formats are trending."""
        formats = []
        for key, fmt in VIDEO_FORMATS_DATABASE.items():
            formats.append({
                "id": key,
                "name": fmt["name"],
                "description": fmt["description"],
                "retention_moyenne": fmt["avg_retention"],
                "difficulte": fmt["difficulty"],
                "exemples_titres": fmt["example_titles"],
            })
        return sorted(formats, key=lambda x: x["retention_moyenne"], reverse=True)

    def get_general_trends(self):
        """Get general gaming trends and hot topics."""
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "tendances_generales": TRENDING_GAMING_TOPICS,
            "formats_populaires": [
                "Shorts/TikTok (croissance rapide)",
                "100 Days Hardcore (retention elevee)",
                "Tier Lists (tres partageables)",
                "Challenges viraux (potentiel viral)",
                "Guides/Tutoriels (trafic de recherche stable)",
            ],
            "conseils_algorithme": [
                "CTR (Click-Through Rate) : miniature + titre sont ESSENTIELS",
                "Watch Time : les 30 premieres secondes determinent tout",
                "Engagement : likes, commentaires, partages boostent la visibilite",
                "Regularite : publier a heures fixes cree une habitude",
                "Shorts : excellent pour gagner des abonnes rapidement",
                "Communaute : repondre aux commentaires ameliore le ranking",
            ],
            "erreurs_a_eviter": [
                "Titres clickbait sans rapport avec le contenu",
                "Intros trop longues (> 30 secondes)",
                "Qualite audio mediocre",
                "Pas de call-to-action",
                "Upload irregulier",
                "Ignorer les analytics",
                "Copier sans apporter de valeur ajoutee",
            ],
        }
