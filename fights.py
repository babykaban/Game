import random
from help_functions import *

"""

This file stores all combat functions, they are used when the player
fights with the enemy, each battle includes four functions 
"loot", "weapon attack", "spell attack" and "evasion". 
Functions vary depending on the enemy.

"""
# ================================================== TROLL =============================================================== #
def loot_troll(troll, parameters, events):
    parameters["action"] = 0
    
    move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
    parameters["screens"]["loot"]["options"][i] = (move_on[0], "shadow_peaks")
    parameters["location_to_move"] = "shadow_peaks"
    
    move_on, i = find_option("shadow_peaks_path", parameters["screens"]["forest"]["options"])
    parameters["screens"]["forest"]["options"][i] = (move_on[0], "shadow_peaks")

    parameters["screens"]["loot"]["text"] += " \\p\n+100 gold \\p\n" \
                                             '+ "Long sword" (25 damage, 100 gold) \\p\n'  \
                                             '+ "Troll hide" (100 gold)'
    
    parameters["inventory"].append({"name": "Long sword", "status": ["equip", "weapon"], "stats":{"type_of_weapon": "sword", "damage": 25}})
    parameters["inventory"].append({"name": "Troll hide", "status": ("tools", "tool")})
    parameters["state"]["gold"] += 100

    parameters["flags"]["fight_troll"] = False 
    parameters["flags"]["troll_in_forest"] = False

    parameters["screen_id"] = "loot"
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

# ================================================== END_TROLL =========================================================== #

# ================================================== WOLVES ============================================================== #
def loot_wolf(enemy, enemes, enemes_counter, parameters, events):
    if len(enemes) == 1:
        enemes_counter = 0

        if check_if_item_in_inventory("Wolven hide", parameters["inventory"]):
            parameters["inventory"][find_item_index_inventory("Wolven hide", parameters["inventory"])]["count"] += 3
        else:
            parameters["inventory"].append({"name": "Wolven hide", "status": ("counted", "hode"), "count": 3})

        events["forest_events"]["numbered_events"]["wolves"] -= 1
        index = find_object_index_array("wolves", events["forest_events"]["events"])
        events["forest_events"]["weights"][index] = events["forest_events"]["numbered_events"]["wolves"] * 3

        parameters["screens"]["loot"]["text"] += ' \\p\n+ 3x "Wolven hide" (15 gold)'
        # You have to reset action to 0 if you changed screen after checking it!!!
        parameters["action"] = 0
        parameters["flags"]["fight_wolves"] = False
        move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
        parameters["screens"]["loot"]["options"][i] = (move_on[0], "forest")
        parameters["location_to_move"] = "forest"
        parameters["screen_id"] = "loot"
    
    return enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events


# ================================================== END_WOLVES ========================================================== #


# ================================================== CREATURE =========================================================== #
def loot_creature(creature, parameters, events):
    random_loot = random.randint(1, 3)
    if random_loot == 1:
        parameters["state"]["gold"] += 10
        parameters["screens"]["loot"]["text"] += " + 10 gold"
    elif random_loot == 2:
        if check_if_item_in_inventory("Heal Potion", parameters["inventory"]):
            parameters["inventory"][find_item_index_inventory("Heal Potion", parameters["inventory"])]["count"] += 1
            parameters["screens"]["loot"]["text"] += "Heal Potion"
        else:
            parameters["inventory"].append({"name": "Heal Potion", "status": "counted", "count": 1})
            parameters["screens"]["loot"]["text"] += "Heal Potion"
    elif random_loot == 3:
        if check_if_item_in_inventory("Mana Potion", parameters["inventory"]):
            parameters["inventory"][find_item_index_inventory("Mana Potion", parameters["inventory"])]["count"] += 1
            parameters["screens"]["loot"]["text"] += "Mana Potion"
        else:
            parameters["inventory"].append({"name": "Mana Potion", "status": "counted", "count": 1})
            parameters["screens"]["loot"]["text"] += "Mana Potion"

    # You have to reset action to 0 if you changed screen after checking it 
    # if you don't want to move to the next screen!!!
    parameters["action"] = 0
    move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
    parameters["screens"]["loot"]["options"][i] = (move_on[0], "swamps")
    parameters["location_to_move"] = "swamps"
    
    creature["number"] -= 1
    if creature["number"] == 0:
        index = find_object_index_array("creature", events["swamp_events"]["events"])
        del events["swamp_events"]["events"][index]
        del events["swamp_events"]["weights"][index]
    
    creature["health"] = 20
    parameters["flags"]["fight_creature"] = False 
    

    parameters["screen_id"] = "loot"
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events
# ================================================== END_CREATURE =========================================================== #


