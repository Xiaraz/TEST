"""
Game Researcher Module - Deep research on specific games for content creation.
"""

import json
import re
from datetime import datetime

import requests

from youtube_coach.data.games_database import GAMES_DATABASE, VIDEO_FORMATS_DATABASE


class GameResearcher:
    """Researches games to provide comprehensive data for content creation."""

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

    def full_research(self, game_name):
        """Perform comprehensive research on a game for content creation."""
        game_key = self._find_game_key(game_name)
        game_data = GAMES_DATABASE.get(game_key)

        report = {
            "jeu": game_name,
            "date_recherche": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "dans_base_donnees": game_data is not None,
        }

        if game_data:
            report.update(self._build_detailed_report(game_data))
        else:
            report.update(self._build_generic_report(game_name))

        # Add YouTube search data
        report["recherche_youtube"] = self._search_youtube_data(
            game_data["name"] if game_data else game_name
        )

        # Add content strategy
        report["strategie_contenu"] = self._build_content_strategy(game_data, game_name)

        # Add competitor analysis
        report["analyse_concurrence"] = self._analyze_competition(game_data, game_name)

        return report

    def _find_game_key(self, game_name):
        """Find the database key for a game name."""
        name_lower = game_name.lower().replace(" ", "_").replace(":", "")
        if name_lower in GAMES_DATABASE:
            return name_lower
        for key, data in GAMES_DATABASE.items():
            if game_name.lower() in data["name"].lower() or game_name.lower() in key:
                return key
        return None

    def _build_detailed_report(self, game_data):
        """Build a detailed report from database data."""
        return {
            "informations_generales": {
                "nom": game_data["name"],
                "genre": game_data["genre"],
                "plateformes": game_data["platforms"],
                "audience_cible": game_data["audience"],
                "score_popularite": f"{game_data['popularity_score']}/100",
            },
            "analyse_contenu": {
                "formats_recommandes": game_data["content_formats"],
                "sujets_tendance": game_data["trending_topics"],
                "formats_concurrents": game_data["competitors_formats"],
                "hashtags": game_data["hashtags"],
            },
            "parametres_optimaux": {
                "duree_video": game_data["best_video_length"],
                "horaires_publication": game_data["best_upload_times"],
                "frequence_recommandee": self._recommend_frequency(game_data),
            },
        }

    def _build_generic_report(self, game_name):
        """Build a generic report for unknown games."""
        return {
            "informations_generales": {
                "nom": game_name,
                "genre": "Non determine",
                "plateformes": ["A verifier"],
                "audience_cible": "A determiner",
                "score_popularite": "Non disponible",
            },
            "analyse_contenu": {
                "formats_recommandes": [
                    "Guide debutant",
                    "Gameplay commente",
                    "Tips & Tricks",
                    "Review / Avis",
                    "Funny moments",
                ],
                "sujets_tendance": [
                    "Faire des recherches sur les tendances actuelles du jeu",
                ],
                "formats_concurrents": [
                    "Analyser les chaines qui couvrent ce jeu",
                ],
                "hashtags": [f"#{game_name.replace(' ', '')}", "#Gaming"],
            },
            "parametres_optimaux": {
                "duree_video": "10-15 min (standard recommande)",
                "horaires_publication": ["17h-19h (apres ecole/travail)"],
                "frequence_recommandee": "2-3 videos par semaine",
            },
            "note": (
                f"Le jeu '{game_name}' n'est pas dans notre base de donnees. "
                "Les recommandations sont generiques. Ajoutez-le a la base "
                "pour des resultats plus precis."
            ),
        }

    def _recommend_frequency(self, game_data):
        """Recommend upload frequency based on game popularity."""
        score = game_data["popularity_score"]
        if score >= 90:
            return "3-5 videos/semaine (haute competition, il faut etre actif)"
        elif score >= 75:
            return "2-3 videos/semaine (bon equilibre)"
        else:
            return "1-2 videos/semaine (niche, qualite > quantite)"

    def _search_youtube_data(self, game_name):
        """Search YouTube for trending content about the game."""
        queries = [
            f"{game_name} 2025",
            f"{game_name} tips tricks",
            f"{game_name} funny moments",
        ]

        results = {}
        for query in queries:
            try:
                response = self.session.get(
                    "https://www.youtube.com/results",
                    params={"search_query": query, "sp": "CAMSAhAB"},
                    timeout=10,
                )
                videos = self._parse_youtube_results(response.text)
                results[query] = videos[:5]
            except requests.RequestException:
                results[query] = []

        return results

    def _parse_youtube_results(self, html):
        """Parse YouTube search results page."""
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

            for item in contents:
                video = item.get("videoRenderer")
                if not video:
                    continue

                title_runs = video.get("title", {}).get("runs", [])
                title = title_runs[0].get("text", "") if title_runs else ""
                views = video.get("viewCountText", {}).get("simpleText", "")
                channel = video.get("ownerText", {}).get("runs", [{}])[0].get("text", "")

                results.append({
                    "titre": title,
                    "vues": views,
                    "chaine": channel,
                })
        except (json.JSONDecodeError, KeyError, IndexError):
            pass

        return results

    def _build_content_strategy(self, game_data, game_name):
        """Build a content creation strategy."""
        game = game_data["name"] if game_data else game_name
        score = game_data["popularity_score"] if game_data else 50

        strategy = {
            "resume": "",
            "piliers_contenu": [],
            "calendrier_type": {},
            "objectifs_30_jours": [],
            "kpis_a_suivre": [
                "Vues moyennes par video",
                "Watch time moyen (%)",
                "Click-Through Rate (CTR) des miniatures",
                "Ratio likes/vues",
                "Croissance abonnes/semaine",
                "Commentaires par video",
            ],
        }

        if score >= 85:
            strategy["resume"] = (
                f"{game} est un jeu TRES competitif sur YouTube. "
                "Pour reussir, il faut se differencier avec un style unique, "
                "une qualite de montage superieure, ou un angle que personne "
                "n'exploite encore."
            )
            strategy["piliers_contenu"] = [
                f"Pilier 1 : Guides & Tips {game} (trafic de recherche)",
                f"Pilier 2 : Highlights & Funny Moments (partageables)",
                f"Pilier 3 : Actualites & Mises a jour (timeliness)",
                f"Pilier 4 : Shorts quotidiens (croissance abonnes)",
            ]
            strategy["calendrier_type"] = {
                "Lundi": f"Guide/Tutorial {game}",
                "Mercredi": f"Highlights/Funny Moments {game}",
                "Vendredi": f"Challenge/Tendance {game}",
                "Quotidien": f"1 Short {game} par jour",
            }
        elif score >= 70:
            strategy["resume"] = (
                f"{game} offre un bon equilibre entre audience et competition. "
                "Concentrez-vous sur la regularite et la construction d'une "
                "communaute fidele."
            )
            strategy["piliers_contenu"] = [
                f"Pilier 1 : Guides complets {game} (reference)",
                f"Pilier 2 : Serie reguliere {game} (fidelisation)",
                f"Pilier 3 : Reactions aux updates (actualite)",
            ]
            strategy["calendrier_type"] = {
                "Mardi": f"Episode de serie {game}",
                "Jeudi": f"Guide ou Tips {game}",
                "Samedi": f"Contenu libre / Tendance {game}",
            }
        else:
            strategy["resume"] = (
                f"{game} est un jeu de niche. L'avantage : moins de competition. "
                "Devenez LA reference pour ce jeu."
            )
            strategy["piliers_contenu"] = [
                f"Pilier 1 : Guides exhaustifs {game} (SEO long-tail)",
                f"Pilier 2 : Communaute et gameplay {game}",
            ]
            strategy["calendrier_type"] = {
                "Mercredi": f"Contenu {game}",
                "Samedi": f"Contenu {game}",
            }

        strategy["objectifs_30_jours"] = [
            "Semaine 1 : Publier 3 videos + setup analytics",
            "Semaine 2 : Analyser les performances, ajuster les miniatures",
            "Semaine 3 : Tester un nouveau format base sur les data",
            "Semaine 4 : Bilan mensuel, definir les objectifs du mois suivant",
        ]

        return strategy

    def _analyze_competition(self, game_data, game_name):
        """Analyze the competitive landscape."""
        game = game_data["name"] if game_data else game_name
        formats = game_data.get("competitors_formats", []) if game_data else []

        return {
            "formats_populaires_concurrents": formats,
            "comment_se_differencier": [
                "Trouver un angle UNIQUE que personne n'exploite",
                "Qualite de montage superieure a la moyenne",
                "Personnalite authentique et memorable",
                "Regularite irreprochable (meme jour, meme heure)",
                "Engagement communautaire (repondre a TOUS les commentaires)",
                "Miniatures et titres 10/10 (le packaging est cle)",
            ],
            "opportunites_inexploitees": [
                f"Contenu {game} en francais (souvent moins sature qu'en anglais)",
                f"Formats longs type documentaire/analyse sur {game}",
                f"Contenu educatif/coaching {game}",
                f"Compilations communautaires {game}",
                f"Collaboration avec d'autres createurs {game}",
            ],
            "erreurs_concurrents": [
                "Titres clickbait excessifs (perte de confiance)",
                "Intros trop longues (perte de retention)",
                "Pas de sous-titres sur les Shorts",
                "Miniatures illisibles sur mobile",
                "Pas de call-to-action",
            ],
        }

    def get_content_calendar(self, game_name, weeks=4):
        """Generate a content calendar for the specified number of weeks."""
        game_key = self._find_game_key(game_name)
        game_data = GAMES_DATABASE.get(game_key)
        game = game_data["name"] if game_data else game_name
        formats = game_data["content_formats"] if game_data else [
            "Gameplay", "Tips", "Funny Moments", "Guide", "Review"
        ]

        calendar = []
        days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

        for week in range(1, weeks + 1):
            week_plan = {"semaine": week, "videos": []}

            # 3 videos per week + daily shorts
            video_days = [1, 3, 5]  # Mardi, Jeudi, Samedi
            for day_idx in video_days:
                fmt = formats[day_idx % len(formats)]
                week_plan["videos"].append({
                    "jour": days[day_idx],
                    "type": "Video longue",
                    "format": fmt,
                    "titre_suggestion": f"{game} - {fmt} #S{week}",
                    "duree": game_data["best_video_length"] if game_data else "10-15 min",
                    "horaire": game_data["best_upload_times"][0] if game_data else "18h",
                })

            # Daily shorts
            week_plan["shorts"] = {
                "frequence": "1 par jour",
                "exemples": [
                    f"Clip {game} du jour",
                    f"Astuce rapide {game}",
                    f"Moment drole {game}",
                ],
            }

            calendar.append(week_plan)

        return {
            "jeu": game,
            "duree": f"{weeks} semaines",
            "calendrier": calendar,
            "conseils": [
                "Preparer les miniatures et titres AVANT de filmer",
                "Batch recording : filmer plusieurs videos le meme jour",
                "Garder 2-3 videos d'avance en stock",
                "Adapter le calendrier en fonction des updates du jeu",
                "Les Shorts peuvent etre extraits des videos longues",
            ],
        }
