"""
Script templates for various YouTube video formats.
Each template provides a complete structure with timing and instructions.
"""

SCRIPT_TEMPLATES = {
    "standard_gaming": {
        "name": "Video Gaming Standard (10-15 min)",
        "sections": [
            {
                "name": "HOOK (0:00 - 0:30)",
                "duration": "30 secondes",
                "instructions": [
                    "Commencer avec un moment FORT du gameplay (clip excitant)",
                    "Phrase d'accroche choc ou question intrigante",
                    "Montrer le meilleur moment de la video en teaser",
                    "Transition rapide vers l'intro"
                ],
                "template": (
                    "[CLIP TEASER - Meilleur moment de la video]\n\n"
                    "\"Yo les gars, aujourd'hui on va {action_principale} "
                    "et croyez-moi, vous n'etes PAS prets pour ce qui va arriver...\"\n\n"
                    "[TRANSITION RAPIDE]"
                )
            },
            {
                "name": "INTRO (0:30 - 1:30)",
                "duration": "1 minute",
                "instructions": [
                    "Se presenter brievement",
                    "Expliquer le concept de la video",
                    "Donner une raison de rester jusqu'a la fin",
                    "Call-to-action rapide (like + sub)"
                ],
                "template": (
                    "\"Salut a tous, bienvenue sur la chaine ! "
                    "Aujourd'hui on se retrouve pour {sujet_video}.\n\n"
                    "Avant de commencer, si vous appreciez ce type de contenu, "
                    "n'hesitez pas a lacher un like et a vous abonner, "
                    "ca aide enormement la chaine !\n\n"
                    "Alors, {transition_vers_contenu}...\""
                )
            },
            {
                "name": "CONTENU PRINCIPAL - Partie 1 (1:30 - 5:00)",
                "duration": "3.5 minutes",
                "instructions": [
                    "Premier bloc de contenu / gameplay",
                    "Maintenir l'energie haute",
                    "Reactions naturelles et commentaires",
                    "Mini-climax a la fin de cette section"
                ],
                "template": (
                    "[GAMEPLAY + COMMENTAIRE]\n\n"
                    "\"OK donc la premiere chose a savoir c'est que {point_1}...\"\n\n"
                    "[Developpement avec exemples concrets]\n\n"
                    "[MOMENT FORT / REACTION]"
                )
            },
            {
                "name": "RETENTION BUMP (5:00 - 5:30)",
                "duration": "30 secondes",
                "instructions": [
                    "Rappeler ce qui arrive plus tard dans la video",
                    "Poser une question au public",
                    "Creer du suspense"
                ],
                "template": (
                    "\"Et attendez, le meilleur arrive... mais d'abord, "
                    "dites-moi en commentaire {question_engagement}. "
                    "Parce que ce qui arrive ensuite, c'est COMPLETEMENT fou...\""
                )
            },
            {
                "name": "CONTENU PRINCIPAL - Partie 2 (5:30 - 10:00)",
                "duration": "4.5 minutes",
                "instructions": [
                    "Deuxieme bloc de contenu",
                    "Augmenter progressivement l'intensite",
                    "Inclure le moment le plus excitant",
                    "Garder le rythme soutenu"
                ],
                "template": (
                    "[GAMEPLAY + COMMENTAIRE - INTENSITE CROISSANTE]\n\n"
                    "\"Maintenant on passe aux choses serieuses avec {point_2}...\"\n\n"
                    "[Developpement et climax principal]\n\n"
                    "[REACTION AU CLIMAX]"
                )
            },
            {
                "name": "CLIMAX (10:00 - 12:00)",
                "duration": "2 minutes",
                "instructions": [
                    "Moment le plus intense de la video",
                    "Reactions authentiques",
                    "Resoudre le suspense principal"
                ],
                "template": (
                    "[MOMENT CULMINANT DE LA VIDEO]\n\n"
                    "\"NON MAIS ATTENDEZ... {reaction_climax}!\"\n\n"
                    "[Replay / Slow-motion du moment fort]"
                )
            },
            {
                "name": "CONCLUSION (12:00 - 13:00)",
                "duration": "1 minute",
                "instructions": [
                    "Recapituler les points cles",
                    "Donner son avis personnel",
                    "Teaser la prochaine video",
                    "CTA final (like, comment, sub, notification)"
                ],
                "template": (
                    "\"Voila les gars, c'etait {resume_video} ! "
                    "J'espere que ca vous a plu.\n\n"
                    "N'oubliez pas de lacher un LIKE si vous avez apprecie, "
                    "abonnez-vous si c'est pas encore fait, "
                    "et activez la cloche pour ne rien rater !\n\n"
                    "Dans la prochaine video on va {teaser_prochaine_video}... "
                    "ca va etre ENORME.\n\n"
                    "A tres vite, ciao !\""
                )
            }
        ]
    },

    "top_list": {
        "name": "Top / Tier List (12-18 min)",
        "sections": [
            {
                "name": "HOOK (0:00 - 0:20)",
                "duration": "20 secondes",
                "instructions": [
                    "Montrer le #1 du classement en teaser",
                    "Question provocante",
                ],
                "template": (
                    "[TEASER DU #1 - Clip rapide]\n\n"
                    "\"Le numero 1 de ce classement va vous CHOQUER... "
                    "et je suis sur que 90% d'entre vous ne l'utilisent PAS.\""
                )
            },
            {
                "name": "INTRO + REGLES (0:20 - 1:30)",
                "duration": "1 minute 10",
                "instructions": [
                    "Expliquer les criteres du classement",
                    "Donner credibilite (experience, stats, sources)",
                    "CTA rapide"
                ],
                "template": (
                    "\"Salut a tous ! Aujourd'hui on fait le TOP {nombre} "
                    "des {sujet} dans {game}.\n\n"
                    "Ce classement est base sur {criteres}. "
                    "On commence du {nombre} jusqu'au numero 1...\""
                )
            },
            {
                "name": "POSITIONS {N} a {N/2+1} (1:30 - 7:00)",
                "duration": "5 minutes 30",
                "instructions": [
                    "1-2 minutes par position",
                    "Gameplay/images pour chaque entree",
                    "Stats et arguments",
                    "Comparaisons entre les entrees"
                ],
                "template": (
                    "\"En position numero {N}, on retrouve {item}...\"\n\n"
                    "[GAMEPLAY/IMAGES + EXPLICATION]\n\n"
                    "\"Ce qui le place ici c'est {raison}...\"\n\n"
                    "[REPETER POUR CHAQUE POSITION]"
                )
            },
            {
                "name": "PAUSE ENGAGEMENT (7:00 - 7:30)",
                "duration": "30 secondes",
                "instructions": [
                    "Demander les predictions du public",
                    "Encourager les commentaires",
                    "Creer du suspense pour le top 3"
                ],
                "template": (
                    "\"Avant de passer au TOP 3, dites-moi en commentaire "
                    "quel est VOTRE numero 1 ? Je suis curieux de voir "
                    "si on est d'accord...\""
                )
            },
            {
                "name": "TOP 3 - 2 - 1 (7:30 - 14:00)",
                "duration": "6 minutes 30",
                "instructions": [
                    "2-3 minutes par position",
                    "Plus de details et d'analyse",
                    "Build-up dramatique",
                    "Le #1 doit etre memorisable"
                ],
                "template": (
                    "\"Et maintenant... le TOP 3 !\"\n\n"
                    "[MUSIQUE EPIQUE]\n\n"
                    "\"Numero 3... {item3} !\"\n[ANALYSE DETAILLEE]\n\n"
                    "\"Numero 2... {item2} !\"\n[ANALYSE DETAILLEE]\n\n"
                    "\"Et le NUMERO 1... roulement de tambours... "
                    "{item1} !\"\n[ANALYSE ULTRA-DETAILLEE + POURQUOI #1]"
                )
            },
            {
                "name": "CONCLUSION (14:00 - 15:00)",
                "duration": "1 minute",
                "instructions": [
                    "Recap rapide du classement",
                    "Inviter au debat",
                    "CTA final"
                ],
                "template": (
                    "\"Voila pour ce TOP {nombre} ! "
                    "Est-ce que vous etes d'accord avec ce classement ? "
                    "Dites-le-moi en commentaire !\n\n"
                    "Like, abo, cloche, et on se retrouve bientot "
                    "pour {teaser} !\""
                )
            }
        ]
    },

    "tutorial_guide": {
        "name": "Tutoriel / Guide Complet (15-20 min)",
        "sections": [
            {
                "name": "HOOK (0:00 - 0:30)",
                "duration": "30 secondes",
                "instructions": [
                    "Montrer le resultat final (avant/apres)",
                    "Promettre un benefice clair"
                ],
                "template": (
                    "[MONTRER LE RESULTAT - Gameplay du niveau atteint]\n\n"
                    "\"En seulement {temps}, vous allez passer de {avant} "
                    "a {apres}. Je vous montre TOUT.\""
                )
            },
            {
                "name": "INTRO + TABLE DES MATIERES (0:30 - 2:00)",
                "duration": "1 minute 30",
                "instructions": [
                    "Lister les chapitres avec timestamps",
                    "Etablir la credibilite",
                    "CTA"
                ],
                "template": (
                    "\"Dans ce guide on va couvrir :\n"
                    "1. {chapitre_1} a {timestamp_1}\n"
                    "2. {chapitre_2} a {timestamp_2}\n"
                    "3. {chapitre_3} a {timestamp_3}\n"
                    "4. {chapitre_4} a {timestamp_4}\n\n"
                    "N'hesitez pas a utiliser les chapitres pour naviguer.\""
                )
            },
            {
                "name": "CHAPITRE 1 - Les Bases (2:00 - 6:00)",
                "duration": "4 minutes",
                "instructions": [
                    "Commencer par les fondamentaux",
                    "Explications claires avec demonstrations",
                    "Rythme modere pour la comprehension"
                ],
                "template": (
                    "\"Chapitre 1 : {titre_chapitre_1}\n\n"
                    "La premiere chose a maitriser c'est {concept}...\"\n\n"
                    "[DEMONSTRATION VISUELLE]\n"
                    "[EXPLICATION PAS A PAS]"
                )
            },
            {
                "name": "CHAPITRE 2 - Intermediaire (6:00 - 10:00)",
                "duration": "4 minutes",
                "instructions": [
                    "Concepts intermediaires",
                    "Erreurs courantes a eviter",
                    "Exemples pratiques"
                ],
                "template": (
                    "\"Chapitre 2 : {titre_chapitre_2}\n\n"
                    "Maintenant qu'on a les bases, passons a {concept_2}...\"\n\n"
                    "[ERREURS A EVITER]\n"
                    "[BONNE METHODE]\n"
                    "[COMPARAISON]"
                )
            },
            {
                "name": "CHAPITRE 3 - Avance (10:00 - 14:00)",
                "duration": "4 minutes",
                "instructions": [
                    "Techniques avancees",
                    "Astuces de pro",
                    "Situations reelles"
                ],
                "template": (
                    "\"Chapitre 3 : {titre_chapitre_3}\n\n"
                    "La c'est la ou ca devient VRAIMENT interessant...\"\n\n"
                    "[TECHNIQUES AVANCEES]\n"
                    "[EXEMPLES EN JEU]"
                )
            },
            {
                "name": "CHAPITRE 4 - Tips Pro (14:00 - 17:00)",
                "duration": "3 minutes",
                "instructions": [
                    "Secrets et astuces cachees",
                    "Optimisations",
                    "Ce qui separe les bons des tres bons"
                ],
                "template": (
                    "\"Chapitre 4 : {titre_chapitre_4}\n\n"
                    "Ces astuces-la, meme les joueurs experimentes "
                    "ne les connaissent pas toutes...\"\n\n"
                    "[ASTUCES PRO]\n"
                    "[DEMONSTRATIONS]"
                )
            },
            {
                "name": "RECAP + CONCLUSION (17:00 - 18:30)",
                "duration": "1 minute 30",
                "instructions": [
                    "Resume des points cles",
                    "Plan d'entrainement suggere",
                    "CTA final"
                ],
                "template": (
                    "\"Pour resumer :\n"
                    "- {recap_1}\n- {recap_2}\n"
                    "- {recap_3}\n- {recap_4}\n\n"
                    "Mon conseil : commencez par {conseil}.\n\n"
                    "Like, abo, et dites-moi en commentaire {question} !\""
                )
            }
        ]
    },

    "funny_moments": {
        "name": "Funny Moments / Compilation (10-15 min)",
        "sections": [
            {
                "name": "COLD OPEN (0:00 - 0:15)",
                "duration": "15 secondes",
                "instructions": [
                    "Le moment le PLUS drole de la video directement",
                    "Pas d'intro, pas de blabla"
                ],
                "template": "[LE MEILLEUR CLIP - Direct sans intro]"
            },
            {
                "name": "INTRO RAPIDE (0:15 - 0:30)",
                "duration": "15 secondes",
                "instructions": [
                    "Branding rapide (logo/animation)",
                    "Pas de long discours"
                ],
                "template": (
                    "[ANIMATION INTRO - 5 secondes max]\n\n"
                    "\"C'est parti pour les meilleurs moments de la semaine !\""
                )
            },
            {
                "name": "BLOC 1 - Fails (0:30 - 4:00)",
                "duration": "3 minutes 30",
                "instructions": [
                    "Enchainer les clips de fails",
                    "Varier les situations",
                    "Reactions naturelles entre les clips",
                    "Sound effects et zoom pour accentuer"
                ],
                "template": (
                    "[CLIP 1 - Setup + Punchline]\n"
                    "[REACTION]\n"
                    "[CLIP 2 - Montee en intensite]\n"
                    "[REACTION]\n"
                    "...\n"
                    "[CLIP FINAL DU BLOC - Le plus gros fail]"
                )
            },
            {
                "name": "BLOC 2 - Moments WTF (4:00 - 7:30)",
                "duration": "3 minutes 30",
                "instructions": [
                    "Moments inexplicables et absurdes",
                    "Pauses pour laisser le spectateur reagir",
                    "Replays au ralenti"
                ],
                "template": (
                    "[CLIPS WTF ENCHAINES]\n"
                    "[SLOW MOTION + ZOOM sur les moments cles]\n"
                    "[REACTIONS AUTHENTIQUES]"
                )
            },
            {
                "name": "BLOC 3 - Best Moments (7:30 - 11:00)",
                "duration": "3 minutes 30",
                "instructions": [
                    "Les meilleurs plays/moments",
                    "Finir sur une note haute",
                    "Crescendo d'intensite"
                ],
                "template": (
                    "[CLIPS BEST OF - du bon au LEGENDAIRE]\n"
                    "[CHAQUE CLIP plus impressionnant que le precedent]\n"
                    "[CLIP FINAL EPIQUE]"
                )
            },
            {
                "name": "OUTRO (11:00 - 11:30)",
                "duration": "30 secondes",
                "instructions": [
                    "Ecran de fin avec suggestions",
                    "CTA court",
                    "Clip bonus rapide"
                ],
                "template": (
                    "[CLIP BONUS DROLE]\n\n"
                    "\"C'est tout pour aujourd'hui ! "
                    "Like + Abo et envoyez vos clips pour le prochain episode !\"\n\n"
                    "[ECRAN DE FIN - 20 secondes]"
                )
            }
        ]
    },

    "shorts_tiktok": {
        "name": "YouTube Shorts / Format Court (30-60 sec)",
        "sections": [
            {
                "name": "HOOK (0:00 - 0:03)",
                "duration": "3 secondes",
                "instructions": [
                    "TOUT se joue dans les 3 premieres secondes",
                    "Visuel accrocheur ou phrase choc",
                    "Texte a l'ecran obligatoire"
                ],
                "template": (
                    "[TEXTE A L'ECRAN: phrase accrocheuse]\n"
                    "\"ATTENDEZ de voir ca...\" / [ACTION IMMEDIATE]"
                )
            },
            {
                "name": "CONTENU (0:03 - 0:50)",
                "duration": "47 secondes",
                "instructions": [
                    "Aller DROIT au but",
                    "Pas de temps mort",
                    "Sous-titres obligatoires",
                    "Musique tendance en fond"
                ],
                "template": (
                    "[CONTENU RAPIDE ET DYNAMIQUE]\n"
                    "[SOUS-TITRES GRANDS ET COLORES]\n"
                    "[TRANSITIONS RAPIDES]\n"
                    "[MUSIQUE TRENDING]"
                )
            },
            {
                "name": "PAYOFF (0:50 - 0:58)",
                "duration": "8 secondes",
                "instructions": [
                    "Le moment de payoff / revelation",
                    "Reaction forte",
                    "Laisser le suspense pour encourager le rewatch"
                ],
                "template": (
                    "[MOMENT DE PAYOFF]\n"
                    "[REACTION FORTE]\n"
                    "\"Follow pour plus !\" / [LOOP VERS LE DEBUT]"
                )
            }
        ]
    }
}