# ===================================================== GOBLIN ============================================================== #
def loot_goblin(goblin, parameters, events):
    
    parameters["inventory"].append({"name": "Golden Locket", "status": "item"})
    parameters["screens"]["loot"]["text"] += ' \\p\n "Golden Locket" (100)'

    # You have to reset action to 0 if you changed screen after checking it 
    # if you don't want to move to the next screen!!!
    parameters["action"] = 0
    move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
    parameters["screens"]["loot"]["options"][i] = (move_on[0], "swamps")
    parameters["location_to_move"] = "swamps"
    
    index = find_object_index_array("goblin", events["swamp_events"]["events"])
    del events["swamp_events"]["events"][index]
    del events["swamp_events"]["weights"][index]

    parameters["flags"]["fight_goblin"] = False
    
    parameters["screen_id"] = "loot"
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

# =================================================== END_GOBLIN ============================================================ #

# ================================================== GUARDS ============================================================= #         
def loot_guard(enemy, enemes, enemes_counter, parameters, events):
    if len(enemes) == 1:
        enemes_counter = 0

        parameters["state"]["gold"] += 10
        # You have to reset action to 0 if you changed screen after checking it!!!
        parameters["action"] = 0
        parameters["flags"]["guards_near_swamps"] = False
        parameters["flags"]["fight_guards"] = False
        move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
        parameters["screens"]["loot"]["options"][i] = (move_on[0], "swamps")
        parameters["location_to_move"] = "swamps"
        parameters["screen_id"] = "loot"
    
    return enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events
# ================================================== END_GUARDS ============================================================= #

# ================================================== BANDITS ============================================================ #

def loot_bandit(enemy, enemes, enemes_counter, parameters, events):
     
    if len(enemes) == 1 or enemy["name"] == "Bandit_Leader":
        enemes_counter = 0
        parameters["state"]["gold"] += 10
        # You have to reset action to 0 if you changed screen after checking it!!!
        parameters["action"] = 0
        parameters["flags"]["bandits_near_tavern"] = False

        tavern_leave, i = find_option("fight_bandits", parameters["screens"]["in_tavern"]["options"])
        parameters["screens"]["in_tavern"]["options"][i] = (tavern_leave[0], "tavern")

        move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
        parameters["screens"]["loot"]["options"][i] = (move_on[0], "tavern")
        parameters["location_to_move"] = "tavern"

        parameters["screen_id"] = "loot"
        if (enemy["name"] == "Bandit_Leader") and len(enemes) > 1:
            parameters["screens"]["loot"]["text"] += " \\p\n You killed the leader so the other bandits escaped"
            parameters["screens"]["tavern"]["text"] = 'You approach "The Drunken Dragon" - a lively gathering place for ' \
                                    'locals and travelers alike, offering ale, food, and tales of ' \
                                    'adventure. '
        else:
            parameters["screens"]["tavern"]["text"] = 'You approach "The Drunken Dragon" - a lively gathering place for ' \
                                    'locals and travelers alike, offering ale, food, and tales of ' \
                                    'adventure. '
   
    return enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events
# ================================================== END_ BANDITS ========================================================= #

