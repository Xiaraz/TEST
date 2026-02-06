"""
Database of popular games with metadata for content creation.
Includes genres, audiences, content formats, and trending topics.
"""

GAMES_DATABASE = {
    # --- Battle Royale ---
    "fortnite": {
        "name": "Fortnite",
        "genre": "Battle Royale",
        "platforms": ["PC", "PS5", "Xbox", "Switch", "Mobile"],
        "audience": "8-25 ans",
        "popularity_score": 95,
        "content_formats": [
            "Gameplay highlights", "Build battles", "Funny moments",
            "Skin reviews", "Map changes", "Tournament recaps",
            "Tips & tricks", "Challenge guides", "Season updates",
            "Creative mode showcases", "Collaborations/Events"
        ],
        "trending_topics": [
            "Nouvelle saison", "Nouveaux skins", "Mises a jour",
            "Tournois", "Collaborations", "Modes creatifs"
        ],
        "best_video_length": "10-15 min",
        "best_upload_times": ["14h-16h", "18h-20h"],
        "hashtags": ["#Fortnite", "#FortniteBR", "#FortniteClips", "#FortniteSeason"],
        "competitors_formats": [
            "Top 5/10 moments", "1v1 build fights", "Challenge videos",
            "Story mode theories", "Live events reactions"
        ]
    },
    "apex_legends": {
        "name": "Apex Legends",
        "genre": "Battle Royale / FPS",
        "platforms": ["PC", "PS5", "Xbox", "Switch"],
        "audience": "16-30 ans",
        "popularity_score": 82,
        "content_formats": [
            "Ranked gameplay", "Legend guides", "Tips & tricks",
            "Weapon tier lists", "Patch reviews", "Pro player analysis",
            "Funny moments", "Clutch compilations", "Map rotations"
        ],
        "trending_topics": [
            "Nouvelle legende", "Changements de meta", "Ranked split",
            "Balance patches", "Esports ALGS", "Season updates"
        ],
        "best_video_length": "12-18 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#ApexLegends", "#Apex", "#ApexClips", "#ApexRanked"],
        "competitors_formats": [
            "Road to Predator", "Legend tier lists", "Aim guides",
            "Movement tech tutorials", "Weapon comparisons"
        ]
    },
    "warzone": {
        "name": "Call of Duty: Warzone",
        "genre": "Battle Royale / FPS",
        "platforms": ["PC", "PS5", "Xbox"],
        "audience": "16-35 ans",
        "popularity_score": 85,
        "content_formats": [
            "Loadout guides", "Win gameplay", "Funny moments",
            "Tips & tricks", "Weapon builds", "Map strategies",
            "Solo vs squads", "Kill records", "Meta analysis"
        ],
        "trending_topics": [
            "Meilleur loadout", "Nouvelle map", "Meta weapons",
            "Season update", "Anti-cheat updates", "Tournois"
        ],
        "best_video_length": "10-15 min",
        "best_upload_times": ["16h-18h", "20h-22h"],
        "hashtags": ["#Warzone", "#CODWarzone", "#CallOfDuty", "#Warzone3"],
        "competitors_formats": [
            "Best class setups", "High kill games", "No-scope montages",
            "1v4 clutches", "Rebirth Island strategies"
        ]
    },

    # --- MOBA ---
    "league_of_legends": {
        "name": "League of Legends",
        "genre": "MOBA",
        "platforms": ["PC"],
        "audience": "16-30 ans",
        "popularity_score": 92,
        "content_formats": [
            "Champion guides", "Ranked gameplay", "Patch analysis",
            "Pro player highlights", "Tier lists", "Funny moments",
            "Coaching sessions", "Off-meta builds", "LEC/LCK/Worlds coverage"
        ],
        "trending_topics": [
            "Nouveau champion", "Patch notes", "Worlds", "Meta shifts",
            "Reworks", "Esports drama", "Season changes"
        ],
        "best_video_length": "15-25 min",
        "best_upload_times": ["14h-16h", "19h-21h"],
        "hashtags": ["#LeagueOfLegends", "#LoL", "#RiotGames", "#LEC", "#Worlds"],
        "competitors_formats": [
            "Unranked to Challenger", "One-trick content", "Champion spotlights",
            "Patch rundowns", "Esports analysis"
        ]
    },
    "valorant": {
        "name": "Valorant",
        "genre": "FPS Tactique",
        "platforms": ["PC", "PS5", "Xbox"],
        "audience": "14-28 ans",
        "popularity_score": 90,
        "content_formats": [
            "Agent guides", "Aim training", "Ranked gameplay",
            "Lineups & setups", "Pro analysis", "Patch reviews",
            "Funny moments", "Clutch compilations", "Map guides"
        ],
        "trending_topics": [
            "Nouvel agent", "Changements de map", "VCT/Champions",
            "Meta shifts", "Nerfs/Buffs", "New skins"
        ],
        "best_video_length": "10-18 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#Valorant", "#ValorantClips", "#VCT", "#RiotGames"],
        "competitors_formats": [
            "Radiant gameplay", "Agent tier lists", "Crosshair guides",
            "Sensitivity settings pro", "Aim training routines"
        ]
    },

    # --- Sandbox / Survie ---
    "minecraft": {
        "name": "Minecraft",
        "genre": "Sandbox / Survie",
        "platforms": ["PC", "PS5", "Xbox", "Switch", "Mobile"],
        "audience": "8-30 ans",
        "popularity_score": 98,
        "content_formats": [
            "Let's Play survie", "Redstone tutorials", "Build showcases",
            "Mod reviews", "Challenges", "Speedruns", "Hardcore series",
            "PvP highlights", "Server events", "Update reviews"
        ],
        "trending_topics": [
            "Nouvelle mise a jour", "Mods populaires", "Challenges viraux",
            "Hardcore 100 days", "Build competitions", "Speedrun records"
        ],
        "best_video_length": "15-30 min",
        "best_upload_times": ["14h-16h", "17h-19h"],
        "hashtags": ["#Minecraft", "#MinecraftBuilds", "#MinecraftMods", "#Hardcore"],
        "competitors_formats": [
            "100 Days Hardcore", "Skyblock series", "Civilization experiments",
            "Redstone contraptions", "Modpack playthroughs"
        ]
    },
    "gta_v": {
        "name": "GTA V / GTA Online",
        "genre": "Action / Open World",
        "platforms": ["PC", "PS5", "Xbox"],
        "audience": "16-35 ans",
        "popularity_score": 88,
        "content_formats": [
            "Money guides", "Heist walkthroughs", "Funny moments",
            "Car meets", "Roleplay highlights", "DLC reviews",
            "Tips for beginners", "PvP montages", "GTA 6 theories"
        ],
        "trending_topics": [
            "Nouveau DLC", "GTA 6 leaks", "Money glitches",
            "Roleplay servers", "Car customization", "Weekly updates"
        ],
        "best_video_length": "12-20 min",
        "best_upload_times": ["16h-18h", "20h-22h"],
        "hashtags": ["#GTAV", "#GTAOnline", "#GTA6", "#Rockstar"],
        "competitors_formats": [
            "Beginner to rich guides", "RP stories", "Stunt montages",
            "Car comparison videos", "Weekly update recaps"
        ]
    },

    # --- RPG ---
    "elden_ring": {
        "name": "Elden Ring",
        "genre": "Action RPG / Souls-like",
        "platforms": ["PC", "PS5", "Xbox"],
        "audience": "18-35 ans",
        "popularity_score": 86,
        "content_formats": [
            "Boss guides", "Build guides", "Lore analysis",
            "DLC walkthroughs", "PvP builds", "Secrets & hidden items",
            "Challenge runs", "No-hit runs", "Beginner tips"
        ],
        "trending_topics": [
            "DLC content", "Best builds", "Lore theories",
            "PvP meta", "Speedrun records", "Hidden secrets"
        ],
        "best_video_length": "15-25 min",
        "best_upload_times": ["14h-16h", "19h-21h"],
        "hashtags": ["#EldenRing", "#FromSoftware", "#Soulsborne", "#EldenRingDLC"],
        "competitors_formats": [
            "All bosses ranked", "OP build guides", "Lore deep dives",
            "Challenge run series", "DLC theories"
        ]
    },
    "palworld": {
        "name": "Palworld",
        "genre": "Survie / Creature Collector",
        "platforms": ["PC", "Xbox"],
        "audience": "12-30 ans",
        "popularity_score": 78,
        "content_formats": [
            "Starter guides", "Best Pals tier list", "Base building",
            "Breeding guides", "Boss fights", "Tips & tricks",
            "Funny moments", "Multiplayer gameplay", "Update reviews"
        ],
        "trending_topics": [
            "New updates", "Best Pals", "Breeding combos",
            "Base optimization", "New content", "PvP"
        ],
        "best_video_length": "12-20 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#Palworld", "#PalworldGame", "#PalworldGuide"],
        "competitors_formats": [
            "All Pals ranked", "Starter guides", "Base design tours",
            "Breeding guides", "Fastest progression"
        ]
    },

    # --- Horreur ---
    "phasmophobia": {
        "name": "Phasmophobia",
        "genre": "Horreur / Co-op",
        "platforms": ["PC", "VR"],
        "audience": "16-30 ans",
        "popularity_score": 72,
        "content_formats": [
            "Ghost hunting gameplay", "Jump scare compilations",
            "Tips for beginners", "Evidence guides", "Funny moments",
            "Solo challenges", "Update reviews", "VR gameplay"
        ],
        "trending_topics": [
            "New ghosts", "Updates", "VR improvements",
            "Difficulty challenges", "New equipment"
        ],
        "best_video_length": "15-25 min",
        "best_upload_times": ["18h-20h", "21h-23h"],
        "hashtags": ["#Phasmophobia", "#HorrorGaming", "#GhostHunting"],
        "competitors_formats": [
            "Funniest moments compilations", "Solo nightmare mode",
            "All ghosts explained", "VR reactions"
        ]
    },

    # --- Sports / Racing ---
    "fifa_fc": {
        "name": "EA Sports FC (FIFA)",
        "genre": "Sports / Football",
        "platforms": ["PC", "PS5", "Xbox", "Switch"],
        "audience": "12-35 ans",
        "popularity_score": 87,
        "content_formats": [
            "Pack openings", "Squad building", "Career mode",
            "Pro Clubs", "Skills tutorials", "Player reviews",
            "Trading tips", "Weekend League recaps", "Draft challenges"
        ],
        "trending_topics": [
            "TOTS", "TOTY", "New promos", "Market crashes",
            "SBCs", "Icon reviews", "Meta formations"
        ],
        "best_video_length": "10-18 min",
        "best_upload_times": ["14h-16h", "18h-20h"],
        "hashtags": ["#EAFC", "#FIFA", "#FUT", "#UltimateTeam"],
        "competitors_formats": [
            "Road to Glory", "Pack opening reactions", "Player reviews",
            "Best formation guides", "Trading to millions"
        ]
    },
    "rocket_league": {
        "name": "Rocket League",
        "genre": "Sports / Vehiculaire",
        "platforms": ["PC", "PS5", "Xbox", "Switch"],
        "audience": "12-28 ans",
        "popularity_score": 75,
        "content_formats": [
            "Freestyle montages", "Ranked gameplay", "Tips & mechanics",
            "Training pack guides", "Pro analysis", "Funny moments",
            "1v1 challenges", "Road to SSL", "Car design showcases"
        ],
        "trending_topics": [
            "New season", "RLCS", "Mechanics tutorials",
            "New items", "Freestyle community", "Rank distribution"
        ],
        "best_video_length": "10-15 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#RocketLeague", "#RLCS", "#Freestyle", "#RocketLeagueClips"],
        "competitors_formats": [
            "Road to SSL series", "Freestyle compilations",
            "Mechanical tutorials", "Pro gameplay analysis"
        ]
    },

    # --- Strategie ---
    "clash_royale": {
        "name": "Clash Royale",
        "genre": "Strategie / Cartes",
        "platforms": ["Mobile"],
        "audience": "10-25 ans",
        "popularity_score": 74,
        "content_formats": [
            "Best decks", "Card reviews", "Challenge guides",
            "Funny moments", "Pro gameplay", "Tier lists",
            "F2P guides", "Clan wars strategies", "Update reviews"
        ],
        "trending_topics": [
            "Balance changes", "New cards", "Best meta decks",
            "CRL", "Season pass", "Evolution cards"
        ],
        "best_video_length": "8-15 min",
        "best_upload_times": ["12h-14h", "17h-19h"],
        "hashtags": ["#ClashRoyale", "#CR", "#Supercell", "#ClashRoyaleDeck"],
        "competitors_formats": [
            "Top ladder gameplay", "Best deck guides", "Card evolution reviews",
            "Challenge wins", "Draft battles"
        ]
    },

    # --- Horror/Indie ---
    "lethal_company": {
        "name": "Lethal Company",
        "genre": "Horreur / Co-op",
        "platforms": ["PC"],
        "audience": "16-30 ans",
        "popularity_score": 80,
        "content_formats": [
            "Funny moments", "Monster encounters", "Multiplayer chaos",
            "Tips & strategies", "Mod showcases", "Challenge runs",
            "Lore theories", "Update reviews"
        ],
        "trending_topics": [
            "New mods", "Updates", "Monster guides",
            "Multiplayer moments", "Strategy guides"
        ],
        "best_video_length": "12-20 min",
        "best_upload_times": ["17h-19h", "20h-22h"],
        "hashtags": ["#LethalCompany", "#IndieGames", "#HorrorGaming"],
        "competitors_formats": [
            "Funniest moments", "All monsters explained",
            "Best mods compilation", "Hardest moon challenges"
        ]
    },

    # --- Generiques populaires ---
    "roblox": {
        "name": "Roblox",
        "genre": "Plateforme / Sandbox",
        "platforms": ["PC", "Mobile", "Xbox"],
        "audience": "6-18 ans",
        "popularity_score": 93,
        "content_formats": [
            "Game reviews", "Roleplay", "Obby challenges",
            "Tycoon gameplay", "Horror games", "Trading guides",
            "Funny moments", "Building showcases"
        ],
        "trending_topics": [
            "Trending games", "New updates", "Robux guides",
            "Popular experiences", "Events", "Creator tools"
        ],
        "best_video_length": "10-20 min",
        "best_upload_times": ["14h-16h", "17h-19h"],
        "hashtags": ["#Roblox", "#RobloxGame", "#RobloxFunny"],
        "competitors_formats": [
            "Best Roblox games", "Scary Roblox games at 3AM",
            "Roblox challenges", "Roleplay stories"
        ]
    },
    "among_us": {
        "name": "Among Us",
        "genre": "Social Deduction",
        "platforms": ["PC", "Mobile", "Switch", "PS5", "Xbox"],
        "audience": "10-25 ans",
        "popularity_score": 65,
        "content_formats": [
            "Impostor gameplay", "Funny moments", "Big brain plays",
            "Mod gameplay", "Role reveals", "Custom game modes"
        ],
        "trending_topics": [
            "New roles", "Mods", "Custom maps",
            "Hide and seek mode", "New cosmetics"
        ],
        "best_video_length": "10-18 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#AmongUs", "#Impostor", "#AmongUsFunny"],
        "competitors_formats": [
            "200 IQ plays", "Funniest impostor moments",
            "Mod showcases", "Proximity chat games"
        ]
    },
    "the_finals": {
        "name": "The Finals",
        "genre": "FPS / Destruction",
        "platforms": ["PC", "PS5", "Xbox"],
        "audience": "16-30 ans",
        "popularity_score": 73,
        "content_formats": [
            "Best builds", "Weapon guides", "Funny moments",
            "Ranked gameplay", "Tips & tricks", "Class guides",
            "Destruction montages", "Update reviews"
        ],
        "trending_topics": [
            "Season updates", "Meta builds", "New weapons",
            "Ranked strategies", "Destruction physics"
        ],
        "best_video_length": "10-15 min",
        "best_upload_times": ["16h-18h", "20h-22h"],
        "hashtags": ["#TheFinals", "#TheFinalsGame", "#FPS"],
        "competitors_formats": [
            "Best build guides", "High kill games",
            "Destruction compilations", "Class tier lists"
        ]
    },
    "helldivers_2": {
        "name": "Helldivers 2",
        "genre": "TPS / Co-op",
        "platforms": ["PC", "PS5"],
        "audience": "18-35 ans",
        "popularity_score": 83,
        "content_formats": [
            "Best loadouts", "Difficulty 9 gameplay", "Funny moments",
            "Stratagem guides", "Co-op highlights", "Tips & tricks",
            "Update reviews", "Community events"
        ],
        "trending_topics": [
            "Balance patches", "New stratagems", "Community wars",
            "Galactic events", "New enemies", "Warbonds"
        ],
        "best_video_length": "12-20 min",
        "best_upload_times": ["15h-17h", "19h-21h"],
        "hashtags": ["#Helldivers2", "#Helldivers", "#ForDemocracy"],
        "competitors_formats": [
            "Best loadout guides", "Solo Helldive difficulty",
            "Funniest moments", "All stratagems ranked"
        ]
    },
}