SEO_TEMPLATES = {
    "description_template": (
        "{hook_description}\n\n"
        "Dans cette video :\n"
        "{bullet_points}\n\n"
        "---\n"
        "TIMESTAMPS :\n"
        "{timestamps}\n\n"
        "---\n"
        "LIENS UTILES :\n"
        "{links}\n\n"
        "---\n"
        "RESEAUX SOCIAUX :\n"
        "{social_links}\n\n"
        "---\n"
        "Tags : {tags}\n\n"
        "#gaming #{game_hashtag} #{format_hashtag}"
    ),
    "title_formulas": [
        "J'AI {action} SUR {game} ET C'EST {reaction} !",
        "{game} : Le SECRET que PERSONNE ne connait...",
        "COMMENT {objectif} sur {game} en {year} (Guide COMPLET)",
        "TOP {nombre} des MEILLEURS {sujet} dans {game}",
        "CE {sujet} est COMPLETEMENT CASSE sur {game} !",
        "{game} mais {twist} - DEFI IMPOSSIBLE",
        "JE TESTE {sujet} sur {game} pour la PREMIERE FOIS",
        "LES {nombre} ERREURS qui vous font PERDRE sur {game}",
        "DE {rang_bas} A {rang_haut} en {temps} sur {game}",
        "{game} SAISON {numero} - TOUT ce qu'il faut SAVOIR"
    ]
}
