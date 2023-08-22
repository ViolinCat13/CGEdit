""" CGEdit is a python program to easily edit your ClanGen saves. """

import json
import os

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

os.system("cls")

# C:/Users/NAME/AppData/Local/ClanGen/ClanGen

if not config["use_default_path"]:
    saveLocation = input("Exact file path to your ClanGen saves folder\nC:/Users/NAME/AppData/Local/ClanGen/ClanGen:\n>> ")
else:
    saveLocation = config["default_path"]
if not config["use_current_clan"]:
    clanName = input("Which clan would you like to edit: ").title()
else:
    currentLoc = saveLocation + "/saves/currentclan.txt"
    with open(currentLoc, encoding="utf-8") as f:
        k = f.readlines()
        clanName = k[0]

saves = saveLocation + "/saves"
saveLocation += f"/saves/{clanName}"

clanLocation = saves + f"/{clanName}clan.json"
catsLocation = saveLocation + "/clan_cats.json"
settingsLocation = saves + "/settings.txt"
eventsLocation = saveLocation + "/events.json"
relationsLocation = saveLocation + "/relationships"


with open(catsLocation, encoding="utf-8") as f:
    cats = json.load(f)

with open(eventsLocation, encoding="utf-8") as f:
    events = json.load(f)

def get_cat_names(cats_list: list):
    names = []
    for c in cats_list:
        status = c["status"]
        prefix = c["name_prefix"]
        suffix = c["name_suffix"]
        names.append([prefix, suffix, status])
    return names

def edit_cat(cat: dict, index: int, cats_list: list):
    """ Function to edit cat dict """
    keys = []
    for x, k in enumerate(cat.keys()):
        value = cats_list[index][k]
        ty = type(value)
        keys.append([k, ty])
        print(f"[{x}] - {k}: {value}")
    select = int(input("Enter the number of the item you want to change: "))
    key, ty = keys[select]
    os.system("cls")
    value = input("What value would you like to insert: ")
    if ty == str:
        pass
    elif ty == int:
        cats_list[index][key] = int(value)
    elif ty == list:
        cats_list[index][key] = list(value)

options = ["edit clan", "manual edit", "quick revive", "quick kill", "kill random", "edit relationships", "change settings"]
for x, o in enumerate(options):
    print(f"[{x}] - {o}")
special = int(input("Which option: "))

os.system("cls")
if special == 1: # Manual Edit
    print("---CLAN CATS---")
    for c in get_cat_names(cats):
        status = c[2]
        if c[2] == "leader":
            suffix = "star"
        else:
            suffix = c[1]
        print(c[0].title() + suffix + " - (" + status + ")")
    print("---------------")

    identifier = input("Enter cat's prefix: ").title()

    os.system("cls")

    if identifier.isnumeric():
        for idx, i in enumerate(cats):
            if i["ID"] == int(identifier):
                edit_cat(i, idx, cats)
    else:
        for idx, i in enumerate(cats):
            if i["name_prefix"] == identifier:
                edit_cat(i, idx, cats)

    with open(catsLocation, "r+", encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        json.dump(cats, f, indent=4)
    print("Cat Saved!")
elif special == 2: # Quick Revive
    pass
elif special == 3: # Quick Kill
    pass
elif special == 4: # Kill Random
    pass
elif special == 5: # Edit Relationships
    pass
elif special == 0: # Edit Clan
    pass
elif special == 6: # Edit settings
    with open(settingsLocation, encoding="utf-8") as s:
        settings = {}
        lines = s.readlines()
        for l in lines:
            lineSplit = l.split(":")
            settings.update({lineSplit[0], lineSplit[1]})