VIDEO_FORMATS_DATABASE = {
    "top_list": {
        "name": "Top / Classement",
        "description": "Top 5, Top 10, Tier Lists - format tres populaire",
        "avg_retention": "65-75%",
        "difficulty": "Facile",
        "example_titles": [
            "TOP 10 des {game} les plus {adjective} !",
            "TIER LIST {game} Saison {X} - Le MEILLEUR classement",
            "Les 5 MEILLEURS {items} dans {game} en {year}"
        ]
    },
    "tutorial": {
        "name": "Tutoriel / Guide",
        "description": "Guides detailles, comment faire, astuces",
        "avg_retention": "55-65%",
        "difficulty": "Moyen",
        "example_titles": [
            "COMMENT devenir PRO sur {game} - Guide COMPLET",
            "Les ASTUCES que PERSONNE ne connait sur {game}",
            "{game} : Le guide ULTIME pour debutants en {year}"
        ]
    },
    "funny_moments": {
        "name": "Moments Droles",
        "description": "Compilations de moments droles, fails, WTF",
        "avg_retention": "70-80%",
        "difficulty": "Facile",
        "example_titles": [
            "LES MOMENTS LES PLUS DROLES sur {game} !",
            "{game} FAILS & FUNNY MOMENTS #{number}",
            "ON A CASSE LE JEU ! {game} moments WTF"
        ]
    },
    "challenge": {
        "name": "Challenge / Defi",
        "description": "Defis uniques, handicaps, paris",
        "avg_retention": "68-78%",
        "difficulty": "Moyen",
        "example_titles": [
            "JE JOUE {game} AVEC {handicap} !",
            "DEFI IMPOSSIBLE sur {game} - Ca tourne MAL",
            "1 KILL = 1 {action} sur {game}"
        ]
    },
    "story_lore": {
        "name": "Histoire / Lore",
        "description": "Analyses de lore, theories, explications d'histoire",
        "avg_retention": "60-70%",
        "difficulty": "Difficile",
        "example_titles": [
            "L'HISTOIRE CACHEE de {game} expliquee",
            "La THEORIE qui change TOUT dans {game}",
            "{game} : Les SECRETS que vous avez RATES"
        ]
    },
    "versus": {
        "name": "Versus / Comparaison",
        "description": "Comparaisons entre jeux, items, personnages",
        "avg_retention": "62-72%",
        "difficulty": "Facile",
        "example_titles": [
            "{item1} vs {item2} - QUEL EST LE MEILLEUR ?",
            "{game1} vs {game2} en {year} - COMPARAISON HONNETE",
            "DEBUTANT vs PRO sur {game}"
        ]
    },
    "first_look": {
        "name": "Decouverte / First Look",
        "description": "Premier regard sur un jeu ou une mise a jour",
        "avg_retention": "55-65%",
        "difficulty": "Facile",
        "example_titles": [
            "JE DECOUVRE {game} et c'est INCROYABLE !",
            "{game} NOUVELLE MISE A JOUR - Premier Regard",
            "CE NOUVEAU JEU va TOUT CHANGER !"
        ]
    },
    "speedrun": {
        "name": "Speedrun / Record",
        "description": "Tentatives de speedrun, records, performances extremes",
        "avg_retention": "72-82%",
        "difficulty": "Difficile",
        "example_titles": [
            "JE SPEEDRUN {game} en {time} !",
            "RECORD DU MONDE {game} - Speedrun explique",
            "{game} en {time} - C'est POSSIBLE ?"
        ]
    },
    "reaction": {
        "name": "Reaction / Review",
        "description": "Reactions aux trailers, updates, news gaming",
        "avg_retention": "58-68%",
        "difficulty": "Facile",
        "example_titles": [
            "MA REACTION au TRAILER de {game} !",
            "{game} UPDATE {version} - MON AVIS HONNETE",
            "LES NEWS GAMING de la SEMAINE - Reaction"
        ]
    },
    "hardcore_series": {
        "name": "Serie Hardcore",
        "description": "Series longues avec progression, perma-death, objectifs",
        "avg_retention": "75-85%",
        "difficulty": "Difficile",
        "example_titles": [
            "100 JOURS en HARDCORE sur {game}",
            "{game} PERMADEATH - Episode {number}",
            "JE SURVIS {X} JOURS dans {game}"
        ]
    }
}


TRENDING_GAMING_TOPICS = [
    "Nouvelles sorties de jeux AAA",
    "Mises a jour de saison (Fortnite, Apex, Valorant)",
    "Evenements esports majeurs",
    "Jeux indie viraux",
    "Controverses gaming",
    "Announcements hardware (PS5 Pro, Switch 2, GPU)",
    "Gaming AI et nouvelles technologies",
    "Nostalgie retro gaming",
    "Speedrun achievements",
    "Crossover events entre jeux",
    "Free-to-play nouveaux",
    "Mods viraux",
    "Jeux de survie co-op",
    "Game Pass / PS Plus ajouts",
    "Gaming mobile evolution"
]