# ========================================================= BEAR =================================================== #

def loot_bear(bear, parameters, events):
    
    parameters["action"] = 0
    move_on, i = find_option(parameters["location_to_move"], parameters["screens"]["loot"]["options"])
    parameters["screens"]["loot"]["options"][i] = (move_on[0], "forest")
    parameters["location_to_move"] = "forest"
    
    parameters["inventory"].append({"name": "Bear hide", "status": "item"})
    parameters["screens"]["loot"]["text"] += " \\p\nBear Hide (80 gold)"

    index = find_object_index_array("bear", events["forest_events"]["events"])
    del events["forest_events"]["events"][index]
    del events["forest_events"]["weights"][index]

    parameters["flags"]["fight_bear"] = False 
    

    parameters["screen_id"] = "loot"
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

# ========================================================= END_BEAR ============================================= #

def attack_enemy_weapon(enemy, parameters, events):
    # Find a weapon
    weapon = parameters["inventory"][find_equipped_item_index_inventory(parameters["inventory"])]["stats"]
    # Calculate damage
    damage = enemy["weapon_damage"] * weapon["damage"]
    if weapon["type_of_weapon"] == "sword":
        damage *= enemy["sword_damage"]
    elif weapon["type_of_weapon"] == "axe":
        damage *= enemy["axe_damage"]
    
    # Check if enemy dead and calculate enemy stats
    if roll() > enemy["weapon_miss_chance"]:
        enemy["health"] -= int(round(damage, 0))
        if enemy["health"] <= 0:
            parameters["screens"]["loot"]["text"] = "You have dealt " + str(int(round(damage, 0))) + " damage.  \\p\n" \
                                        + enemy["name"] + " is dead. \\p\n"
            loot_func = enemy["loot"]
            parameters["screen_id"], parameters["action"], parameters["location_to_move"], events = \
                            loot_func(enemy, parameters, events)
        else:
            parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + " damage. " \
                                        + enemy["name"] + " \\p\n"
    else:
        parameters["screens"]["evade"]["text"] = "You have missed. \\p\n"
    
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

def attack_enemy_spell(enemy, spells, parameters, events):
    if parameters["action"] != 0 and \
        parameters["screens"]["spells"]["options"][parameters["action"] - 1][0] == "Back":
            parameters["screen_id"] = "attack"
            parameters["action"] = 0
    else:
        # Find spell and spell mana_cost
        spell = spells[find_spell(parameters["screens"]["spells"]["options"][parameters["action"] - 1][0], spells)]
        mana_cost = spell["stats"]["mana_cost"]

        # Calculating damage
        damage = spell["stats"]["damage"] * enemy["spell_damage"]
        if enemy["vulnerability"] == spell["stats"]["effect"]:
            damage *= enemy["vulnerability_factor"]

        # Check if enemy dead and calculate enemy stats
        if check_mana(mana_cost, parameters["state"]):
            parameters["state"]["mana"] -= mana_cost
            if roll() > enemy["spell_miss_chance"]:
                enemy["health"] -= int(round(damage, 0))
                if enemy["health"] <= 0:
                    parameters["screens"]["loot"]["text"] = "You have dealt " + str(int(round(damage, 0))) + \
                            " damage with "+ spell["name"] + " . \\p\n " + enemy["name"] + " is dead. \\p\n"

                    loot_func = enemy["loot"]
                    parameters["screen_id"], parameters["action"], parameters["location_to_move"], events = \
                        loot_func(enemy, parameters, events)
                else:
                    parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + \
                                                " damage with "+ spell["name"] + " to " + enemy["name"] + " \\p\n"
            else:
                parameters["screens"]["evade"]["text"] = "You have missed."
        else:
            parameters["screen_id"] = "attack"
            parameters["screens"]["attack"]["text"] = "You have not enough mana \\p\n"
            parameters["action"] = 0
    
    return parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

