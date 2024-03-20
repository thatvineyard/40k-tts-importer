from wahapedia import FACTIONS, Datasheet


ADMECH_DATASHEETS_BLACKSTONE_CAMPAIGN: list[Datasheet] = [
    Datasheet(
        FACTIONS.ADMECH,
        "Tech-priest Manipulus",
        "Tech-priest-Manipulus",
        nickname="The Custodian",
        notes='Leading Conservatives\\n - Unit gives -1 OC 3\\" aura, 1CP regain on 5+',
        weapon_amounts={
            "Magnarail lance": 1,
            "Transonic cannon": 0,
        },
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Technoarcheologist",
        "Technoarcheologist",
        nickname="Archibaldus",
        notes="Leading Royal Guard\\nArtisan (When in aquisition objective: change hit, wound or saving throw to unmodified 6)",
        weapon_amounts={"Mechanicus pistol": 1, "Servo-arc claw": 1},
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Skitarii Rangers",
        "Skitarii-Rangers",
        nickname="Prospectors",
        weapon_amounts={
            "Mechanicus pistol": 1,
            "Arc rifle": 1,
            "Galvanic rifle": 6,
            "Plasma caliver": 1,
            "Transuranic arquebus": 1,
            "Alpha combat weapon": 1,
            "Close combat weapon": 9,
        },
        wargear_amounts={
            "Enhanced data-tether": 1,
            "Omnispex": 0,
        },
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Skitarii Vanguard",
        "Skitarii-Vanguard",
        nickname="Conservatives",
        notes="Bodyguarding The Custodian\\n - Leader gives lethal hits",
        weapon_amounts={
            "Mechanicus pistol": 1,
            "Arc rifle": 1,
            "Radium carbine": 6,
            "Plasma caliver": 1,
            "Transuranic arquebus": 1,
            "Alpha combat weapon": 1,
            "Close combat weapon": 9,
        },
        wargear_amounts={
            "Enhanced data-tether": 1,
            "Omnispex": 0,
        },
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Skitarii Vanguard",
        "Skitarii-Vanguard",
        nickname="Royal Guard",
        notes="Bodyguarding Archibaldus",
        weapon_amounts={
            "Mechanicus pistol": 1,
            "Arc rifle": 1,
            "Radium carbine": 6,
            "Plasma caliver": 1,
            "Transuranic arquebus": 1,
            "Alpha combat weapon": 1,
            "Close combat weapon": 9,
        },
        wargear_amounts={
            "Enhanced data-tether": 1,
            "Omnispex": 0,
        },
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Serberys Raiders",
        "Serberys-Raiders",
        nickname="Skitteriskits",
        weapon_amounts={
            "Mechanicus pistol": 1,
            "Galvanic carbine": 3,
            "Cavalry sabre": 3,
        },
        wargear_amounts={
            "Enhanced data-tether": 1,            
        }
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Sicarian Ruststalkers",
        "Sicarian-Ruststalkers",
        nickname="Absolute Mad Lads",
        weapon_amounts={
            "Transonic blades": 4,
            "Transonic blades and chordclaw": 1,
            "Transonic razor and chordclaw": 0,
        },
    ),
]

