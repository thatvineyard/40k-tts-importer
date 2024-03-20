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

    def __init__(
        self,
        faction: FACTIONS,
        name: str,
        path: str,
        nickname: str = "",
        notes: str = "",
        weapon_amounts: dict[str, int] = {},
        wargear_amounts: dict[str, int] = {},
    ) -> None:
        self.faction = faction
        self.name = name
        self.path = path
        self.nickname = nickname
        self.notes = notes
        self.weapon_amounts = weapon_amounts
        self.wargear_amounts = wargear_amounts


class ADMECH_DETACHMENTS(Enum):
    RADZONE_CORPS = auto()
    SKITARII_HUNTER_COHORT = auto()
    DATAPSALM_CONCLAVE = auto()
    EXPLORATOR_MANIPLE = auto()
    COHORT_CYBERNETICA = auto()

def generate_url(datasheet: Datasheet):
    return f"{BASE_URL}/{CONTEXTPATH_FACTIONS}/{FACTION_PATHS[datasheet.faction]}/{datasheet.path}"