def evade_enemy(enemy, parameters):
    
    enemy_damage = random.randint(enemy["damage"][0], enemy["damage"][1])
    if parameters["action"] == 1:
        if roll() < enemy["evade"]:
            parameters["screens"]["attack"]["text"] = " You have succeed. " + enemy["name"] + " \\p\n"
            parameters["screen_id"] = "attack"
        else:
            parameters["state"]["health"] -= int(round(enemy_damage, 0))
            parameters["screens"]["attack"]["text"] = " You did not succeed. " + enemy["name"] +  " deal "  + \
                                                str(int(round(enemy_damage, 0))) + \
                                                " damage to you " " \\p\n"

    elif parameters["action"] == 2:
        if roll() < enemy["parry"]:
            if enemy["parry_damage"] < 1:
                enemy_damage *= enemy["parry_damage"]
                parameters["state"]["health"] -= int(round(enemy_damage, 0))
                parameters["screens"]["attack"]["text"] = "You block the attack, but " \
                    + enemy["name"] + " delt you " + str(int(round(enemy_damage, 0))) + " damage."
                parameters["screen_id"] = "attack"
            else:
                parameters["screens"]["attack"]["text"] = "You block the attack"
                parameters["screen_id"] = "attack"
        else:
            parameters["state"]["health"] -= int(round(enemy_damage, 0))
            parameters["screens"]["attack"]["text"] = " You try to block but " + enemy["name"] + " deal " + \
                                            str(int(round(enemy_damage, 0))) + " damage to you "  " \\p\n"
    elif parameters["action"] == 3:
        if check_mana(10, parameters["state"]):
            parameters["state"]["mana"] -= 10
            if roll() < enemy["magic_shield"]:
                if enemy["magic_shield_damage"] < 1:
                    enemy_damage *= enemy["magic_shield_damage"]
                    parameters["state"]["health"] -= int(round(enemy_damage, 0))
                    parameters["screens"]["attack"]["text"] = "You block the attack, but " \
                        + enemy["name"] + " delt you " + str(int(round(enemy_damage, 0))) + " damage."
                    parameters["screen_id"] = "attack"
                else:
                    parameters["screens"]["attack"]["text"] = " You blocked the attack" \
                                                                    " with magic shield. "
                    parameters["screen_id"] = "attack"
            else:
                parameters["state"]["health"] -= int(round(enemy_damage, 0))
                parameters["screens"]["attack"]["text"] = " You did not succeed. " + \
                    enemy["name"] + " deal " + str(int(round(enemy_damage, 0))) + " damage to you "  " \\p\n"
        else:
            parameters["screens"]["evade"]["text"] = "You have not enough mana"
            parameters["screen_id"] = "evade"
            parameters["action"] = 0
    return parameters["screen_id"], parameters["action"]


def attack_enemy_in_multiple_fight_weapon(index, enemes, enemes_counter, choose_screen, parameters, events):
    # Set loot function
    if index <= len(enemes):
        loot_func = enemes[index - 1]["loot"] 
        
        # Find a weapon
        weapon = parameters["inventory"][find_equipped_item_index_inventory(parameters["inventory"])]["stats"]
        # Calculate damage
        damage = enemes[index - 1]["weapon_damage"] * weapon["damage"]
        if weapon["type_of_weapon"] == "sword":
            damage *= enemes[index - 1]["sword_damage"]
        elif weapon["type_of_weapon"] == "axe":
            damage *= enemes[index - 1]["axe_damage"]
        
        # Check if enemes[index - 1] dead and calculate enemes[index - 1] stats
        if roll() > enemes[index - 1]["weapon_miss_chance"]:
            enemes[index - 1]["health"] -= int(round(damage, 0))
            if enemes[index - 1]["health"] <= 0:
                parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + " damage.  \\p\n" \
                                            + enemes[index - 1]["name"] + " is dead. \\p\n"
                parameters["screens"]["loot"]["text"] = "You have dealt " + str(int(round(damage, 0))) + " damage.  \\p\n" \
                                            + enemes[index - 1]["name"] + " is dead. \\p\n"
                
                enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events = \
                        loot_func(enemes[index - 1], enemes, enemes_counter, parameters, events)
                del enemes[index - 1]
                del parameters["screens"][choose_screen]["options"][index - 1]
                
            else:
                parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + " damage. " \
                                            + enemes[index - 1]["name"] + " \\p\n"
        else:
            parameters["screens"]["evade"]["text"] = "You have missed. \\p\n"
        
        enemes_counter = len(enemes)
        parameters["screens"][choose_screen]["text"] = ""
        parameters["screens"]["attack"]["text"] = ""
    
    return enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

