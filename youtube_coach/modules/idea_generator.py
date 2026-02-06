"""
Idea Generator Module - Generates video ideas based on games and trends.
"""

import random
from datetime import datetime

from youtube_coach.data.games_database import GAMES_DATABASE, VIDEO_FORMATS_DATABASE


class IdeaGenerator:
    """Generates creative video ideas for YouTube gaming content."""

    VIRAL_HOOKS = [
        "Et si je jouais avec {contrainte} ?",
        "Le secret que les pros ne partagent JAMAIS",
        "J'ai teste pendant {duree} et voila ce qui s'est passe",
        "Personne ne fait ca et pourtant c'est BROKEN",
        "J'ai decouvert un GLITCH incroyable",
        "DE ZERO A HERO en une seule video",
        "Le {item} le plus SOUS-ESTIME du jeu",
        "JE DEFIE un TOP {rang} joueur",
        "Comment j'ai atteint {objectif} en {temps}",
        "L'erreur que 99% des joueurs font",
    ]

    CHALLENGE_IDEAS = [
        "Jouer uniquement avec {restriction}",
        "Gagner sans utiliser {element}",
        "Laisser le chat Twitch decider de tout",
        "Jouer avec un volant/une manette de danse",
        "Defi 0 a {objectif} sans mourir",
        "Randomizer challenge complet",
        "Speedrun debutant vs speedrun pro",
        "Jouer les yeux bandes (avec un guide)",
        "Utiliser UNIQUEMENT le pire {element} du jeu",
        "Inverser les commandes challenge",
        "1 mort = changer de jeu",
        "Jouer avec les parametres graphiques au MINIMUM",
    ]

    SERIES_IDEAS = [
        "Road to {rang_max} - Episode {n}",
        "100 Jours Hardcore {game}",
        "Du pire au meilleur : tous les {elements} testes",
        "Je deviens PRO en {temps} - Jour {n}",
        "Survie extreme : {game} difficulte max",
        "Histoire complete de {game} expliquee",
        "Chaque {element} en 1 minute",
        "Progression F2P (Free to Play) Journal - Semaine {n}",
    ]

    COLLAB_IDEAS = [
        "1v1 contre un abonne",
        "On enseigne {game} a un DEBUTANT TOTAL",
        "Pro vs Casual - Qui gagne ?",
        "Mon petit frere/ma copine teste {game}",
        "Tournoi d'abonnes - {game}",
    ]

    def generate_ideas(self, game_name, count=10, formats=None):
        """Generate video ideas for a specific game."""
        game_key = self._find_game_key(game_name)
        game_data = GAMES_DATABASE.get(game_key)

        if not game_data:
            return self._generate_generic_ideas(game_name, count)

        ideas = []
        year = datetime.now().year

        # Generate ideas from different categories
        ideas.extend(self._generate_trending_ideas(game_data, year))
        ideas.extend(self._generate_format_ideas(game_data, year))
        ideas.extend(self._generate_challenge_ideas(game_data))
        ideas.extend(self._generate_series_ideas(game_data))
        ideas.extend(self._generate_seasonal_ideas(game_data, year))
        ideas.extend(self._generate_collab_ideas(game_data))

        # Filter by format if specified
        if formats:
            ideas = [i for i in ideas if i.get("format") in formats] or ideas

        # Shuffle and limit
        random.shuffle(ideas)
        return ideas[:count]

    def _find_game_key(self, game_name):
        """Find the database key for a game name."""
        name_lower = game_name.lower().replace(" ", "_").replace(":", "")
        if name_lower in GAMES_DATABASE:
            return name_lower
        for key, data in GAMES_DATABASE.items():
            if game_name.lower() in data["name"].lower() or game_name.lower() in key:
                return key
        return None

    def _generate_trending_ideas(self, game_data, year):
        """Generate ideas based on trending topics."""
        ideas = []
        game = game_data["name"]

        for topic in game_data["trending_topics"]:
            ideas.append({
                "titre": f"{game} : {topic} - TOUT ce qu'il faut savoir en {year}",
                "format": "reaction",
                "categorie": "Tendance",
                "description": f"Couvrir {topic} avec analyse et reactions en temps reel.",
                "potentiel_viral": "Eleve" if game_data["popularity_score"] >= 85 else "Moyen",
                "difficulte": "Facile",
                "duree_recommandee": "10-15 min",
                "hook_suggestion": f"La {topic} de {game} change TOUT...",
                "tags_suggeres": game_data["hashtags"] + [f"#{topic.replace(' ', '')}"],
            })

        return ideas

    def _generate_format_ideas(self, game_data, year):
        """Generate ideas based on popular video formats."""
        ideas = []
        game = game_data["name"]

        for fmt_key, fmt in VIDEO_FORMATS_DATABASE.items():
            for content_format in game_data["content_formats"][:3]:
                title_template = random.choice(fmt["example_titles"])
                title = title_template.replace("{game}", game).replace("{year}", str(year))
                title = title.replace("{number}", str(random.randint(1, 50)))
                title = title.replace("{adjective}", random.choice(
                    ["CASSES", "FORTS", "DROLES", "RARES", "SECRETS"]
                ))
                title = title.replace("{items}", content_format)

                ideas.append({
                    "titre": title,
                    "format": fmt_key,
                    "categorie": fmt["name"],
                    "description": f"{fmt['description']} - Focus sur {content_format}",
                    "potentiel_viral": "Eleve" if "Top" in fmt["name"] or "Drole" in fmt["name"] else "Moyen",
                    "difficulte": fmt["difficulty"],
                    "duree_recommandee": game_data["best_video_length"],
                    "retention_estimee": fmt["avg_retention"],
                    "hook_suggestion": random.choice(self.VIRAL_HOOKS).replace(
                        "{contrainte}", content_format
                    ),
                    "tags_suggeres": game_data["hashtags"],
                })

        return ideas

    def _generate_challenge_ideas(self, game_data):
        """Generate challenge video ideas."""
        ideas = []
        game = game_data["name"]
        elements = game_data["content_formats"]

        for challenge in self.CHALLENGE_IDEAS:
            element = random.choice(elements)
            challenge_desc = challenge.replace("{restriction}", element)
            challenge_desc = challenge_desc.replace("{element}", element)
            challenge_desc = challenge_desc.replace("{objectif}", "Champion")

            ideas.append({
                "titre": f"{game} mais {challenge_desc} !",
                "format": "challenge",
                "categorie": "Challenge / Defi",
                "description": f"Challenge unique sur {game} : {challenge_desc}",
                "potentiel_viral": "Eleve",
                "difficulte": "Moyen",
                "duree_recommandee": game_data["best_video_length"],
                "hook_suggestion": f"Est-ce que c'est POSSIBLE de {challenge_desc} sur {game} ?",
                "tags_suggeres": game_data["hashtags"] + ["#Challenge", "#Defi"],
            })

        return ideas

    def _generate_series_ideas(self, game_data):
        """Generate series/recurring content ideas."""
        ideas = []
        game = game_data["name"]

        for series in self.SERIES_IDEAS:
            title = series.replace("{game}", game)
            title = title.replace("{rang_max}", "Top 1")
            title = title.replace("{temps}", "30 jours")
            title = title.replace("{elements}", random.choice(game_data["content_formats"]))
            title = title.replace("{element}", random.choice(game_data["content_formats"]))
            title = title.replace("{n}", "1")

            ideas.append({
                "titre": f"{game} - {title}",
                "format": "hardcore_series",
                "categorie": "Serie",
                "description": f"Serie reguliere sur {game}. Format fidilisant a forte retention.",
                "potentiel_viral": "Moyen (mais forte retention)",
                "difficulte": "Difficile",
                "duree_recommandee": "15-25 min",
                "hook_suggestion": f"Episode 1 d'une NOUVELLE SERIE sur {game}...",
                "tags_suggeres": game_data["hashtags"] + ["#Serie", "#Episode1"],
                "note": "Les series creent de la fidelite. Les viewers reviennent pour chaque episode.",
            })

        return ideas

    def _generate_seasonal_ideas(self, game_data, year):
        """Generate ideas tied to current events/seasons."""
        ideas = []
        game = game_data["name"]
        month = datetime.now().month

        seasonal_events = {
            1: ("Nouvel An", f"Mes OBJECTIFS {game} pour {year}"),
            2: ("Saint-Valentin", f"Les MEILLEURS duos de {game}"),
            3: ("Printemps", f"Le RENOUVEAU de {game} en {year}"),
            4: ("Paques", f"Les SECRETS caches de {game} - Chasse aux oeufs"),
            5: ("Ete approche", f"Se PREPARER pour l'ete sur {game}"),
            6: ("E3/Summer Game Fest", f"Les ANNONCES {game} du Summer Game Fest"),
            7: ("Vacances", f"GUIDE COMPLET {game} pour les VACANCES"),
            8: ("Gamescom", f"{game} a la Gamescom - Recap"),
            9: ("Rentree", f"RENTREE {game} - La NOUVELLE META"),
            10: ("Halloween", f"{game} HALLOWEEN SPECIAL - MODE HORREUR"),
            11: ("Black Friday", f"Les MEILLEURES AFFAIRES gaming {year}"),
            12: ("Noel", f"SPECIAL NOEL {game} - Le BEST OF de l'annee"),
        }

        event_name, title = seasonal_events.get(month, ("", f"Les NEWS de {game}"))
        ideas.append({
            "titre": title,
            "format": "reaction",
            "categorie": f"Saisonnier - {event_name}",
            "description": f"Contenu lie a {event_name}. Bon pour le trafic saisonnier.",
            "potentiel_viral": "Moyen",
            "difficulte": "Facile",
            "duree_recommandee": "10-15 min",
            "hook_suggestion": f"Special {event_name} sur {game} !",
            "tags_suggeres": game_data["hashtags"] + [f"#{event_name.replace(' ', '')}"],
        })

        return ideas

    def _generate_collab_ideas(self, game_data):
        """Generate collaboration video ideas."""
        ideas = []
        game = game_data["name"]

        for collab in self.COLLAB_IDEAS:
            title = collab.replace("{game}", game)
            ideas.append({
                "titre": f"{game} - {title}",
                "format": "challenge",
                "categorie": "Collaboration",
                "description": f"Video collaborative. Ideal pour cross-promotion.",
                "potentiel_viral": "Eleve",
                "difficulte": "Moyen",
                "duree_recommandee": game_data["best_video_length"],
                "hook_suggestion": f"On fait un truc de FOU avec un abonne...",
                "tags_suggeres": game_data["hashtags"] + ["#Collab", "#Communaute"],
            })

        return ideas

    def _generate_generic_ideas(self, game_name, count):
        """Generate generic ideas for a game not in our database."""
        ideas = []
        year = datetime.now().year

        generic_templates = [
            {
                "titre": f"JE DECOUVRE {game_name} ET C'EST INCROYABLE !",
                "format": "first_look",
                "categorie": "Decouverte",
                "description": f"Premier regard sur {game_name}. Reactions et gameplay.",
            },
            {
                "titre": f"TOP 10 ASTUCES {game_name} que PERSONNE ne connait",
                "format": "top_list",
                "categorie": "Tips & Tricks",
                "description": f"Les meilleures astuces pour progresser sur {game_name}.",
            },
            {
                "titre": f"{game_name} GUIDE COMPLET DEBUTANT {year}",
                "format": "tutorial",
                "categorie": "Guide",
                "description": f"Guide complet pour bien debuter sur {game_name}.",
            },
            {
                "titre": f"LES MOMENTS LES PLUS FOUS SUR {game_name}",
                "format": "funny_moments",
                "categorie": "Funny Moments",
                "description": f"Compilation des meilleurs moments sur {game_name}.",
            },
            {
                "titre": f"{game_name} MAIS C'EST UN DEFI IMPOSSIBLE",
                "format": "challenge",
                "categorie": "Challenge",
                "description": f"Defi original et divertissant sur {game_name}.",
            },
            {
                "titre": f"100 JOURS HARDCORE SUR {game_name}",
                "format": "hardcore_series",
                "categorie": "Serie",
                "description": f"Serie hardcore sur {game_name}. Format a forte retention.",
            },
            {
                "titre": f"{game_name} en {year} - CA VAUT ENCORE LE COUP ?",
                "format": "reaction",
                "categorie": "Review",
                "description": f"Review honnete de {game_name} en {year}.",
            },
            {
                "titre": f"LES SECRETS CACHES DE {game_name}",
                "format": "story_lore",
                "categorie": "Lore / Secrets",
                "description": f"Exploration des secrets et du lore de {game_name}.",
            },
        ]

        for template in generic_templates:
            template.update({
                "potentiel_viral": "Moyen",
                "difficulte": "Moyen",
                "duree_recommandee": "10-15 min",
                "hook_suggestion": f"Vous n'allez PAS croire ce que j'ai decouvert sur {game_name}...",
                "tags_suggeres": [f"#{game_name.replace(' ', '')}", "#Gaming", "#YouTube"],
            })
            ideas.append(template)

        random.shuffle(ideas)
        return ideas[:count]

    def generate_shorts_ideas(self, game_name, count=5):
        """Generate YouTube Shorts specific ideas."""
        game_key = self._find_game_key(game_name)
        game_data = GAMES_DATABASE.get(game_key, {})
        game = game_data.get("name", game_name)

        shorts_templates = [
            f"LE MOMENT LE PLUS CLUTCH DE MA VIE sur {game} #Shorts",
            f"Cette astuce {game} va CHANGER votre vie #Shorts",
            f"POV : Tu decouvres un SECRET dans {game} #Shorts",
            f"{game} en 60 SECONDES #Shorts",
            f"Le PIRE fail de tous les temps sur {game} #Shorts",
            f"DEBUTANT vs PRO en 1 clip - {game} #Shorts",
            f"3 ASTUCES {game} que PERSONNE ne connait #Shorts",
            f"CE MOMENT ou tout bascule sur {game} #Shorts",
            f"SPEEDRUN {game} en 1 minute ! #Shorts",
            f"Reaction EXTREME sur {game} #Shorts",
        ]

        ideas = []
        selected = random.sample(shorts_templates, min(count, len(shorts_templates)))
        for title in selected:
            ideas.append({
                "titre": title,
                "format": "shorts_tiktok",
                "categorie": "YouTube Shorts",
                "description": "Format court (30-60s). Ideal pour gagner des abonnes.",
                "potentiel_viral": "Tres Eleve",
                "difficulte": "Facile",
                "duree_recommandee": "30-60 secondes",
                "conseils": [
                    "Les 3 premieres secondes doivent ACCROCHER",
                    "Sous-titres OBLIGATOIRES",
                    "Format vertical 9:16",
                    "Musique tendance en fond",
                    "Boucle parfaite = plus de vues (loop)",
                ],
                "tags_suggeres": (game_data.get("hashtags", []) or [f"#{game.replace(' ', '')}"]) + ["#Shorts", "#Gaming"],
            })

        return ideas
