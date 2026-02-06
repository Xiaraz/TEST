"""
Script Writer Module - Generates complete video scripts.
"""

import random
from datetime import datetime

from youtube_coach.data.games_database import GAMES_DATABASE
from youtube_coach.data.script_templates import SCRIPT_TEMPLATES


class ScriptWriter:
    """Generates structured video scripts for YouTube gaming content."""

    def generate_script(self, game_name, video_title, video_format="standard_gaming", custom_points=None):
        """Generate a complete video script."""
        template = SCRIPT_TEMPLATES.get(video_format, SCRIPT_TEMPLATES["standard_gaming"])
        game_data = self._get_game_data(game_name)
        game = game_data.get("name", game_name) if game_data else game_name

        script = {
            "titre_video": video_title,
            "jeu": game,
            "format": template["name"],
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "sections": [],
            "notes_production": self._generate_production_notes(game_data),
            "musiques_suggerees": self._suggest_music(video_format),
            "effets_visuels": self._suggest_visual_effects(video_format),
        }

        for section in template["sections"]:
            script_section = {
                "nom": section["name"],
                "duree": section["duration"],
                "instructions": section["instructions"],
                "script_texte": self._fill_template(
                    section["template"],
                    game,
                    video_title,
                    custom_points,
                ),
                "notes_montage": self._generate_editing_notes(section["name"]),
            }
            script["sections"].append(script_section)

        return script

    def _get_game_data(self, game_name):
        """Look up game data from the database."""
        name_lower = game_name.lower().replace(" ", "_").replace(":", "")
        if name_lower in GAMES_DATABASE:
            return GAMES_DATABASE[name_lower]
        for key, data in GAMES_DATABASE.items():
            if game_name.lower() in data["name"].lower() or game_name.lower() in key:
                return data
        return None

    def _fill_template(self, template, game, title, custom_points):
        """Fill in script template with actual content."""
        filled = template
        filled = filled.replace("{action_principale}", f"faire quelque chose d'INCROYABLE sur {game}")
        filled = filled.replace("{sujet_video}", title)
        filled = filled.replace("{transition_vers_contenu}", "rentrons directement dans le vif du sujet")
        filled = filled.replace("{point_1}", f"la base que tout joueur de {game} doit connaitre")
        filled = filled.replace("{point_2}", f"les techniques avancees de {game}")
        filled = filled.replace("{question_engagement}", f"ce que VOUS pensez de {game} en ce moment")
        filled = filled.replace("{reaction_climax}", "C'EST PAS POSSIBLE")
        filled = filled.replace("{resume_video}", title)
        filled = filled.replace("{teaser_prochaine_video}", f"un truc encore plus fou sur {game}")

        if custom_points:
            for i, point in enumerate(custom_points):
                filled = filled.replace(f"{{custom_{i+1}}}", point)

        return filled

    def _generate_production_notes(self, game_data):
        """Generate production notes for the video."""
        notes = [
            "AUDIO : Utiliser un micro de bonne qualite. L'audio est plus important que la video.",
            "MINIATURE : Preparer 2-3 versions de miniature pour A/B testing.",
            "ECLAIRAGE : Si facecam, eclairage 3 points recommande.",
            "ENREGISTREMENT : Enregistrer gameplay en 1080p60 minimum.",
            "MONTAGE : Couper les temps morts. Rythme soutenu.",
        ]

        if game_data:
            notes.append(
                f"HORAIRE : Publier de preference a {', '.join(game_data.get('best_upload_times', ['18h-20h']))}."
            )
            notes.append(
                f"DUREE CIBLE : {game_data.get('best_video_length', '10-15 min')}."
            )

        return notes

    def _suggest_music(self, video_format):
        """Suggest music styles based on video format."""
        music_map = {
            "standard_gaming": [
                "Intro : Musique energique/electronique",
                "Gameplay : Lo-fi beats ou musique du jeu",
                "Climax : Musique epique/dramatique",
                "Outro : Musique chill/relaxante",
            ],
            "top_list": [
                "Fond : Musique suspense legere",
                "Revelations : Sound effect dramatique",
                "Top 1 : Musique epique triomphante",
            ],
            "tutorial_guide": [
                "Fond : Lo-fi study beats (calme)",
                "Points importants : Sound effect notification",
                "Recap : Musique positive/motivante",
            ],
            "funny_moments": [
                "Fond : Musique joyeuse/comique",
                "Fails : Sound effects cartoonesques",
                "Moments WTF : Vine boom / Bruh sound",
                "Best moments : Musique epique ironique",
            ],
            "shorts_tiktok": [
                "Musique TRENDING TikTok/Reels du moment",
                "Son viral en lien avec le contenu",
                "Beat drop synchro avec le moment fort",
            ],
        }
        return music_map.get(video_format, music_map["standard_gaming"])

    def _suggest_visual_effects(self, video_format):
        """Suggest visual effects based on video format."""
        effects_map = {
            "standard_gaming": [
                "Zoom rapide sur les moments forts",
                "Texte anime pour les phrases cles",
                "Transitions fluides entre les segments",
                "Facecam en picture-in-picture",
                "Fleches et cercles pour guider l'attention",
            ],
            "top_list": [
                "Numeros animes pour chaque position",
                "Barre de progression du classement",
                "Split screen pour comparaisons",
                "Effet reveal pour le numero 1",
            ],
            "tutorial_guide": [
                "Annotations et fleches directionnelles",
                "Zones surlignees sur le gameplay",
                "Texte explicatif a l'ecran",
                "Slow-motion pour les techniques",
                "Before/After side by side",
            ],
            "funny_moments": [
                "Zoom comique sur les visages/reactions",
                "Effets memes (deal with it, thug life)",
                "Replay au ralenti des fails",
                "Emojis et stickers animes",
                "Jump cuts rapides",
            ],
            "shorts_tiktok": [
                "SOUS-TITRES grands et dynamiques (OBLIGATOIRE)",
                "Transitions TikTok style",
                "Effet zoom/shake sur les moments forts",
                "Texte anime par mot",
                "Format VERTICAL 9:16",
            ],
        }
        return effects_map.get(video_format, effects_map["standard_gaming"])

    def _generate_editing_notes(self, section_name):
        """Generate editing notes for a specific section."""
        if "HOOK" in section_name:
            return [
                "MONTAGE RAPIDE - pas de temps mort",
                "Musique energique des la premiere seconde",
                "Texte a l'ecran pour renforcer le message",
                "Ce segment determine si le viewer reste ou part",
            ]
        elif "INTRO" in section_name:
            return [
                "Branding coherent (couleurs, logo)",
                "Enchainer rapidement vers le contenu",
                "Ne pas s'attarder sur le CTA",
            ]
        elif "RETENTION" in section_name or "PAUSE" in section_name:
            return [
                "Graphique ou animation pour la question",
                "Laisser un silence de 1-2 secondes pour que le viewer reflexisse",
                "Excellent moment pour un teaser du climax",
            ]
        elif "CLIMAX" in section_name:
            return [
                "Montage le plus travaille de la video",
                "Replays multi-angles si possible",
                "Reactions authentiques (ne pas en rajouter)",
                "Musique epique synchronisee",
            ]
        elif "CONCLU" in section_name or "OUTRO" in section_name:
            return [
                "Ecran de fin YouTube (20 secondes)",
                "Suggestions de videos pertinentes",
                "CTA clair et concis",
            ]
        else:
            return [
                "Maintenir un bon rythme de montage",
                "Couper les temps morts",
                "Ajouter des effets visuels pour maintenir l'attention",
            ]

    def generate_description(self, game_name, video_title, timestamps=None):
        """Generate an optimized YouTube description."""
        game_data = self._get_game_data(game_name)
        game = game_data.get("name", game_name) if game_data else game_name
        hashtags = game_data.get("hashtags", [f"#{game.replace(' ', '')}"]) if game_data else [f"#{game.replace(' ', '')}"]

        desc_parts = [
            f"{video_title}\n",
            f"Dans cette video, on se retrouve pour du contenu {game} !",
            "Si vous appreciez, n'hesitez pas a liker et vous abonner.\n",
        ]

        if timestamps:
            desc_parts.append("TIMESTAMPS :")
            for ts, label in timestamps:
                desc_parts.append(f"{ts} - {label}")
            desc_parts.append("")

        desc_parts.extend([
            "---",
            "RESEAUX SOCIAUX :",
            "Twitter : @votre_twitter",
            "Instagram : @votre_instagram",
            "Discord : lien_discord",
            "TikTok : @votre_tiktok",
            "",
            "---",
            f"Tags : {' '.join(hashtags)} #Gaming #YouTube #Gameplay",
        ])

        return "\n".join(desc_parts)

    def generate_tags(self, game_name, video_topic):
        """Generate optimized YouTube tags."""
        game_data = self._get_game_data(game_name)
        game = game_data.get("name", game_name) if game_data else game_name

        tags = [
            game,
            f"{game} gameplay",
            f"{game} fr",
            f"{game} francais",
            f"{game} {video_topic}",
            f"{game} {datetime.now().year}",
            f"{game} tips",
            f"{game} guide",
            "gaming",
            "gaming fr",
            "jeux video",
        ]

        if game_data:
            tags.extend([
                f"{game} {game_data['genre']}",
                *[f"{game} {fmt}" for fmt in game_data["content_formats"][:3]],
            ])

        return tags[:30]  # YouTube limit is ~500 chars, usually 30 tags max
