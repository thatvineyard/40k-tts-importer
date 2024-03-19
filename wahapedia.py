from enum import Enum, auto

BASE_URL = "https://wahapedia.ru/wh40k10ed"
CONTEXTPATH_FACTIONS = "factions"

# FACTIONS


class FACTIONS(Enum):
    ADMECH = auto()
    NECRON = auto()

FACTION_PATHS: dict[FACTIONS, str] = {
    FACTIONS.ADMECH: "adeptus-mechanicus",
    FACTIONS.NECRON: "necrons",
}

# DATASHEETS


class Datasheet:

    def __init__(self, faction: FACTIONS, name: str, path: str) -> None:
        self.faction = faction
        self.name = name
        self.path = path

class ADMECH_DETACHMENTS(Enum):
    RADZONE_CORPS = auto()
    SKITARII_HUNTER_COHORT = auto()
    DATAPSALM_CONCLAVE = auto()
    EXPLORATOR_MANIPLE = auto()
    COHORT_CYBERNETICA = auto()

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
    Datasheet(FACTIONS.ADMECH, "Fulgurite Electro-priests", "Fulgurite-Electro-priests"),
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

def generate_url(datasheet: Datasheet):
    return f'{BASE_URL}/{CONTEXTPATH_FACTIONS}/{FACTION_PATHS[datasheet.faction]}/{datasheet.path}'