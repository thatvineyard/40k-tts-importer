import json
import inquirer

def split_objects_by_value(objects, value_getter, search_keys):
    # Initialize a dictionary to hold the lists of objects for each search key
    sorted_objects = {search_key: [] for search_key in search_keys}

    # Iterate through each object in the input list
    for obj in objects:
      # Get the value associated with the specified key for the current object
      key_value = value_getter(obj)
      
      # If the key value is in our list of search keys, append the object to the corresponding list
      if key_value in search_keys:
          sorted_objects[key_value].append(obj)

    return sorted_objects


def split_objects_by_key_value(objects, key_name, search_keys):
    return split_objects_by_value(objects, lambda x: x.get(key_name), search_keys)

# Function to read and process the JSON file
def process_skitarii_json(file_path):
    # Open and read the JSON file
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    try:
        roster = data['roster']
        force = roster['forces'][0]
        selections = force['selections']
 
        return split_objects_by_key_value(selections, "type", ["upgrade", "model", "unit"])
    except (KeyError, IndexError) as e:
        print(f"Error navigating JSON structure: {e}")
        return None
      
def get_typename_from_object_with_profiles(object):
  try:
    return object["profiles"][0]["typeName"]
  except KeyError:
    return ""
    

def format_statline(profile):
  try:
    characteristics = profile["characteristics"]
  except KeyError:
    print(f"Error reading characteristics for {profile["name"]}")
    return ""
  characteristics_strings = map(lambda characteristic: f"[sup]{characteristic["name"]}[/sup][b]{characteristic["$text"]}[/b]", characteristics)
  characteristics_string = " ∘ ".join(characteristics_strings)
  
  characteristics_string = characteristics_string.replace("\"", "″")
  
  return f"{characteristics_string}"

def format_weapon(weapon_selection):
  name = weapon_selection["name"]
  characteristics = weapon_selection["profiles"][0]["characteristics"]
  
  characteristics_strings = []
  for characteristic in characteristics:
    if characteristic["$text"] == "-":
      continue
    
    if characteristic["name"] in ("Keywords"):
      characteristics_strings.append(f"\\n⁎ {characteristic["$text"]}")
      continue
    
    if characteristic["name"] in ("Range"):
      characteristics_strings.append(f"{characteristic["$text"]}")
      continue
      
    characteristics_strings.append(f"[sup]{characteristic["name"]}[/sup][b]{characteristic["$text"]}[/b]")
  
  characteristics_string = " ∘ ".join(characteristics_strings)
  
  characteristics_string = characteristics_string.replace("\"", "″")
  
  return f"[u]{name}[/u]\\n{characteristics_string}"

abilities_to_include_description = [
  "Invulnerable Save"
]

def format_ability(ability_selection):
  
  result = ability_selection["name"]
  if ability_selection["name"] in abilities_to_include_description: 
    result += f" {ability_selection["characteristics"][0]["$text"]}"
    
  return f"{result}"

def print_model_wargear(model):
  upgrades = split_objects_by_key_value(model["selections"], "type", ["upgrade"])["upgrade"]
  upgrades_by_type = split_objects_by_value(upgrades, get_typename_from_object_with_profiles, ["Abilities", "Ranged Weapons", "Melee Weapons"])
  abilities, ranged_weapons, melee_weapons = upgrades_by_type["Abilities"], upgrades_by_type["Ranged Weapons"], upgrades_by_type["Melee Weapons"]
  
  for weapon in map(format_weapon, ranged_weapons):
    print(f"⁘ {weapon}", end="\\n")
  for weapon in map(format_weapon, melee_weapons):
    print(f"⁝ {weapon}", end="\\n")
  for ability in map(format_ability, abilities):
    print(f"※ {ability}", end="\\n")

def print_statline(unit):
  model_profiles = split_objects_by_value(unit["profiles"], lambda x: x["typeName"], ["Unit", "Abilities"])
  unit, model_abilities = model_profiles["Unit"], model_profiles["Abilities"] 
  
  print(f"{"\n".join(map(lambda x: format_statline(x), unit))}", end="\\n")
  for ability in map(format_ability, model_abilities):
    print(f"⁂ {ability}", end="\\n")
  
def print_model_categories(model):
  print(f"[i]{" ● ".join(map(lambda x: x["name"], model["categories"]))}[/i]")
  
def print_unit(unit):
  for model in unit["selections"]:
    print(f"--- {model["name"]} ---")
    print_statline(unit)
    print(end="\\n")
    print_model_wargear(model)
    print(end="\\n")
    print_model_categories(unit)

def print_model(model):
  print(f"--- {model["name"]} ---", end="\\n")
  print_statline(model)
  print_model_wargear(model)
  print_model_categories(model)
  
def print_stats(unit_or_model):
  match unit_or_model["type"]:
    case "unit":
      print_unit(unit_or_model)
    case "model":
      print_model(unit_or_model)


file_path = "Skitarii.json"
processed_values = process_skitarii_json(file_path)
upgrades, models, units = processed_values['upgrade'], processed_values['model'], processed_values['unit']

print("Upgrades:", len(upgrades))
print("Models:", len(models))
print("Units:", len(units))

all_units = {obj['name']: obj for obj in units + models if 'name' in obj}
answers = inquirer.prompt([inquirer.List("unit", "Which unit do you want to see?", all_units)])


print_stats(all_units[answers["unit"]])