def attack_enemy_in_multiple_fight_spell(index, enemes, enemes_counter, choose_screen, spells, parameters, events):
  
    if parameters["action"] != 0 and \
        parameters["screens"]["spells"]["options"][parameters["action"] - 1][0] == "Back":
            parameters["screen_id"] = "attack"
            parameters["action"] = 0
    else:  
        if len(enemes) == 1:
            index = 1

        # Set loot function
        loot_func = enemes[index - 1]["loot"]
        
        # Find spell and spell mana_cost
        spell = spells[find_spell(parameters["screens"]["spells"]["options"][parameters["action"] - 1][0], spells)]
        mana_cost = spell["stats"]["mana_cost"]

        # Calculating damage
        damage = spell["stats"]["damage"] * enemes[index - 1]["spell_damage"]
        if enemes[index - 1]["vulnerability"] == spell["stats"]["effect"]:
            damage *= enemes[index - 1]["vulnerability_factor"]

        # Check if enemes[index - 1] dead and calculate enemes[index - 1] stats
        if check_mana(mana_cost, parameters["state"]):
            parameters["state"]["mana"] -= mana_cost
            if roll() > enemes[index - 1]["spell_miss_chance"]:
                enemes[index - 1]["health"] -= int(round(damage, 0))
                if enemes[index - 1]["health"] <= 0:
                    parameters["screens"]["loot"]["text"] = "You have dealt " + str(int(round(damage, 0))) + \
                            " damage with "+ spell["name"] + " . \\p\n " + enemes[index - 1]["name"] + " is dead. \\p\n"
                    parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + \
                            " damage with "+ spell["name"] + " . \\p\n " + enemes[index - 1]["name"] + " is dead. \\p\n"
                    
                    enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events = \
                        loot_func(enemes[index - 1], enemes, enemes_counter, parameters, events)
                    del enemes[index - 1]
                    del parameters["screens"][choose_screen]["options"][index - 1]
                else:
                    parameters["screens"]["evade"]["text"] = "You have dealt " + str(int(round(damage, 0))) + \
                                                " damage with "+ spell["name"] + " to " + enemes[index - 1]["name"] + " \\p\n"
            else:
                parameters["screens"]["evade"]["text"] = "You have missed."
        else:
            parameters["screen_id"] = "attack"
            parameters["action"] = 0
            
        
        
        
        enemes_counter = len(enemes)
        if parameters["state"]["mana"] > 0:
            parameters["screens"][choose_screen]["text"] = ""
            parameters["screens"]["attack"]["text"] = ""
        else:
            parameters["screens"]["attack"]["text"] = "You have not enough mana \\p\n"

    return enemes_counter, parameters["screen_id"], parameters["action"], parameters["location_to_move"], events

