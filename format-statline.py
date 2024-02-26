from typing import Any
from xml.etree import ElementTree

SCHEMA_NAMESPACE = "{http://www.battlescribe.net/schema/catalogueSchema}"

namespaces = {
  "": "http://www.battlescribe.net/schema/catalogueSchema"
}

tree = ElementTree.parse("Imperium - Adeptus Mechanicus.cat")
root = tree.getroot()

models_to_pick = [
  "Ironstrider Ballistarii",
  "Cybernetica Datasmith",
  "Onager Dunecrawler",
  "Pteraxii Sterylizors",
  "Serberys Raiders",
  "Sicarian Ruststalkers",
  "Marshal",
  "Rangers",
  "Kastelan Robots"
]

abilities_to_include_description = [
  "Invulnerable Save"
]

def format_ability(ability_profile: ElementTree.Element | Any):
  result = ability_profile.get("name")
  
  if ability_profile.get("name") in abilities_to_include_description:
    result += f" [b]{ability_profile.find("./characteristics/characteristic", namespaces).text}[/b]"
    
  return f"[u]{result}[/u]"


for model in root.findall("./sharedSelectionEntries/selectionEntry", namespaces):
  if model.get("name") in models_to_pick:
    print(f"== {model.get("name")} ==")
    
    
    profiles = model.findall("./profiles/profile", namespaces)
    
    # statline
    try:
      statline_profile = next(profile for profile in profiles if profile.get("typeName") == "Unit")
      statline = statline_profile.findall("./characteristics/characteristic", namespaces)
      
      statline_strings = map(lambda stat: f"{stat.get("name")}[[b]{stat.text}[/b]]", statline)
      print(" ".join(statline_strings))
    except StopIteration:
      print("Could not find statline profile for this model")
      pass
    
    # abilities
    try:
      abilities_profiles = list(profile for profile in profiles if profile.get("typeName") == "Abilities")
      abilities_strings = map(format_ability, abilities_profiles)
      print("")
      print(" ● ".join(abilities_strings))
    except StopIteration:
      print("Could not find statline profile for this model")
      pass
    
    
    
    # categories
    category_links = model.findall("./categoryLinks/categoryLink", namespaces)
    try:
      category_profiles = filter(lambda x: x.get("primary") == "true", category_links)
      category_strings = map(lambda category_profile: category_profile.get("name"), category_profiles)
      print("")
      print(" ◆ ".join(category_strings))
      category_profiles = filter(lambda x: x.get("primary") != "true", category_links)
      category_strings = map(lambda category_profile: category_profile.get("name"), category_profiles)
      print(" ◆ ".join(category_strings))
    except StopIteration:
      print("Could not find statline profile for this model")
      pass
  
    print()
  
    