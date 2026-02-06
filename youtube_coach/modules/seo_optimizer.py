"""
SEO Optimizer Module - Optimizes titles, descriptions, tags, and thumbnails.
"""

import random
import re
from datetime import datetime

from youtube_coach.data.games_database import GAMES_DATABASE
from youtube_coach.data.script_templates import SEO_TEMPLATES


class SEOOptimizer:
    """Optimizes YouTube content for maximum discoverability."""

    POWER_WORDS_FR = [
        "INCROYABLE", "SECRET", "MEILLEUR", "ULTIME", "COMPLET",
        "EXCLUSIF", "OFFICIEL", "NOUVEAU", "CASSE", "BROKEN",
        "CHOQUE", "IMPOSSIBLE", "EPIQUE", "LEGENDAIRE", "FOU",
        "INTERDIT", "CACHE", "RARE", "GRATUIT", "FACILE",
        "PRO", "TUTO", "GUIDE", "ASTUCE", "ERREUR",
    ]

    EMOTIONAL_TRIGGERS_FR = [
        "Vous n'allez PAS croire...",
        "PERSONNE ne fait ca...",
        "ATTENTION a cette erreur...",
        "Le SECRET que les pros cachent...",
        "ENFIN revele...",
        "Ca change TOUT...",
        "ARRETEZ de faire ca...",
        "La VERITE sur...",
    ]

    THUMBNAIL_COLORS = {
        "haute_performance": ["Rouge vif (#FF0000)", "Jaune (#FFD700)", "Blanc (#FFFFFF)"],
        "gaming": ["Vert neon (#00FF41)", "Violet (#9B59B6)", "Bleu electrique (#0099FF)"],
        "horreur": ["Rouge sombre (#8B0000)", "Noir (#000000)", "Blanc (#FFFFFF)"],
        "fun": ["Rose (#FF69B4)", "Orange (#FF6600)", "Cyan (#00FFFF)"],
    }

    def optimize_title(self, base_title, game_name=None):
        """Optimize a video title for maximum CTR."""
        suggestions = []

        # Rule 1: Length check
        title_length = len(base_title)
        length_ok = title_length <= 60

        # Generate variations
        suggestions.append(self._add_power_words(base_title))
        suggestions.append(self._add_brackets(base_title))
        suggestions.append(self._add_numbers(base_title))
        suggestions.append(self._add_urgency(base_title))
        suggestions.append(self._capitalize_strategy(base_title))

        if game_name:
            game_data = self._get_game_data(game_name)
            if game_data:
                suggestions.append(f"{game_data['name']} : {base_title}")
                suggestions.append(f"{base_title} | {game_data['name']} {datetime.now().year}")

        # Deduplicate and filter
        unique_suggestions = list(dict.fromkeys(suggestions))
        valid_suggestions = [s for s in unique_suggestions if len(s) <= 70 and s != base_title]

        return {
            "titre_original": base_title,
            "longueur_original": title_length,
            "longueur_ok": length_ok,
            "conseil_longueur": "Ideal: 40-60 caracteres" if not length_ok else "Bonne longueur !",
            "suggestions_optimisees": valid_suggestions[:6],
            "regles_titre": [
                "Maximum 60 caracteres (visible en entier sur mobile)",
                "Mettre les mots-cles importants AU DEBUT",
                "Utiliser des MAJUSCULES strategiques (1-2 mots max)",
                "Inclure des chiffres quand c'est possible",
                "Creer de la curiosite sans mentir (pas de clickbait toxique)",
                "Le titre doit fonctionner AVEC la miniature (complementaires)",
            ],
        }

    def _add_power_words(self, title):
        """Add power words to a title."""
        word = random.choice(self.POWER_WORDS_FR)
        return f"{title} - {word} !"

    def _add_brackets(self, title):
        """Add brackets for emphasis."""
        brackets = random.choice([
            "[GUIDE COMPLET]", "[TUTO]", "[FR]", "[EXCLUSIF]", "[NOUVEAU]"
        ])
        return f"{title} {brackets}"

    def _add_numbers(self, title):
        """Add numbers to make title more specific."""
        if not any(char.isdigit() for char in title):
            return f"TOP 10 {title}"
        return title

    def _add_urgency(self, title):
        """Add urgency to the title."""
        urgency = random.choice([
            "avant qu'il soit TROP TARD",
            "en " + str(datetime.now().year),
            "MAINTENANT",
        ])
        return f"{title} {urgency}"

    def _capitalize_strategy(self, title):
        """Apply strategic capitalization."""
        words = title.split()
        if len(words) >= 3:
            # Capitalize the most important word
            important_idx = len(words) // 2
            words[important_idx] = words[important_idx].upper()
        return " ".join(words)

    def _get_game_data(self, game_name):
        """Look up game in database."""
        name_lower = game_name.lower().replace(" ", "_").replace(":", "")
        if name_lower in GAMES_DATABASE:
            return GAMES_DATABASE[name_lower]
        for key, data in GAMES_DATABASE.items():
            if game_name.lower() in data["name"].lower() or game_name.lower() in key:
                return data
        return None

    def generate_thumbnail_guide(self, game_name, video_format="standard_gaming"):
        """Generate a detailed thumbnail creation guide."""
        game_data = self._get_game_data(game_name) if game_name else None
        game = game_data["name"] if game_data else game_name

        # Choose color palette
        if video_format in ("funny_moments",):
            palette = self.THUMBNAIL_COLORS["fun"]
        elif "horreur" in (game_data.get("genre", "").lower() if game_data else ""):
            palette = self.THUMBNAIL_COLORS["horreur"]
        else:
            palette = self.THUMBNAIL_COLORS["haute_performance"]

        return {
            "jeu": game,
            "format_video": video_format,
            "specifications_techniques": {
                "resolution": "1280 x 720 pixels (minimum)",
                "resolution_recommandee": "1920 x 1080 pixels",
                "format": "16:9",
                "taille_max": "2 MB",
                "formats_acceptes": "JPG, PNG, GIF, BMP",
            },
            "palette_couleurs": palette,
            "elements_obligatoires": [
                "Visage avec emotion forte (surprise, joie, choc)",
                "Texte GROS et LISIBLE (3-5 mots max)",
                "Contraste eleve (fond vs sujet)",
                "Image de gameplay claire et reconnaissable",
                "Pas plus de 3 elements visuels principaux",
            ],
            "conseils_design": [
                "Le texte doit etre lisible en PETIT (sur mobile)",
                "Utiliser des contours epais sur le texte (stroke)",
                "Fond : couleur unie ou blur du gameplay",
                "Le visage doit occuper ~30% de la miniature",
                "Tester la lisibilite en taille reduite",
                "Regarder ce qui fonctionne chez la concurrence",
                "Creer 2-3 versions et A/B tester",
            ],
            "erreurs_a_eviter": [
                "Trop de texte (illisible sur mobile)",
                "Couleurs ternes ou fades",
                "Image floue ou basse resolution",
                "Miniature sans rapport avec la video",
                "Trop d'elements visuels (confusion)",
                "Police difficile a lire",
                "Pas de visage/emotion (moins de clics)",
            ],
            "outils_recommandes": [
                "Canva (gratuit) - Templates YouTube",
                "Photoshop / GIMP - Edition avancee",
                "Remove.bg - Supprimer les fonds",
                "Thumbnail Test - Tester la visibilite",
            ],
            "formule_miniature": (
                "EMOTION (visage) + ACTION (gameplay) + TEXTE (3-5 mots) "
                "= Miniature a fort CTR"
            ),
        }

    def analyze_title(self, title):
        """Analyze a title and provide a score with recommendations."""
        score = 0
        feedback = []

        # Length check
        length = len(title)
        if 40 <= length <= 60:
            score += 20
            feedback.append("Longueur ideale (40-60 caracteres)")
        elif length <= 70:
            score += 10
            feedback.append("Longueur acceptable, idealement < 60 caracteres")
        else:
            feedback.append("TROP LONG - Sera coupe sur mobile. Reduisez a < 60 caracteres")

        # Power words
        has_power = any(word.upper() in title.upper() for word in self.POWER_WORDS_FR)
        if has_power:
            score += 15
            feedback.append("Contient des mots puissants (bien !)")
        else:
            feedback.append("Ajoutez un mot puissant (MEILLEUR, SECRET, INCROYABLE...)")

        # Numbers
        has_numbers = any(char.isdigit() for char in title)
        if has_numbers:
            score += 15
            feedback.append("Contient des chiffres (attire l'oeil)")
        else:
            feedback.append("Ajoutez des chiffres si possible (TOP 5, 10 astuces...)")

        # Caps strategy
        caps_words = sum(1 for word in title.split() if word.isupper() and len(word) > 1)
        if 1 <= caps_words <= 3:
            score += 15
            feedback.append("Bonnes majuscules strategiques")
        elif caps_words > 3:
            feedback.append("Trop de MAJUSCULES - gardez 1-3 mots max")
        else:
            feedback.append("Utilisez 1-3 mots en MAJUSCULES pour l'accent")
            score += 5

        # Curiosity/Emotion
        curiosity_patterns = [
            r"comment", r"pourquoi", r"secret", r"\?", r"!",
            r"personne", r"jamais", r"impossible", r"incroyable",
        ]
        has_curiosity = any(
            re.search(pattern, title, re.IGNORECASE)
            for pattern in curiosity_patterns
        )
        if has_curiosity:
            score += 20
            feedback.append("Cree de la curiosite/emotion (excellent)")
        else:
            feedback.append("Ajoutez un element de curiosite ou d'emotion")

        # Punctuation
        if "!" in title or "?" in title:
            score += 5
            feedback.append("Bonne utilisation de la ponctuation")

        # Year
        current_year = str(datetime.now().year)
        if current_year in title:
            score += 10
            feedback.append(f"Contient l'annee {current_year} (bon pour le SEO)")
        else:
            feedback.append(f"Ajoutez {current_year} pour le SEO si pertinent")

        return {
            "titre": title,
            "score": min(score, 100),
            "note": self._score_to_grade(score),
            "feedback": feedback,
            "verdict": self._score_to_verdict(score),
        }

    def _score_to_grade(self, score):
        """Convert score to letter grade."""
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

    def _score_to_verdict(self, score):
        """Convert score to verdict message."""
        if score >= 80:
            return "Excellent titre ! Pret a publier."
        elif score >= 60:
            return "Bon titre, mais peut etre ameliore."
        elif score >= 40:
            return "Titre moyen. Appliquez les suggestions ci-dessus."
        else:
            return "Titre faible. Reecrivez en suivant les recommandations."

    def generate_seo_package(self, game_name, video_title, video_format="standard_gaming"):
        """Generate a complete SEO package (title + description + tags + thumbnail guide)."""
        return {
            "analyse_titre": self.analyze_title(video_title),
            "suggestions_titres": self.optimize_title(video_title, game_name),
            "guide_miniature": self.generate_thumbnail_guide(game_name, video_format),
            "formules_titres_bonus": SEO_TEMPLATES["title_formulas"],
        }