ADMECH_DATASHEETS: list[Datasheet] = [
    Datasheet(FACTIONS.ADMECH, "Belisarius Cawl", "Belisarius-Cawl"),
    Datasheet(FACTIONS.ADMECH, "Cybernetica Datasmith", "Cybernetica-Datasmith"),
    Datasheet(FACTIONS.ADMECH, "Skitarii Marshal", "Skitarii-Marshal"),
    Datasheet(FACTIONS.ADMECH, "Sydonian Skatros", "Sydonian-Skatros"),
    Datasheet(FACTIONS.ADMECH, "Tech-priest Dominus", "Tech-priest-Dominus"),
    Datasheet(FACTIONS.ADMECH, "Tech-priest Enginseer", "Tech-priest-Enginseer"),
    Datasheet(FACTIONS.ADMECH, "Tech-priest Manipulus", "Tech-priest-Manipulus"),
    Datasheet(FACTIONS.ADMECH, "Technoarcheologist", "Technoarcheologist"),
    Datasheet(FACTIONS.ADMECH, "Skitarii Rangers", "Skitarii-Rangers"),
    Datasheet(FACTIONS.ADMECH, "Skitarii Vanguard", "Skitarii-Vanguard"),
    Datasheet(FACTIONS.ADMECH, "Skorpius Dunerider", "Skorpius-Dunerider"),
    Datasheet(FACTIONS.ADMECH, "Archaeopter Fusilave", "Archaeopter-Fusilave"),
    Datasheet(FACTIONS.ADMECH, "Archaeopter Stratoraptor", "Archaeopter-Stratoraptor"),
    Datasheet(FACTIONS.ADMECH, "Archaeopter Transvector", "Archaeopter-Transvector"),
    Datasheet(
        FACTIONS.ADMECH, "Corpuscarii Electro-priests", "Corpuscarii-Electro-priests"
    ),
    Datasheet(
        FACTIONS.ADMECH, "Fulgurite Electro-priests", "Fulgurite-Electro-priests"
    ),
    Datasheet(FACTIONS.ADMECH, "Ironstrider Ballistarii", "Ironstrider-Ballistarii"),
    Datasheet(FACTIONS.ADMECH, "Kastelan Robots", "Kastelan-Robots"),
    Datasheet(FACTIONS.ADMECH, "Kataphron Breachers", "Kataphron-Breachers"),
    Datasheet(FACTIONS.ADMECH, "Kataphron Destroyers", "Kataphron-Destroyers"),
    Datasheet(FACTIONS.ADMECH, "Onager Dunecrawler", "Onager-Dunecrawler"),
    Datasheet(FACTIONS.ADMECH, "Pteraxii Skystalkers", "Pteraxii-Skystalkers"),
    Datasheet(FACTIONS.ADMECH, "Pteraxii Sterylizors", "Pteraxii-Sterylizors"),
    Datasheet(FACTIONS.ADMECH, "Serberys Raiders", "Serberys-Raiders"),
    Datasheet(FACTIONS.ADMECH, "Serberys Sulphurhounds", "Serberys-Sulphurhounds"),
    Datasheet(FACTIONS.ADMECH, "Sicarian Infiltrators", "Sicarian-Infiltrators"),
    Datasheet(FACTIONS.ADMECH, "Sicarian Ruststalkers", "Sicarian-Ruststalkers"),
    Datasheet(FACTIONS.ADMECH, "Skorpius Disintegrator", "Skorpius-Disintegrator"),
    Datasheet(
        FACTIONS.ADMECH,
        "Sydonian Dragoons With Radium Jezzails",
        "Sydonian-Dragoons-With-Radium-Jezzails",
    ),
    Datasheet(
        FACTIONS.ADMECH,
        "Sydonian Dragoons With Taser Lances",
        "Sydonian-Dragoons-With-Taser-Lances",
    ),
]

NECRON_DATASHEETS_BLACKSTONE_CAMPAIGN = [
    Datasheet(
        FACTIONS.NECRON,
        "Overlord with Translocation Shroud",
        "Overlord-with-translocation-shroud",
    ),
    Datasheet(
        FACTIONS.NECRON,
        "Plasmancer",
        "Plasmancer",
    ),
    Datasheet(
        FACTIONS.NECRON,
        "Immortals",
        "Immortals",
        weapon_amounts={
            "Gauss blaster": 1,
            "Tesla carbine": 0,
        }
    ),
    Datasheet(
        FACTIONS.NECRON,
        "Necron Warriors",
        "Necron-Warriors",
        weapon_amounts={
            "Gauss flayer": 1,
            "Gauss reaper": 0,
        }
    ),
    Datasheet(
        FACTIONS.NECRON,
        "Flayed Ones",
        "Flayed-Ones",
    ),
    Datasheet(
        FACTIONS.NECRON,
        "Canoptek Scarab Swarms",
        "Canoptek-Scarab-Swarms",
    )
]