def evade_enemes(enemes, enemes_counter, choose_screen, parameters):

    if len(enemes) > 1:
        fight_screen = choose_screen
    else:
        fight_screen = "attack"
    
    enemes_counter -= 1
    
    enemy_damage = random.randint(enemes[enemes_counter - 1]["damage"][0], enemes[enemes_counter - 1]["damage"][1])
    if parameters["action"] == 1:
        if roll() < enemes[enemes_counter - 1]["evade"]:
            parameters["screens"][fight_screen]["text"] += " You have succeed. " + enemes[enemes_counter - 1]["name"] + " \\p\n"
            parameters["screens"]["evade"]["text"] += "You try to evade " + enemes[enemes_counter - 1]["name"] + " \\p\n"
        else:
            parameters["state"]["health"] -= int(round(enemy_damage, 0))
            parameters["screens"][fight_screen]["text"] += " You did not succeed. " + enemes[enemes_counter - 1]["name"] +  " deal "  + \
                                                str(int(round(enemy_damage, 0))) + " damage to you \\p\n"
            parameters["screens"]["evade"]["text"] += "You try to evade " + enemes[enemes_counter - 1]["name"] + " \\p\n"

    elif parameters["action"] == 2:
        if roll() < enemes[enemes_counter - 1]["parry"]:
            if enemes[enemes_counter - 1]["parry_damage"] < 1:
                enemy_damage *= enemes[enemes_counter - 1]["parry_damage"]
                parameters["state"]["health"] -= int(round(enemy_damage, 0)) 
                parameters["screens"][fight_screen]["text"] += "You parry the attack, but " \
                    + enemes[enemes_counter - 1]["name"] + " delt you " + str(int(round(enemy_damage, 0))) + " damage. \\p\n"
                parameters["screens"]["evade"]["text"] += "You try to parry " + enemes[enemes_counter - 1]["name"] + " \\p\n"
            else:
                parameters["screens"]["evade"]["text"] += "You try to parry " + enemes[enemes_counter - 1]["name"] + " \\p\n"
                parameters["screens"][fight_screen]["text"] += "You parry the attack \\p\n"
        else:
            parameters["state"]["health"] -= int(round(enemy_damage, 0))
            parameters["screens"][fight_screen]["text"] += " You try to block but " + enemes[enemes_counter - 1]["name"] + " deal " + \
                                            str(int(round(enemy_damage, 0))) + " damage to you \\p\n"
            parameters["screens"]["evade"]["text"] += "You try to evade " + enemes[enemes_counter - 1]["name"] + " \\p\n"
    
    elif parameters["action"] == 3:
        if check_mana(10, parameters["state"]):
            parameters["state"]["mana"] -= 10
            if roll() < enemes[enemes_counter - 1]["magic_shield"]:
                if enemes[enemes_counter - 1]["magic_shield_damage"] < 1:
                    enemy_damage *= enemes[enemes_counter - 1]["magic_shield_damage"]
                    parameters["state"]["health"] -= int(round(enemy_damage, 0)) 
                    parameters["screens"][fight_screen]["text"] += "You block the attack, but " \
                        + enemes[enemes_counter - 1]["name"] + " delt you " + str(int(round(enemy_damage, 0))) + " damage. \\p\n"
                    parameters["screens"]["evade"]["text"] += "You try to block " + enemes[enemes_counter - 1]["name"] + " \\p\n"
                else:
                    parameters["screens"]["evade"]["text"] += "You try to block " + enemes[enemes_counter - 1]["name"] + " \\p\n"
                    parameters["screens"][fight_screen]["text"] += " You blocked the attack" \
                                                                    " with magic shield.  \\p\n"
            else:
                parameters["state"]["health"] -= int(round(enemy_damage, 0))
                parameters["screens"][fight_screen]["text"] += " You did not succeed. " + \
                    enemes[enemes_counter - 1]["name"] + " deal " + str(int(round(enemy_damage, 0))) + " damage to you "  " \\p\n"
                parameters["screens"]["evade"]["text"] += "You try to block " + enemes[enemes_counter - 1]["name"] + " \\p\n"
        else:
            parameters["screens"]["evade"]["text"] = "You have not enough mana \\p\n"
            enemes_counter += 1
            parameters["action"] = 0
    
    return enemes_counter, parameters["action"]