#!/usr/bin/env python3
"""
YouTube Content Coach - Your complete YouTube gaming content assistant.

Interactive CLI tool for:
- Trend analysis
- Video idea generation
- Script writing
- Game-specific research
- SEO optimization
- Thumbnail guides
- Content calendars
"""

import json
import os
import sys
import textwrap
from datetime import datetime

# Add parent dir to path so we can run from anywhere
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_coach.modules.trend_analyzer import TrendAnalyzer
from youtube_coach.modules.idea_generator import IdeaGenerator
from youtube_coach.modules.script_writer import ScriptWriter
from youtube_coach.modules.game_researcher import GameResearcher
from youtube_coach.modules.seo_optimizer import SEOOptimizer


# ─── ANSI Colors ──────────────────────────────────────────────────────────────
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"


def c(text, color):
    """Colorize text."""
    return f"{color}{text}{Colors.RESET}"


def bold(text):
    return c(text, Colors.BOLD)


def header(text):
    return c(text, Colors.BOLD + Colors.CYAN)


def success(text):
    return c(text, Colors.GREEN)


def warning(text):
    return c(text, Colors.YELLOW)


def error(text):
    return c(text, Colors.RED)


def accent(text):
    return c(text, Colors.MAGENTA)


def dim(text):
    return c(text, Colors.DIM)


def separator(char="─", length=60):
    return dim(char * length)


def box(title, content_lines):
    """Draw a box around content."""
    width = max(len(title) + 4, max((len(line) for line in content_lines), default=40) + 4)
    width = min(width, 70)
    lines = []
    lines.append(c(f"┌{'─' * (width - 2)}┐", Colors.CYAN))
    lines.append(c(f"│ {title:<{width - 4}} │", Colors.CYAN + Colors.BOLD))
    lines.append(c(f"├{'─' * (width - 2)}┤", Colors.CYAN))
    for line in content_lines:
        # Truncate if too long
        display = line[:width - 4]
        padding = width - 4 - len(display)
        lines.append(c("│ ", Colors.CYAN) + display + " " * padding + c(" │", Colors.CYAN))
    lines.append(c(f"└{'─' * (width - 2)}┘", Colors.CYAN))
    return "\n".join(lines)


# ─── Application ──────────────────────────────────────────────────────────────
class YouTubeCoach:
    """Main application class."""

    def __init__(self):
        self.trend_analyzer = TrendAnalyzer()
        self.idea_generator = IdeaGenerator()
        self.script_writer = ScriptWriter()
        self.game_researcher = GameResearcher()
        self.seo_optimizer = SEOOptimizer()
        self.current_game = None

    def run(self):
        """Main application loop."""
        self._show_welcome()

        while True:
            try:
                self._show_main_menu()
                choice = input(f"\n{c('>', Colors.CYAN)} Votre choix : ").strip()

                if choice == "1":
                    self._menu_trends()
                elif choice == "2":
                    self._menu_ideas()
                elif choice == "3":
                    self._menu_scripts()
                elif choice == "4":
                    self._menu_game_research()
                elif choice == "5":
                    self._menu_seo()
                elif choice == "6":
                    self._menu_calendar()
                elif choice == "7":
                    self._menu_full_package()
                elif choice == "0" or choice.lower() in ("q", "quit", "exit"):
                    print(f"\n{success('Merci d avoir utilise YouTube Content Coach !')}")
                    print(f"{dim('Bonne creation et bonne chance sur YouTube !')}\n")
                    break
                else:
                    print(error("\nChoix invalide. Reessayez."))

            except KeyboardInterrupt:
                print(f"\n\n{success('Au revoir !')}")
                break
            except EOFError:
                print(f"\n\n{success('Au revoir !')}")
                break

    def _show_welcome(self):
        """Display welcome screen."""
        os.system("clear" if os.name != "nt" else "cls")
        print()
        print(c("╔══════════════════════════════════════════════════════════╗", Colors.CYAN))
        print(c("║                                                          ║", Colors.CYAN))
        print(c("║", Colors.CYAN) + c("       YOUTUBE CONTENT COACH v1.0", Colors.BOLD + Colors.WHITE) + c("                       ║", Colors.CYAN))
        print(c("║", Colors.CYAN) + c("    Votre assistant creation YouTube Gaming", Colors.YELLOW) + c("             ║", Colors.CYAN))
        print(c("║                                                          ║", Colors.CYAN))
        print(c("║", Colors.CYAN) + dim("  Tendances | Idees | Scripts | SEO | Recherche") + c("         ║", Colors.CYAN))
        print(c("║                                                          ║", Colors.CYAN))
        print(c("╚══════════════════════════════════════════════════════════╝", Colors.CYAN))
        print()

    def _show_main_menu(self):
        """Display main menu."""
        print(f"\n{separator()}")
        if self.current_game:
            print(f"{dim('Jeu actif :')} {accent(self.current_game)}")
        print(f"\n{header('MENU PRINCIPAL')}\n")
        menu_items = [
            ("1", "Analyser les tendances", "Decouvrir ce qui marche en ce moment"),
            ("2", "Generer des idees de videos", "Obtenir des idees creatives"),
            ("3", "Ecrire un script", "Script complet avec structure"),
            ("4", "Recherche approfondie d'un jeu", "Tout savoir pour creer du contenu"),
            ("5", "Optimisation SEO", "Titres, tags, miniatures"),
            ("6", "Calendrier de contenu", "Planning de publication"),
            ("7", "Package COMPLET", "Tout en un pour un jeu"),
            ("0", "Quitter", ""),
        ]
        for num, title, desc in menu_items:
            if num == "0":
                print(f"  {c(num, Colors.RED)}  {dim(title)}")
            else:
                print(f"  {c(num, Colors.CYAN)}  {bold(title)}")
                if desc:
                    print(f"     {dim(desc)}")

    def _ask_game(self, prompt="Quel jeu ?"):
        """Ask for a game name."""
        if self.current_game:
            use_current = input(
                f"{dim(f'Jeu actuel : {self.current_game}. Utiliser ? [O/n] : ')}"
            ).strip().lower()
            if use_current != "n":
                return self.current_game

        game = input(f"{c('>', Colors.CYAN)} {prompt} : ").strip()
        if game:
            self.current_game = game
        return game

    # ─── Trends Menu ──────────────────────────────────────────────────────────
    def _menu_trends(self):
        """Trends analysis menu."""
        print(f"\n{header('ANALYSE DES TENDANCES')}")
        print(f"\n  {c('1', Colors.CYAN)}  Jeux les plus populaires")
        print(f"  {c('2', Colors.CYAN)}  Tendances d'un jeu specifique")
        print(f"  {c('3', Colors.CYAN)}  Formats video qui marchent")
        print(f"  {c('4', Colors.CYAN)}  Tendances generales gaming")
        print(f"  {c('0', Colors.RED)}  {dim('Retour')}")

        choice = input(f"\n{c('>', Colors.CYAN)} Choix : ").strip()

        if choice == "1":
            self._show_trending_games()
        elif choice == "2":
            self._show_game_trends()
        elif choice == "3":
            self._show_trending_formats()
        elif choice == "4":
            self._show_general_trends()

    def _show_trending_games(self):
        """Display trending games."""
        games = self.trend_analyzer.get_trending_games(15)
        print(f"\n{header('TOP 15 JEUX LES PLUS POPULAIRES')}\n")

        for i, game in enumerate(games, 1):
            score = game["popularity_score"]
            bar_length = score // 5
            bar = c("█" * bar_length, Colors.GREEN if score >= 85 else Colors.YELLOW if score >= 70 else Colors.RED)
            empty = dim("░" * (20 - bar_length))

            print(f"  {c(f'{i:>2}.', Colors.CYAN)} {bold(game['name'][:25]): <28} {bar}{empty} {bold(str(score))}/100")
            print(f"      {dim(game['genre'])} | Top formats: {dim(', '.join(game['best_formats'][:3]))}")
            print()

    def _show_game_trends(self):
        """Display trends for a specific game."""
        game = self._ask_game("Quel jeu analyser ?")
        if not game:
            return

        print(f"\n{dim('Analyse en cours...')}")
        analysis = self.trend_analyzer.analyze_game_trends(game)

        if not analysis.get("found"):
            print(error(f"\n{analysis.get('message', 'Jeu non trouve.')}"))
            if "suggestion" in analysis:
                print(dim(analysis["suggestion"]))
            return

        print(f"\n{header(f'ANALYSE DES TENDANCES : {analysis[\"game\"]}')}\n")

        # General info
        info_lines = [
            f"Genre : {analysis['genre']}",
            f"Plateformes : {', '.join(analysis['platforms'])}",
            f"Audience : {analysis['audience_cible']}",
            f"Popularite : {analysis['score_popularite']}/100",
        ]
        print(box("Informations", info_lines))

        # Trending topics
        print(f"\n{bold('Sujets Tendance :')}")
        for topic in analysis["sujets_tendance"]:
            print(f"  {c('>', Colors.GREEN)} {topic}")

        # Best formats
        print(f"\n{bold('Meilleurs Formats :')}")
        for fmt in analysis["meilleurs_formats"][:6]:
            print(f"  {c('>', Colors.CYAN)} {fmt}")

        # Recommended settings
        print(f"\n{bold('Parametres Recommandes :')}")
        print(f"  Duree : {accent(analysis['duree_recommandee'])}")
        print(f"  Horaires : {accent(', '.join(analysis['meilleurs_horaires']))}")
        print(f"  Hashtags : {dim(' '.join(analysis['hashtags_recommandes']))}")

        # Recommendations
        print(f"\n{bold('Recommandations :')}")
        for rec in analysis["recommandations"]:
            print(f"  {c('!', Colors.YELLOW)} {rec}")

    def _show_trending_formats(self):
        """Display trending video formats."""
        formats = self.trend_analyzer.get_trending_formats()
        print(f"\n{header('FORMATS VIDEO POPULAIRES')}\n")

        for fmt in formats:
            retention = fmt["retention_moyenne"]
            print(f"  {c('>', Colors.CYAN)} {bold(fmt['name'])} {dim(f'(Retention: {retention})')}")
            print(f"    {fmt['description']}")
            print(f"    Difficulte : {self._difficulty_color(fmt['difficulte'])}")
            print(f"    Exemples : {dim(fmt['exemples_titres'][0])}")
            print()

    def _show_general_trends(self):
        """Display general gaming trends."""
        trends = self.trend_analyzer.get_general_trends()
        print(f"\n{header(f'TENDANCES GAMING - {trends[\"date\"]}')}\n")

        print(bold("Tendances Generales :"))
        for trend in trends["tendances_generales"]:
            print(f"  {c('>', Colors.GREEN)} {trend}")

        print(f"\n{bold('Formats Populaires :')}")
        for fmt in trends["formats_populaires"]:
            print(f"  {c('>', Colors.CYAN)} {fmt}")

        print(f"\n{bold('Conseils Algorithme YouTube :')}")
        for tip in trends["conseils_algorithme"]:
            print(f"  {c('!', Colors.YELLOW)} {tip}")

        print(f"\n{bold('Erreurs a Eviter :')}")
        for err in trends["erreurs_a_eviter"]:
            print(f"  {c('X', Colors.RED)} {err}")

    # ─── Ideas Menu ───────────────────────────────────────────────────────────
    def _menu_ideas(self):
        """Ideas generation menu."""
        print(f"\n{header('GENERATEUR D IDEES')}")
        print(f"\n  {c('1', Colors.CYAN)}  Idees de videos longues")
        print(f"  {c('2', Colors.CYAN)}  Idees de Shorts")
        print(f"  {c('0', Colors.RED)}  {dim('Retour')}")

        choice = input(f"\n{c('>', Colors.CYAN)} Choix : ").strip()

        if choice == "1":
            self._generate_video_ideas()
        elif choice == "2":
            self._generate_shorts_ideas()

    def _generate_video_ideas(self):
        """Generate and display video ideas."""
        game = self._ask_game("Pour quel jeu generer des idees ?")
        if not game:
            return

        try:
            count = int(input(f"{c('>', Colors.CYAN)} Combien d'idees ? (defaut: 10) : ").strip() or "10")
        except ValueError:
            count = 10

        print(f"\n{dim('Generation en cours...')}")
        ideas = self.idea_generator.generate_ideas(game, count=count)

        print(f"\n{header(f'IDEES DE VIDEOS - {game.upper()}')}\n")

        for i, idea in enumerate(ideas, 1):
            print(f"{c(f'  IDEE #{i}', Colors.BOLD + Colors.CYAN)}")
            print(f"  {bold(idea['titre'])}")
            print(f"  {dim(f'Format: {idea.get(\"categorie\", \"N/A\")} | '
                        f'Viral: {idea.get(\"potentiel_viral\", \"N/A\")} | '
                        f'Difficulte: {idea.get(\"difficulte\", \"N/A\")}')}")
            print(f"  {dim(f'Duree: {idea.get(\"duree_recommandee\", \"N/A\")}')}")
            print(f"  Hook : {accent(idea.get('hook_suggestion', ''))}")
            print(f"  {dim(idea.get('description', ''))}")
            print(f"  Tags : {dim(' '.join(idea.get('tags_suggeres', [])))}")
            print(separator("·", 50))
            print()

    def _generate_shorts_ideas(self):
        """Generate YouTube Shorts ideas."""
        game = self._ask_game("Pour quel jeu ?")
        if not game:
            return

        ideas = self.idea_generator.generate_shorts_ideas(game, count=5)

        print(f"\n{header(f'IDEES SHORTS - {game.upper()}')}\n")

        for i, idea in enumerate(ideas, 1):
            print(f"  {c(f'SHORT #{i}', Colors.BOLD + Colors.MAGENTA)}")
            print(f"  {bold(idea['titre'])}")
            print(f"  {dim(idea['description'])}")
            print(f"\n  {bold('Conseils :')}")
            for tip in idea.get("conseils", []):
                print(f"    {c('>', Colors.YELLOW)} {tip}")
            print()

    # ─── Scripts Menu ─────────────────────────────────────────────────────────
    def _menu_scripts(self):
        """Script writing menu."""
        game = self._ask_game("Pour quel jeu ?")
        if not game:
            return

        title = input(f"{c('>', Colors.CYAN)} Titre de la video : ").strip()
        if not title:
            print(error("Titre requis."))
            return

        print(f"\n{bold('Choisissez un format :')}")
        formats = [
            ("1", "standard_gaming", "Video Gaming Standard (10-15 min)"),
            ("2", "top_list", "Top / Tier List (12-18 min)"),
            ("3", "tutorial_guide", "Tutoriel / Guide (15-20 min)"),
            ("4", "funny_moments", "Funny Moments (10-15 min)"),
            ("5", "shorts_tiktok", "YouTube Shorts (30-60 sec)"),
        ]
        for num, _, desc in formats:
            print(f"  {c(num, Colors.CYAN)}  {desc}")

        fmt_choice = input(f"\n{c('>', Colors.CYAN)} Format (defaut: 1) : ").strip() or "1"
        fmt_map = {f[0]: f[1] for f in formats}
        video_format = fmt_map.get(fmt_choice, "standard_gaming")

        print(f"\n{dim('Generation du script...')}")
        script = self.script_writer.generate_script(game, title, video_format)

        self._display_script(script)

        # Option to generate SEO
        seo = input(f"\n{c('>', Colors.CYAN)} Generer le package SEO aussi ? [O/n] : ").strip().lower()
        if seo != "n":
            self._display_seo_for_script(game, title, video_format)

    def _display_script(self, script):
        """Display a generated script."""
        print(f"\n{header(f'SCRIPT : {script[\"titre_video\"]}')}")
        print(f"{dim(f'Jeu: {script[\"jeu\"]} | Format: {script[\"format\"]} | Date: {script[\"date_creation\"]}')}\n")

        for section in script["sections"]:
            print(c(f"{'=' * 60}", Colors.CYAN))
            print(f"{c(section['nom'], Colors.BOLD + Colors.YELLOW)}")
            print(f"{dim(f'Duree : {section[\"duree\"]}')}")
            print(c(f"{'─' * 60}", Colors.DIM))

            print(f"\n{bold('Instructions :')}")
            for inst in section["instructions"]:
                print(f"  {c('>', Colors.GREEN)} {inst}")

            print(f"\n{bold('Script :')}")
            for line in section["script_texte"].split("\n"):
                if line.strip():
                    if line.startswith("["):
                        print(f"  {c(line, Colors.MAGENTA)}")
                    elif line.startswith('"') or line.startswith("'"):
                        print(f"  {c(line, Colors.WHITE)}")
                    else:
                        print(f"  {line}")

            print(f"\n{bold('Notes de montage :')}")
            for note in section["notes_montage"]:
                print(f"  {c('!', Colors.YELLOW)} {note}")
            print()

        # Production notes
        print(f"\n{header('NOTES DE PRODUCTION')}")
        for note in script["notes_production"]:
            print(f"  {c('>', Colors.CYAN)} {note}")

        print(f"\n{header('MUSIQUES SUGGEREES')}")
        for music in script["musiques_suggerees"]:
            print(f"  {c('>', Colors.MAGENTA)} {music}")

        print(f"\n{header('EFFETS VISUELS')}")
        for effect in script["effets_visuels"]:
            print(f"  {c('>', Colors.GREEN)} {effect}")

    def _display_seo_for_script(self, game, title, video_format):
        """Display SEO data for a script."""
        seo_data = self.seo_optimizer.generate_seo_package(game, title, video_format)
        self._display_seo(seo_data)

        # Tags
        tags = self.script_writer.generate_tags(game, title)
        print(f"\n{header('TAGS YOUTUBE')}")
        print(f"  {dim(', '.join(tags))}")

        # Description
        desc = self.script_writer.generate_description(game, title)
        print(f"\n{header('DESCRIPTION YOUTUBE')}")
        print(dim("─" * 40))
        for line in desc.split("\n"):
            print(f"  {dim(line)}")

    # ─── Game Research Menu ───────────────────────────────────────────────────
    def _menu_game_research(self):
        """Game research menu."""
        game = self._ask_game("Quel jeu rechercher ?")
        if not game:
            return

        print(f"\n  {c('1', Colors.CYAN)}  Recherche complete")
        print(f"  {c('2', Colors.CYAN)}  Calendrier de contenu")
        print(f"  {c('0', Colors.RED)}  {dim('Retour')}")

        choice = input(f"\n{c('>', Colors.CYAN)} Choix : ").strip()

        if choice == "1":
            self._show_full_research(game)
        elif choice == "2":
            self._show_calendar(game)

    def _show_full_research(self, game):
        """Display full research report for a game."""
        print(f"\n{dim('Recherche en cours (cela peut prendre quelques secondes)...')}")
        report = self.game_researcher.full_research(game)

        print(f"\n{header(f'RAPPORT DE RECHERCHE : {report[\"jeu\"].upper()}')}")
        print(f"{dim(f'Date: {report[\"date_recherche\"]}')}\n")

        # General info
        info = report.get("informations_generales", {})
        info_lines = [f"{k}: {v}" for k, v in info.items()]
        print(box("Informations Generales", info_lines))

        # Content analysis
        content = report.get("analyse_contenu", {})
        print(f"\n{bold('Formats Recommandes :')}")
        for fmt in content.get("formats_recommandes", []):
            print(f"  {c('>', Colors.CYAN)} {fmt}")

        print(f"\n{bold('Sujets Tendance :')}")
        for topic in content.get("sujets_tendance", []):
            print(f"  {c('>', Colors.GREEN)} {topic}")

        # Optimal settings
        settings = report.get("parametres_optimaux", {})
        print(f"\n{bold('Parametres Optimaux :')}")
        for k, v in settings.items():
            print(f"  {accent(k)} : {v}")

        # Strategy
        strategy = report.get("strategie_contenu", {})
        print(f"\n{header('STRATEGIE DE CONTENU')}")
        print(f"  {strategy.get('resume', '')}")

        print(f"\n{bold('Piliers de Contenu :')}")
        for pillar in strategy.get("piliers_contenu", []):
            print(f"  {c('>', Colors.CYAN)} {pillar}")

        print(f"\n{bold('Calendrier Type :')}")
        for day, content_type in strategy.get("calendrier_type", {}).items():
            print(f"  {bold(day)} : {content_type}")

        print(f"\n{bold('Objectifs 30 Jours :')}")
        for obj in strategy.get("objectifs_30_jours", []):
            print(f"  {c('>', Colors.GREEN)} {obj}")

        print(f"\n{bold('KPIs a Suivre :')}")
        for kpi in strategy.get("kpis_a_suivre", []):
            print(f"  {c('>', Colors.YELLOW)} {kpi}")

        # Competition
        competition = report.get("analyse_concurrence", {})
        print(f"\n{header('ANALYSE CONCURRENCE')}")

        print(f"\n{bold('Comment se Differencier :')}")
        for tip in competition.get("comment_se_differencier", []):
            print(f"  {c('!', Colors.YELLOW)} {tip}")

        print(f"\n{bold('Opportunites Inexploitees :')}")
        for opp in competition.get("opportunites_inexploitees", []):
            print(f"  {c('>', Colors.GREEN)} {opp}")

    def _show_calendar(self, game):
        """Display content calendar."""
        try:
            weeks = int(input(f"{c('>', Colors.CYAN)} Nombre de semaines ? (defaut: 4) : ").strip() or "4")
        except ValueError:
            weeks = 4

        calendar = self.game_researcher.get_content_calendar(game, weeks)

        print(f"\n{header(f'CALENDRIER DE CONTENU : {calendar[\"jeu\"]}')}")
        print(f"{dim(f'Duree : {calendar[\"duree\"]}')}\n")

        for week in calendar["calendrier"]:
            print(c(f"{'─' * 50}", Colors.CYAN))
            print(f"{c(f'  SEMAINE {week[\"semaine\"]}', Colors.BOLD + Colors.YELLOW)}")
            print(c(f"{'─' * 50}", Colors.CYAN))

            for video in week["videos"]:
                print(f"  {bold(video['jour'])} - {video['format']}")
                print(f"    {dim(video['titre_suggestion'])}")
                print(f"    {dim(f'Duree: {video[\"duree\"]} | Publier a: {video[\"horaire\"]}')}")

            shorts = week.get("shorts", {})
            print(f"\n  {accent('Shorts')} : {shorts.get('frequence', '1/jour')}")
            for ex in shorts.get("exemples", []):
                print(f"    {dim(f'> {ex}')}")
            print()

        print(f"{bold('Conseils Planning :')}")
        for tip in calendar.get("conseils", []):
            print(f"  {c('>', Colors.GREEN)} {tip}")

    # ─── SEO Menu ─────────────────────────────────────────────────────────────
    def _menu_seo(self):
        """SEO optimization menu."""
        print(f"\n{header('OPTIMISATION SEO')}")
        print(f"\n  {c('1', Colors.CYAN)}  Analyser un titre")
        print(f"  {c('2', Colors.CYAN)}  Optimiser un titre")
        print(f"  {c('3', Colors.CYAN)}  Guide miniature")
        print(f"  {c('4', Colors.CYAN)}  Package SEO complet")
        print(f"  {c('0', Colors.RED)}  {dim('Retour')}")

        choice = input(f"\n{c('>', Colors.CYAN)} Choix : ").strip()

        if choice == "1":
            self._analyze_title()
        elif choice == "2":
            self._optimize_title()
        elif choice == "3":
            self._thumbnail_guide()
        elif choice == "4":
            self._full_seo_package()

    def _analyze_title(self):
        """Analyze a YouTube title."""
        title = input(f"{c('>', Colors.CYAN)} Entrez votre titre : ").strip()
        if not title:
            return

        analysis = self.seo_optimizer.analyze_title(title)

        print(f"\n{header('ANALYSE DU TITRE')}\n")
        print(f"  Titre : {bold(analysis['titre'])}")
        print(f"  Score : {self._score_color(analysis['score'])}/100 ({bold(analysis['note'])})")
        print(f"  Verdict : {analysis['verdict']}\n")

        for fb in analysis["feedback"]:
            if any(word in fb.lower() for word in ["ideal", "bien", "bon", "excellent"]):
                print(f"  {c('OK', Colors.GREEN)} {fb}")
            else:
                print(f"  {c('!!', Colors.YELLOW)} {fb}")

    def _optimize_title(self):
        """Optimize a title with suggestions."""
        title = input(f"{c('>', Colors.CYAN)} Votre titre actuel : ").strip()
        game = self._ask_game("Jeu (optionnel, Entree pour passer)")

        result = self.seo_optimizer.optimize_title(title, game if game else None)

        print(f"\n{header('SUGGESTIONS DE TITRES')}\n")
        print(f"  Original : {dim(result['titre_original'])}")
        print(f"  Longueur : {result['longueur_original']} car. {dim(result['conseil_longueur'])}\n")

        print(bold("  Suggestions optimisees :"))
        for i, suggestion in enumerate(result["suggestions_optimisees"], 1):
            score = self.seo_optimizer.analyze_title(suggestion)["score"]
            print(f"  {c(str(i), Colors.CYAN)}. {suggestion}")
            print(f"     {dim(f'Score: {score}/100')}")

        print(f"\n{bold('Regles du bon titre :')}")
        for rule in result["regles_titre"]:
            print(f"  {c('>', Colors.YELLOW)} {rule}")

    def _thumbnail_guide(self):
        """Display thumbnail creation guide."""
        game = self._ask_game("Pour quel jeu ?")
        guide = self.seo_optimizer.generate_thumbnail_guide(game if game else "Gaming")

        print(f"\n{header('GUIDE CREATION MINIATURE')}\n")

        specs = guide["specifications_techniques"]
        print(bold("Specifications :"))
        for k, v in specs.items():
            print(f"  {dim(k)} : {v}")

        print(f"\n{bold('Palette de Couleurs :')}")
        for color in guide["palette_couleurs"]:
            print(f"  {c('>', Colors.MAGENTA)} {color}")

        print(f"\n{bold('Elements Obligatoires :')}")
        for elem in guide["elements_obligatoires"]:
            print(f"  {c('>', Colors.GREEN)} {elem}")

        print(f"\n{bold('Conseils Design :')}")
        for tip in guide["conseils_design"]:
            print(f"  {c('!', Colors.YELLOW)} {tip}")

        print(f"\n{bold('Erreurs a Eviter :')}")
        for err in guide["erreurs_a_eviter"]:
            print(f"  {c('X', Colors.RED)} {err}")

        print(f"\n{bold('Outils Recommandes :')}")
        for tool in guide["outils_recommandes"]:
            print(f"  {c('>', Colors.CYAN)} {tool}")

        print(f"\n{accent('FORMULE :')} {guide['formule_miniature']}")

    def _full_seo_package(self):
        """Generate complete SEO package."""
        game = self._ask_game("Pour quel jeu ?")
        if not game:
            return
        title = input(f"{c('>', Colors.CYAN)} Titre de la video : ").strip()
        if not title:
            return

        package = self.seo_optimizer.generate_seo_package(game, title)
        self._display_seo(package)

    def _display_seo(self, seo_data):
        """Display SEO data."""
        # Title analysis
        analysis = seo_data.get("analyse_titre", {})
        print(f"\n{header('ANALYSE TITRE')}")
        print(f"  Score : {self._score_color(analysis.get('score', 0))}/100 ({analysis.get('note', '')})")
        for fb in analysis.get("feedback", []):
            print(f"  {dim(fb)}")

        # Title suggestions
        suggestions = seo_data.get("suggestions_titres", {})
        print(f"\n{header('SUGGESTIONS TITRES')}")
        for i, s in enumerate(suggestions.get("suggestions_optimisees", []), 1):
            print(f"  {c(str(i), Colors.CYAN)}. {s}")

        # Thumbnail
        thumb = seo_data.get("guide_miniature", {})
        print(f"\n{header('MINIATURE')}")
        print(f"  {accent(thumb.get('formule_miniature', ''))}")

        # Bonus formulas
        print(f"\n{header('FORMULES DE TITRES BONUS')}")
        for formula in seo_data.get("formules_titres_bonus", [])[:5]:
            print(f"  {c('>', Colors.MAGENTA)} {formula}")

    # ─── Calendar Menu ────────────────────────────────────────────────────────
    def _menu_calendar(self):
        """Content calendar menu."""
        game = self._ask_game("Pour quel jeu ?")
        if game:
            self._show_calendar(game)

    # ─── Full Package ─────────────────────────────────────────────────────────
    def _menu_full_package(self):
        """Generate everything for a game."""
        game = self._ask_game("Pour quel jeu voulez-vous le package complet ?")
        if not game:
            return

        print(f"\n{c('=' * 60, Colors.CYAN)}")
        print(f"{c('  PACKAGE COMPLET', Colors.BOLD + Colors.WHITE)} : {accent(game.upper())}")
        print(f"{c('=' * 60, Colors.CYAN)}")

        # 1. Trend Analysis
        print(f"\n{header('1/5 - ANALYSE DES TENDANCES')}")
        analysis = self.trend_analyzer.analyze_game_trends(game)
        if analysis.get("found"):
            info_lines = [
                f"Genre : {analysis['genre']}",
                f"Popularite : {analysis['score_popularite']}/100",
                f"Audience : {analysis['audience_cible']}",
                f"Duree recommandee : {analysis['duree_recommandee']}",
            ]
            print(box(analysis["game"], info_lines))
            print(f"\n  Sujets tendance : {', '.join(analysis['sujets_tendance'][:5])}")
        else:
            print(warning(f"  Jeu non trouve dans la base. Resultats generiques."))

        # 2. Ideas
        print(f"\n{header('2/5 - TOP 5 IDEES DE VIDEOS')}")
        ideas = self.idea_generator.generate_ideas(game, count=5)
        for i, idea in enumerate(ideas, 1):
            print(f"\n  {c(f'#{i}', Colors.CYAN)} {bold(idea['titre'])}")
            print(f"      {dim(f'{idea.get(\"categorie\", \"\")} | Viral: {idea.get(\"potentiel_viral\", \"\")}')}")

        # 3. Script for first idea
        print(f"\n{header('3/5 - SCRIPT (premiere idee)')}")
        if ideas:
            first_idea = ideas[0]
            script = self.script_writer.generate_script(
                game,
                first_idea["titre"],
                first_idea.get("format", "standard_gaming"),
            )
            print(f"\n  {bold(script['titre_video'])}")
            for section in script["sections"]:
                print(f"\n  {c(section['nom'], Colors.YELLOW)}")
                print(f"  {dim(section['duree'])}")
                preview = section["script_texte"][:150].replace("\n", " ")
                print(f"  {dim(preview)}...")

        # 4. SEO
        print(f"\n{header('4/5 - SEO')}")
        if ideas:
            seo = self.seo_optimizer.analyze_title(ideas[0]["titre"])
            print(f"  Score titre : {self._score_color(seo['score'])}/100 ({seo['note']})")
            tags = self.script_writer.generate_tags(game, ideas[0]["titre"])
            print(f"  Tags : {dim(', '.join(tags[:10]))}")

        # 5. Calendar
        print(f"\n{header('5/5 - CALENDRIER (4 semaines)')}")
        calendar = self.game_researcher.get_content_calendar(game, weeks=4)
        for week in calendar["calendrier"][:2]:  # Show first 2 weeks
            print(f"\n  {bold(f'Semaine {week[\"semaine\"]}')}")
            for video in week["videos"]:
                print(f"    {video['jour']} : {dim(video['format'])}")

        print(f"\n{dim('... + 2 semaines supplementaires')}")

        print(f"\n{c('=' * 60, Colors.GREEN)}")
        print(f"{success('  PACKAGE COMPLET GENERE AVEC SUCCES !')}")
        print(f"{c('=' * 60, Colors.GREEN)}")
        print(f"\n{dim('Utilisez les menus individuels pour plus de details sur chaque section.')}")

    # ─── Helpers ──────────────────────────────────────────────────────────────
    def _score_color(self, score):
        """Colorize a score."""
        if score >= 80:
            return c(str(score), Colors.GREEN)
        elif score >= 60:
            return c(str(score), Colors.YELLOW)
        else:
            return c(str(score), Colors.RED)

    def _difficulty_color(self, difficulty):
        """Colorize difficulty."""
        colors = {
            "Facile": Colors.GREEN,
            "Moyen": Colors.YELLOW,
            "Difficile": Colors.RED,
        }
        return c(difficulty, colors.get(difficulty, Colors.WHITE))


def main():
    """Entry point."""
    app = YouTubeCoach()
    app.run()


if __name__ == "__main__":
    main()
