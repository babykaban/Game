from random import random
from help_functions import *

# In this file stored all "event functions" 

# ============================================= TAVERN_EVENTS ========================================================== #
def in_tavern(flags, screens):
    if not flags["hero_saw_bandits"] and flags["bandits_near_tavern"] and not flags["you_are_drunk"]:
        flags["hero_saw_bandits"] = True
        tavern_leave, i = find_option("tavern", screens["in_tavern"]["options"])
        screens["in_tavern"]["options"][i] = (tavern_leave[0], "fight_bandits")
    
    elif flags["hero_saw_bandits"] and flags["bandits_near_tavern"] and flags["you_are_drunk"]:
        tavern_leave, i = find_option("fight_bandits", screens["in_tavern"]["options"])
        screens["in_tavern"]["options"][i] = (tavern_leave[0], "you_got_drunk")
        flags["bandits_near_tavern"] = False

def innkeeper_lose_10_gold(state, screens):
    state["gold"] -= 10
    del_option("innkeeper_lose_10_gold", screens["innkeeper"]["options"])
    del screens["innkeeper_lose_10_gold"]

def innkeeper_lose_30_gold(state, screens):
    state["gold"] -= 30
    del_option("innkeeper_lose_30_gold", screens["innkeeper"]["options"])
    del screens["innkeeper_lose_30_gold"]

def innkeeper(action, screens, inventory, state):
    if action != 0:
        if screens["innkeeper"]["options"][action - 1][0] == "Buy beer":
            if state["gold"] >= 10:
                if check_if_item_in_inventory("Beer", inventory):
                    inventory[find_item_index_inventory("Beer", inventory)]["count"] += 1
                    state["gold"] -= 10
                else:
                    inventory.append({"name": "Beer", "status": ("counted", "beer"), "count": 1})
                    state["gold"] -= 10

def party(flags, screens):
    if not flags["you_are_drunk"]:
        del screens["party"]
        del_option("party", screens["in_tavern"]["options"])
        flags["you_are_drunk"] = True
        flags["party_in_tavern"] = True

def old_woman(flags, screens):
    del screens["old_woman"]
    del_option("old_woman", screens["in_tavern"]["options"])
    flags["you_know_Jacob"] = True

def you_got_drunk(flags, state, screens):
    if flags["you_are_drunk"]:
        state["gold"] = 0
        state["health"] -= 20
        tavern_leave, i = find_option("you_got_drunk", screens["in_tavern"]["options"])
        screens["in_tavern"]["options"][i] = (tavern_leave[0], "tavern")
        screens["tavern"]["text"] = 'You approach "The Drunken Dragon" - a lively gathering place for ' \
                            'locals and travelers alike, offering ale, food, and tales of ' \
                            'adventure. '
        flags["you_are_drunk"] = False
# ============================================ END_TAVERN_EVENTS ======================================================= #  


# ================================================ SHADOW_PEAKS_EVENTS ================================================== #
def shadow_peaks_path(screens, screen_id, action, state, flags):
    if action != 0 and action <= len(screens["shadow_peaks_path"]["options"]):
        if screens["shadow_peaks_path"]["options"][action - 1][0] == "Pay 500 gold":
            if state["gold"] >= 500:
                state["gold"] -= 500
                flags["troll_in_forest"] = False
                screen_id = "pay_troll"
                action = 0

    return screen_id, action

def negotiate_troll(screens):
    del screens["negotiate_troll"] 
    del_option("negotiate_troll", screens["shadow_peaks_path"]["options"])

def ask_troll(screens):
    del screens["ask_troll"] 
    del_option("ask_troll", screens["shadow_peaks_path"]["options"])

def pay_troll(screens):
    del screens["pay_troll"]
    del screens["shadow_peaks_path"]

    move_on, i = find_option("shadow_peaks_path", screens["forest"]["options"])
    screens["forest"]["options"][i] = (move_on[0], "shadow_peaks")

def troll_golden_locket(screens):
    del screens["troll_golden_locket"]
    del screens["shadow_peaks_path"]

    move_on, i = find_option("shadow_peaks_path", screens["forest"]["options"])
    screens["forest"]["options"][i] = (move_on[0], "shadow_peaks")

def add_inventory_in_troll_offer_screen(screens, inventory):
    for item in inventory:
        if item["status"][0] == "counted":
            screens["offer_troll"]["options"].append((item["name"] + " " + str(item["count"]), "else_items_troll"))
        elif item["status"][0] == "equip":
            screens["offer_troll"]["options"].append((item["name"], "equipment_troll"))
        elif item["name"] == "Golden Locket":
            screens["offer_troll"]["options"].append((item["name"], "troll_golden_locket"))
    screens["offer_troll"]["options"].append(("Cancel", "shadow_peaks_path"))

def offer_troll(screens, inventory, action):
    if len(screens["offer_troll"]["options"]) == 0:
        add_inventory_in_troll_offer_screen(screens, inventory)
    else:
        del_all_options(screens["offer_troll"]["options"])
        add_inventory_in_troll_offer_screen(screens, inventory)

    # NOTE: Since there is a constant option on this screen, 
    # we compare only the action - 1 with len of screens["screen"]["options"] - 1 !!
   
    if action - 1 < len(screens["offer_troll"]["options"]) - 1:
        if inventory[action]["status"][0] == "counted" and action != 0:
            inventory[action]["count"] -= 1
            if inventory[action]["count"] == 0:
                del inventory[action]
            action = 0
        
        elif action != 0:
            if inventory[action]["status"][0] == "equip":
                del inventory[action]
            elif inventory[action]["name"] == "Golden Locket":
                del inventory[action]
            action = 0

def troll_enemy(screens, flags, action):
    if action != 0 and action - 1 < len(screens["fight_troll"]["options"]):
        if action == 1:
            screens["fight"]["text"] = "How do you want to attack ?"
            flags["fight_troll"] = True

# ================================================ END_SHADOW_PEAKS_EVENTS ============================================== #


# ============================================ VILLAGE_EVENTS ================================================================ #
def church(screens, flags, state, action, pay):
    if flags["church_quest_done"]:
        screens["church"]["options"][0][0] = "Rest and heal (10 Gold)"
    if action == 1:
        if state["health"] < 100 or state["mana"] < 100 and state["gold"] >= pay:
            if state["health"] + 30  > 100:
                state["health"] = 100
            else:
                state["health"] += 30
            
            if state["mana"] + 30 > state["max_mana"]:
                state["mana"] = state["max_mana"]
            else:
                state["mana"] += 30
            
            state["gold"] -= pay

def church_jacob(screens):
    del screens["church_jacob"]
    del_option("church_jacob", screens["church"]["options"])

def women_jacob(flags, screens):
    del screens["women_jacob"]
    del_option("women_jacob", screens["women"]["options"])
    flags["you_know_where_jacob_live"] = True

def jacob_home(screens, flags, action):
    if action != 0 and action <= len(screens["jacob_home"]["options"]):
        if screens["jacob_home"]["options"][action - 1][0] == "Knock on the door":
            screens["jacob_home"]["text"] = "You knocked on the door, but there was no answer." \
                                            " Despite this, you could hear someone moving inside the house."
            del screens["jacob_home"]["options"][action - 1]
            action = 0
        elif screens["jacob_home"]["options"][action - 1][0] == "Yell Jacob's name":
            screens["jacob_home"]["text"] = "You try calling out Jacob's name, but there's no response. You start " \
                                            "to wonder if perhaps he's not home, or if he's purposely avoiding " \
                                            "you. "
            del screens["jacob_home"]["options"][action - 1]
            action = 0

        if len(screens["jacob_home"]["options"]) == 0:
            screens["jacob_home"]["options"].append(("Try to open the door", "inside_jacob_house"))
    
    elif flags["conversation_done"] and flags["beer"]:
        del_all_options(screens["jacob_home"]["options"])
        screens["jacob_home"]["text"] = 'As you step out of the abandoned house, you notice a tall man standing near the door, \
                                        who looks as if he was about to enter the house himself. "What are you doing in my house?" \
                                        the man asked, his eyes narrowed suspiciously.'
        screens["jacob_home"]["options"].append(("Ask who he is", "jacob_home"))
        screens["jacob_home"]["options"].append(("Tell that you are looking for The Heart of Elders",
                                                "jacob_home"))
        screens["jacob_home"]["options"].append(("Tell that you are from the city guard, and he is arrested",
                                                "jacob_home"))
        screens["jacob_home"]["options"].append(("Tell if he doesn't do as you say, you're going to kill him",
                                                "jacob_home"))
        flags["conversation_done"] = False
    
    if not flags["conversation_done"] and flags["beer"] and \
    action != 0 and action - 1 < len(screens["jacob_home"]["options"]):
        if screens["jacob_home"]["options"][action - 1][0] == "Ask who he is":
            screens["jacob_home"]["text"] = '"Answer my question first. Why were you in my home?"'
            del screens["jacob_home"]["options"][action - 1]
            action = 0
        elif screens["jacob_home"]["options"][action - 1][0] == "Tell that you are looking for The Heart of Elders":
            screens["jacob_home"]["text"] = '"In my house? Wow, you must be a legendary treasure hunter."'
            del screens["jacob_home"]["options"][action - 1]
            action = 0
        elif screens["jacob_home"]["options"][action - 1][0] == \
                "Tell that you are from the city guard, and he is arrested":
            screens["jacob_home"][
                "text"] = '"If you are going to pretend to be a guard, at least dress accordingly."'
            del screens["jacob_home"]["options"][action - 1]
            action = 0
        elif screens["jacob_home"]["options"][action - 1][0] == \
                "Tell if he doesn't do as you say, you're going to kill him":
            screens["jacob_home"]["text"] = '"... Are you feeling well?"'
            del screens["jacob_home"]["options"][action - 1]
            action = 0
        elif screens["jacob_home"]["options"][action - 1][0] == "Try to explain the situation":
            screens["jacob_home"]["text"] = "You finally are able to explain that someone is  \
                                            living in this home, and you have mistaken that man for Jacob." \
                                            "So, you're saying someone was in my house? Well, I've been away" \
                                            "for 'a' few weeks, so I wouldn't be surprised if someone took advantage of my absence."
            del_all_options(screens["jacob_home"]["options"])
            screens["jacob_home"]["options"].append(("Continue", "jacob_home"))
            action = 0
        
        elif screens["jacob_home"]["options"][action - 1][0] == "Continue" and \
                action - 1 < len(screens["jacob_home"]["options"]):
            screens["jacob_home"]["text"] = 'Jacob pauses for a moment and looks thoughtful. \
                I know the Heart of Elders is hidden in a cave deep in the Shadow Peaks.' \
                                            "Getting there is a dangerous journey, but I've been there before. \
                        I know a shortcut through the swamp, that way we can go around that Troll." \
                                            "If you're willing to take the risk, I can tell you how to get through the" \
                                            "swamp. However I won't join you. I risked my life far too many times in the past."
            del_all_options(screens["jacob_home"]["options"])
            del_option("inside_jacob_house", screens["village"]["options"])
            flags["path_to_shadow_peaks"] = True
            screens["jacob_home"]["options"].append(
                ("*you now know the path from the Stinky Swamps to the Shadow Peaks*", "village"))
            action = 0            

        if len(screens["jacob_home"]["options"]) == 2 and \
                ("Try to explain the situation", "jacob_home") not in screens["jacob_home"]["options"]:
            screens["jacob_home"]["options"].append(("Try to explain the situation", "jacob_home"))

    return action

def inside_jacob_house(screens, flags, inventory, action):
    if action != 0 and action <= len(screens["inside_jacob_house"]["options"]):
        if screens["inside_jacob_house"]["options"][action - 1][0] == "Look around":
            screens["inside_jacob_house"]["text"] = "You find a man fast asleep in his bed, snoring" \
                                                    "softly. The room is dimly lit and quiet except for the sound " \
                                                    "of Jacob's breathing. "
            del screens["inside_jacob_house"]["options"][action - 1]
            screens["inside_jacob_house"]["options"].append(("Wake him up", "inside_jacob_house"))
            action = 0

        elif screens["inside_jacob_house"]["options"][action - 1][0] == "Wake him up":
            screens["inside_jacob_house"][
                "text"] = 'As you shake the man gently, he slowly opens his eyes and blinks a ' \
                        "few times, looking around in confusion before finally focusing on you. " \
                        '"Who are you?" he asks, sounding groggy.'
            del screens["inside_jacob_house"]["options"][action - 1]
            screens["inside_jacob_house"]["options"].append(("Ask who he is", "inside_jacob_house"))
            screens["inside_jacob_house"]["options"].append(("Tell that you are looking for The Heart of Elders",
                                                            "inside_jacob_house"))
            screens["inside_jacob_house"]["options"].append(
                ("Tell that you are from the city guard, and he is arrested",
                "inside_jacob_house"))
            screens["inside_jacob_house"]["options"].append(
                ("Tell if he doesn't do as you say, you're going to kill him",
                "inside_jacob_house"))
            action = 0

        elif screens["inside_jacob_house"]["options"][action - 1][0] == "Ask who he is":
            screens["inside_jacob_house"]["text"] = "Aren't we the curious one? Before I tell you who I am, " \
                                                    "why don't you tell me who you are?"
            del screens["inside_jacob_house"]["options"][action - 1]
            action = 0
        elif screens["inside_jacob_house"]["options"][action - 1][
            0] == "Tell that you are looking for The Heart of Elders":
            screens["inside_jacob_house"]["text"] = "The Heart of Elders? I've never heard of it."
            del screens["inside_jacob_house"]["options"][action - 1]
            action = 0
        elif screens["inside_jacob_house"]["options"][action - 1][0] == \
                "Tell that you are from the city guard, and he is arrested":
            screens["inside_jacob_house"]["text"] = "Ha! Arrested? What for? I haven't done anything wrong lately."
            del screens["inside_jacob_house"]["options"][action - 1]
            action = 0
        elif screens["inside_jacob_house"]["options"][action - 1][0] == \
                "Tell if he doesn't do as you say, you're going to kill him":
            screens["inside_jacob_house"]["text"] = "He laughs in your face: " \
                                                    '"'"I've faced death many times before,"' \
                                                        " he says. "Go ahead, do it if you"'"ve got the guts.'"
            del screens["inside_jacob_house"]["options"][action - 1]
            action = 0

        if len(screens["inside_jacob_house"]["options"]) == 0:
            screens["inside_jacob_house"]["text"] = '"Look, I"'"m getting tired of this conversation. Be on your " \
                                                    "way.'I wouldn't say no to a drink though if you decide to " \
                                                    "visit again. *beer* "
            del_option("jacob_home", screens["village"]["options"])
            screens["village"]["options"].append(("Go to Jacob's place", "inside_jacob_house"))
            del_all_options(screens["inside_jacob_house"]["options"])
            screens["inside_jacob_house"]["options"].append(("Leave", "village"))
            flags["conversation_done"] = True

    elif check_if_item_in_inventory("Beer", inventory) and not flags["beer"] and \
            flags["conversation_done"]:
        screens["inside_jacob_house"]["options"].append(("Offer man a drink.", "inside_jacob_house"))
        flags["beer"] = True
        flags["converstion_done"] = False

    if flags["beer"] and not check_if_item_in_inventory("Beer", inventory) and \
            len(screens["inside_jacob_house"]["options"]) > 1:
        del_option("inside_jacob_house", screens["inside_jacob_house"]["options"])

    elif flags["beer"] and action != 0 and action - 1 < len(screens["inside_jacob_house"]["options"]):
        if screens["inside_jacob_house"]["options"][action - 1][0] == "Offer man a drink.":
            inventory[find_item_index_inventory("Beer", inventory)]["count"] -= 1
            if inventory[find_item_index_inventory("Beer", inventory)]["count"] == 0:
                del inventory[find_item_index_inventory("Beer", inventory)]
            screens["inside_jacob_house"]["text"] = 'He takes it gratefully and raises it to his lips. He takes a sip.  \
                                        "Ah, this is just what I needed," he says with a smile. "I"'"ve been living \
                                        in this abandoned home for a while now, just trying to get by. It's nice  \
                                        to have some company for a change." \
                                                    "The man then proceeds to tell you more about himself and  \
                                        "'his life, but as he talks, it becomes clear that he is not Jacob.'
            del_option("inside_jacob_house", screens["inside_jacob_house"]["options"])
            del_option("village", screens["inside_jacob_house"]["options"])
            screens["inside_jacob_house"]["options"].append(("Leave", "jacob_home"))
            action = 0

    return action

def church_quest(screens, flags, inventory, action, pay_for_rest):
    if  not flags["church_quest"] and not flags["church_quest_done"]:
        if check_if_item_in_inventory("Herbs", inventory):
            if inventory[find_item_index_inventory("Herbs", inventory)]["count"] >= 3:
                screens["church_quest"]["options"].append(("Give herbs to the monk", "church_quest"))
                flags["church_quest"] = True

    elif action != 0 and find_item_index_inventory("Herbs", inventory) \
        and not flags["church_quest_done"]:
        if screens["church_quest"]["options"][action - 1][0] == "Give herbs to the monk" \
                and inventory[find_item_index_inventory("Herbs", inventory)]["count"] >= 3:
            del_all_options(screens["church_quest"]["options"])
            screens["church_quest"]["text"] = '"You have done us a great service! ' \
                                            "Don't hesitate to come back if you " \
                                            'ever need a place to rest or heal." '
            screens["church_quest"]["options"].append(("*you can rest twice as cheaply*", "church"))
            del_option("church_quest", screens["church"]["options"])
            inventory[find_item_index_inventory("Herbs", inventory)]["count"] -= 3
            if inventory[find_item_index_inventory("Herbs", inventory)]["count"] == 0:
                del inventory[find_item_index_inventory("Herbs", inventory)]
            pay_for_rest /= 2
            flags["church_quest_done"] = True
    return pay_for_rest

def sad_man(parameters): 
    if check_if_item_in_inventory("Golden Locket", parameters["inventory"]) and \
        not check_if_option_in_screen("sad_man_bless", parameters["screens"]["sad_man"]["options"]):
        parameters["screens"]["sad_man"]["options"].append(("Give Golden Locket", "sad_man_bless"))
    elif not check_if_item_in_inventory("Golden Locket", parameters["inventory"]) and \
        check_if_option_in_screen("sad_man_bless", parameters["screens"]["sad_man"]["options"]):
        del_option("sad_man_bless", parameters["screens"]["sad_man"]["options"])

    # if parameters["action"] == 2:
    #     del parameters["inventory"][find_item_index_inventory("Golden Locket", parameters["inventory"])]
    #     parameters["screen_id"] = "sad_man_bless"
    #     parameters["action"] = 0
    
    return parameters["screen_id"], parameters["action"]

def man_jacob(screens):
    del screens["man_jacob"]
    del_option("man_jacob", screens["sad_man"]["options"])

def village(screens):
    if len(screens["move"]["options"]) == 0:
        screens["move"]["options"].append(("Go to the Gorn's Shop", "store"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Whispering Woods", ""))
    else:
        del_all_options(screens["move"]["options"])
        screens["move"]["options"].append(("Go to the Gorn's Shop", "store"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Whispering Woods", "forest"))

# ============================================ END_VILLAGE_EVENTS ================================================================ #

# ============================================== STORE_EVENTS ================================================================== #
def find_item_idex_store(key, store):
    count = 0
    for item in store:
        if item["name"] == key:
            break
        count += 1
    return count

def add_store_buy_in_screen(screens, store):
    for item in store:
        text = item["name"] + " (" + str(item["price"]) + ")"
        screens["buy"]["options"].append((text, "buy"))


def add_store_sell_in_screen(screens, inventory):
    for item in inventory:
        if item["status"][0] == "counted":
            screens["sell"]["options"].append((item["name"], "sell"))
        else:
            if item["status"][0] == "equip" or item["status"][0] == "item":
                screens["sell"]["options"].append((item["name"], "sell"))


def processingStoreEvents(screen_id, screens, state, inventory, spells, store, items_sell_prices, index):
    if(len(screens["buy"]["options"]) != 0 and len(screens["buy"]["options"]) > index and screen_id == "buy"):
        if screens["buy"]["options"][index][0] in screens["buy"]["options"][index]: 
            item = store[index]
            
            if item["type"][0] == "counted":
                if state["gold"] >= item["price"] and check_if_item_in_inventory(item["name"], inventory):
                    inventory[find_item_index_inventory(item["name"], inventory)]["count"] += 1
                    state["gold"] -= item["price"]
                elif state["gold"] >= item["price"] and not check_if_item_in_inventory(item["name"], inventory):
                    inventory.append({"name": item["name"], "status": item["type"], "count": 1})
                    state["gold"] -= item["price"]

            elif item["type"][0] == "tools":
                if state["gold"] >= item["price"]:
                    inventory.append({"name": item["name"], "status": item["type"]})
                    del store[find_item_idex_store(item["name"], store)]
                    action = 0
                    state["gold"] -= item["price"]

            elif item["type"][0] == "weapon":
                if state["gold"] >= item["price"]:
                    inventory.append({"name": item["name"], "status": ["equip", "weapon"], 
                                        "stats": {"type_of_weapon": item["stats"]["type"], "damage": item["stats"]["damage"]}})
                    del store[find_item_idex_store(item["name"], store)]
                    action = 0
                    state["gold"] -= item["price"]

            elif item["type"][0] == "spell":
                if state["gold"] >= item["price"]:
                    spells.append({"name": item["name"], "stats": {"effect": item["stats"]["effect"], 
                                                "damage": item["stats"]["damage"], 
                                                "mana_cost": item["stats"]["mana_cost"]}})
                    del store[find_item_idex_store(item["name"], store)]
                    action = 0
                    state["gold"] -= item["price"]
            
            elif item["type"][0] == "armor":
                if state["gold"] >= item["price"]:
                    inventory.append({"name": item["name"], "status": item["type"], "stats": item["stats"]})
                    del store[find_item_idex_store(item["name"], store)]
                    action = 0
                    state["gold"] -= item["price"]
    
    elif(len(screens["sell"]["options"]) != 0 and len(screens["sell"]["options"]) > index and screen_id == "sell"):
        if screens["sell"]["options"][index][0] in screens["sell"]["options"][index]:
            
            item_index = find_item_index_inventory(screens["sell"]["options"][index][0], inventory)
            sell_price = items_sell_prices[find_index_in_sell_prices(inventory[item_index]["name"], items_sell_prices)]["sell_price"]

            if inventory[item_index]["status"][0] == "counted":
                inventory[item_index]["count"] -= 1
                if inventory[item_index]["count"] == 0:
                    del inventory[item_index]
                state["gold"] += sell_price
            
            elif inventory[item_index]["status"][0] == "equip":
                del inventory[item_index]
                state["gold"] += sell_price
            
            elif inventory[item_index]["status"][0] == "item":
                del inventory[item_index]
                state["gold"] += sell_price
                    

def buy_and_sell(screen_id, screens, state, inventory, spells, store, items_sell_prices, action):
    if screen_id == "buy":
        if len(screens["buy"]["options"]) == 0:
            add_store_buy_in_screen(screens, store)
        else:
            del_all_options(screens["buy"]["options"])
            add_store_buy_in_screen(screens, store)
    
    elif screen_id == "sell":
        if len(screens["sell"]["options"]) == 0:
            add_store_sell_in_screen(screens, inventory)
        else:
            del_all_options(screens["sell"]["options"])
            add_store_sell_in_screen(screens, inventory)
    
    action = 0
    
    return action

def store_screen(screens, previous_store_screen):
    if len(screens["move"]["options"]) == 0:
        screens["move"]["options"].append(("Go to the Havencross", "village"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Whispering Woods", "forest"))
    else:
        del_all_options(screens["move"]["options"])
        screens["move"]["options"].append(("Go to the Havencross", "village"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Whispering Woods", "forest"))
    previous_store_screen = "store"
    return previous_store_screen
def hunter_sells(previous_store_screen):
    previous_store_screen = "hunter_sells"
    return previous_store_screen
# ============================================== END_STORE_EVENTS ============================================================= #

# ================================================== FOREST_EVENTS ============================================================= #
def forest(flags, screens, screen_id, action, inventory,
           forest_events, forest_events_weights, numbered_forest_events):

    if len(screens["move"]["options"]) == 0:
        screens["move"]["options"].append(("Go to the Havencross", "village"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Gorn's shop", "store"))
        if flags["guards_near_swamps"]:
            screens["move"]["options"].append(("Go to the Stinky Swamps", "swamps_path"))
        else:
            screens["move"]["options"].append(("Go to the Stinky Swamps", "swamps"))
        screens["move"]["options"].append(("Go to the Shadow Peaks", "mountains"))
    else:
        del_all_options(screens["move"]["options"])
        screens["move"]["options"].append(("Go to the Havencross", "village"))
        screens["move"]["options"].append(("Go to the Drunken Dragon tavern", "tavern"))
        screens["move"]["options"].append(("Go to the Gorn's Shop", "store"))
        if flags["guards_near_swamps"]:
            screens["move"]["options"].append(("Go to the Stinky Swamps", "swamps_path"))
        else:
            screens["move"]["options"].append(("Go to the Stinky Swamps", "swamps"))
        screens["move"]["options"].append(("Go to the Shadow Peaks", "mountains"))  
    
    if action == 1:
        event = choose_random_event(forest_events, forest_events_weights)[0]
        index = find_object_index_array(event, forest_events)
        if event == "villagers": # One time 
            screen_id = event
            del forest_events[index]
            del forest_events_weights[index]
            action = 0
        elif event == "bear": # One time
            screen_id = event    
            action = 0
        elif event == "bear_lair": # One time
            screen_id = event
            del forest_events[index]
            del forest_events_weights[index]
            action = 0
        elif event == "herbs": # Rep N = 10
            screen_id = event
            action = 0
        elif event == "boar": # Rep N = 10
            screen_id = event
            action = 0
        elif event == "travelers": # Rep N = 3
            screen_id = event
            action = 0
        elif event == "mushrooms": # Rep
            screen_id = event
            action = 0
        elif event == "stone": # One time
            screen_id = event
            del forest_events[index]
            del forest_events_weights[index]      
            action = 0
        elif event == "wolves": # Rep N = 4
            screen_id = event
            action = 0
        elif event == "merchant": # Rep N = 15
            screen_id = event
            action = 0

    return screen_id, action

def stone(screen_id, action, forest_events, forest_events_weights, state):
    if action == 1:
        if(check_if_object_in_array("bear", forest_events)):
            index = find_object_index_array("bear", forest_events)
            del forest_events[index]
            del forest_events_weights[index]
        
        if(check_if_object_in_array("wolves", forest_events)):
            index = find_object_index_array("wolves", forest_events)
            del forest_events[index]
            del forest_events_weights[index]
    elif action == 2:
        state["health"] += 40
        state["max_mana"] += 5
        state["mana"] = state["max_mana"]
    elif action == 3:
        if state["mana"] >= 20:
            state["mana"] -= 20
            screen_id = "wait_druinds"
            action = 0
    return screen_id, action

def mushrooms(screen_id, action, location_of_end):
    if action == 1:
        screen_id = "GAME_OVER"
        location_of_end = "mushrooms"
        action = 0
    return screen_id, action, location_of_end
 
def villagers(screen_id, action, inventory, flags, state, forest_events, forest_events_weights):
    if action == 1:
        inventory.append({"name": "Berries", "status": "item"})
        flags["berries"] = True
    elif action == 2:
        index = find_object_index_array("bear", forest_events)
        forest_events_weights[index] /= 2
    elif action == 3 and state["mana"] >= 20:
        index = find_object_index_array("bear_lair", forest_events)
        forest_events_weights[index] = 20
        flags["berries"] = True
        state["mana"] -= 20
        inventory.append({"name": "Berries", "status": "item"})
        screen_id = "help_villagers"
        action = 0
    return screen_id, action

def bear_lair(screen_id, action, lair_events, lair_weights, forest_events, inventory, state):
    if action == 1:
        if len(lair_events) != 0:
            event = lair_events[random.randint(0, (len(lair_events) - 1))]
            index = find_object_index_array(event, lair_events)

            if "bear" in forest_events:
                lair_weights["counter"] += 1
                if lair_weights["counter"] > 2:
                    lair_weights["bear_attack_chance"] = 35
                elif lair_weights["counter"] > 3:
                    lair_weights["bear_attack_chance"] = 70
                elif lair_weights["counter"] > 4:
                    lair_weights["bear_attack_chance"] = 100

            if roll() > lair_weights["bear_attack_chance"]:
                if event == "ring": # One time 
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Silver ring", "status": "item"})
                    action = 0
                elif event == "coat": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Warm coat", "status": "item"})
                    action = 0
                elif event == "gold_1": # One time
                    screen_id = event
                    del lair_events[index]
                    state["gold"] += 25
                    action = 0
                elif event == "lair_herbs": # One time
                    screen_id = event
                    del lair_events[index]
                    if check_if_item_in_inventory("Herbs", inventory):
                        inventory[find_item_index_inventory("Herbs", inventory)]["count"] += 3
                    else:
                        inventory.append({"name": "Herbs", "status": ("counted", "leaves"), "count": 1})
                        action = 0
                elif event == "pendant": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Magic pendant", "status": "tools"})
                    action = 0
                elif event == "backpack": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Old backpack", "status": "item"})
                    action = 0
                elif event == "tools": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Crafting tools", "status": "item"})
                    action = 0
                elif event == "dagger": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Rusty dagger", "status": "equip", 
                                      "stats":{"type_of_weapon": "sword", "damage": 8}})
                    action = 0
                elif event == "gold_2": # One time
                    screen_id = event
                    del lair_events[index]
                    state["gold"] += 25
                    action = 0
                elif event == "lair_key": # One time
                    screen_id = event
                    del lair_events[index]
                    inventory.append({"name": "Bear's lair key", "status": "tools"})
                    action = 0
            else:
                screen_id = "bear"
                action = 0

    return screen_id, action
    

def herbs(action, inventory, numbered_forest_events, forest_events_weights, forest_events):
    if action == 1:
        if check_if_item_in_inventory("Herbs", inventory):
            inventory[find_item_index_inventory("Herbs", inventory)]["count"] += 1
        else:
            inventory.append({"name": "Herbs", "status": ("counted", "leaves"), "count": 1})
        numbered_forest_events["herbs"] -= 1
        index = find_object_index_array("herbs", forest_events)
        forest_events_weights[index] = numbered_forest_events["herbs"] * 3


def boar(action, screen_id, inventory, numbered_forest_events, forest_events_weights, forest_events):
    if action == 1:
        hunt_chance = 20
        if check_if_item_in_inventory("Hunting Bow", inventory):
            hunt_chance += 30
        if check_if_item_in_inventory("Hunting knife", inventory):
            hunt_chance += 20
        
        if roll() < hunt_chance:
            screen_id = "success_hunt_boar"
            if check_if_item_in_inventory("Boar meat", inventory):
                inventory[find_item_index_inventory("Boar meat", inventory)]["count"] += 1
            else:
                inventory.append({"name": "Boar meat", "status": ("counted", "meat"), "count": 1})
            
            if check_if_item_in_inventory("Boar leather", inventory):
                inventory[find_item_index_inventory("Boar leather", inventory)]["count"] += 1
            else:
                inventory.append({"name": "Boar leather", "status": ("counted", "leather"), "count": 1})
            
            numbered_forest_events["boar"] -= 1
            index = find_object_index_array("boar", forest_events)
            forest_events_weights[index] = numbered_forest_events["boar"] * 3
            action = 0
        else:
            screen_id = "failure_hunt_boar"
            action = 0
    
    return screen_id, action

def travelers(action, screen_id, numbered_forest_events, forest_events_weights, forest_events, state):
    if action == 1:
        if roll() < 70:
            screen_id = "good_travelers"
            state["health"] += 20
            state["mana"] += 20
            numbered_forest_events["travelers"] -= 1
            index = find_object_index_array("travelers", forest_events)
            forest_events_weights[index] = numbered_forest_events["travelers"] * 3
            action = 0
        else:
            screen_id = "bad_travelers"
            state["gold"] = 0
            numbered_forest_events["travelers"] -= 1
            index = find_object_index_array("travelers", forest_events)
            forest_events_weights[index] = numbered_forest_events["travelers"] * 3
            action = 0
    
    return screen_id, action

def bear(screens, screen_id, action, inventory, flags, state):
    if check_if_item_in_inventory("Berries", inventory) and flags["berries"]:
        screens["bear"]["options"].append(("Try to offer berries to the bear", "berries_bear"))
        flags["berries"] = False
    
    if action == 1:
        screens["fight"]["text"] = "You raise your weapon and charge at the bear, ready to defend yourself."
        flags["fight_bear"] = True
    elif action == 2:
        if state["mana"] >= 50:
            state["mana"] -= 50
            screen_id = "run_away_bear"
            action = 0

    return screen_id, action

def wolves_func(screens, screen_id, action, flags, state, inventory):
    indexes, in_inventory = find_specific_item_status("meat", inventory)
    if in_inventory and not check_if_option_in_screen("throw_meat", screens["wolves"]["options"]):
        for index in indexes:
            screens["wolves"]["options"].append(("Throw " + inventory[index]["name"] + " to the wolves.", "throw_meat"))

    else:
        del_all_options_for_key("throw_meat", screens["wolves"]["options"])
        for index in indexes:
            screens["wolves"]["options"].append(("Throw " + inventory[index]["name"] + " to the wolves.", "throw_meat"))

    if(check_if_item_in_inventory("Magic flute", inventory) and not \
        check_if_option_in_screen("use_magic_wolves", screens["wolves"]["options"]) and state["mana"] >= 20):
        
        screens["wolves"]["options"].append(("Use a \"Magic flute\" [20 mana]", "use_magic_wolves"))
    
    elif((check_if_option_in_screen("use_magic_wolves", screens["wolves"]["options"]) and state["mana"] < 20) or \
        not check_if_item_in_inventory("Magic flute", inventory)):

        del_option("use_magic_wolves", screens["wolves"]["options"])

    if action == 1:
        flags["fight_wolves"] = True
    elif action == 2:
        if roll() > 80:
            screens["run_away_wolves"]["text"] = "Your heart races and your breath is ragged. " \
                "After a few moments, you realize that you have lost them, and stop to catch your breath."
        else:
            screens["run_away_wolves"]["text"] = "You turn and bolt in the opposite direction, but" \
                " the wolves quickly catch up with you. They leap onto your back and bring you to the ground." \
                " \\p\n-40 health"
            state["health"] -= 40
    elif action == 3 and check_if_option_in_screen("use_magic_wolves", screens["wolves"]["options"]):
        state["mana"] -= 20

    elif action != 0 and action <= len(screens["wolves"]["options"]) and \
        screens["wolves"]["options"][action - 1][1] == "throw_meat":
        item_index = 0
        count = 0
        for option in screens["wolves"]["options"]:
            for index in indexes:
                if option[0] == "Throw " + inventory[index]["name"] + " to the wolves." and \
                    action - 1 == count:
                    item_index = index
                    break
            if count == action - 1:
                break
            count += 1
        
        inventory[item_index]["count"] -= 1
        if inventory[item_index]["count"] == 0:
            del inventory[item_index]
        
    
    return screen_id, action

# ======================================================= END_FOREST_EVENTS ====================================================== #

# ====================================================== SWAMPS_EVENTS ======================================================= #
def swamps(screens, screen_id, flags, swamp_events, swamps_events_weights, action):
    
    if not flags["guards_near_swamps"] and action == 1:
        event = choose_random_event(swamp_events, swamps_events_weights)[0]
        index = find_object_index_array(event, swamp_events)
        if event == "statue": # One time 
            screen_id = event
            del swamp_events[index]
            del swamps_events_weights[index]
            action = 0
        elif event == "obelisk": # One time
            screen_id = event
            del swamp_events[index]
            del swamps_events_weights[index]
            action = 0
        elif event == "rusted_sword": # One time
            screen_id = event
            del swamp_events[index]
            del swamps_events_weights[index]
            action = 0
        elif event == "purple_flowers_1": # Rep
            screen_id = event
            action = 0
        elif event == "purple_flowers_2": # Rep
            screen_id = event
            action = 0
        elif event == "solid_ground": # Rep
            screen_id = event
            action = 0
        elif event == "creature": # Three times
            screen_id = event
            action = 0
        elif event == "goblin": # One time
            screen_id = event
            action = 0

    if flags["path_to_shadow_peaks"]:
        screens["swamps"]["options"].append(("Follow the path that Jacob told", "swamps")) # Add mautains path
        flags["path_to_shadow_peaks"] = False

    return screen_id, action

def statue(screens, state, inventory, action):
    if action != 0 and action - 1 < len(screens["statue"]["options"]):
        if action == 1:
            screens["event"]["text"] = "The statue comes to life and reveals itself to be a friendly" \
                                        " spirit. It offers to aid you in your quest and grants you a" \
                                        " boon of increased mana. (+10 Max Mana)"
            state["max_mana"] += 10
            action = 0
        elif action == 2:
            screens["event"]["text"] = "You find a gem in the statue's eye socket"'. ("Gem", costs 50 gold)'
            inventory.append({"name": "Gem", "status": "item"})
            action = 0
        
def obelisk(screens, state, spells, action):
    if action != 0 and action - 1 < len(screens["obelisk"]["options"]):
        if action == 1:
            screens["event"]["text"] = "The runes pulse as you place your hand on the obelisk, and" \
                                        " you feel a surge of power. (Restore mana to full)"
            state["mana"] = state["max_mana"]
            action = 0
        elif action == 2:
            screens["event"]["text"] = "You study the runes on the obelisk and learn a new spell." \
                                        ' + "Water splash" spell - makes an enemy wet (double damage from Frostbolt),' \
                                        " makes enemy to skip 1 attack (stun)"
            spells.append({"name": "Water splash", "stats" :{"effect": "water", "damage": 10, "mana_cost": 15}})
            action = 0

def rusted_sword(screens, state, inventory, action):    
    if action != 0 and action - 1 < len(screens["rusted_sword"]["options"]):
        if action == 1:
            screens["event"]["text"] = "The sword is rusty and dirty, but you take it anyway." \
                                    ' + "Rusty sword" (5 damage, 10 gold)'
            inventory.append({"name": "Rusty sword", "status": "equip", "stats":{"type_of_weapon": "sword", "damage": 5}})
            action = 0
        elif action == 2:
            screens["event"]["text"] = "Attempt to clean the sword before picking it up. You spend" \
                                        " some time cleaning the sword and it looks like it was not" \
                                        ' here for that long. - 30 mana + "Fine sword"  (15 damage, 30 gold)'
            inventory.append({"name": "Fine sword", "status": "equip", "stats":{"type_of_weapon": "sword", "damage": 15}})
            state["mana"] -= 30
            action = 0

def purple_flowers_1(screens, state, inventory, action):
    if action != 0 and action - 1 < len(screens["purple_flowers_1"]["options"]):
        if action == 1:
            screens["event"]["text"] = "You carefully pluck some of the purple flowers and add" \
                                        ' them to your inventory. + "Purple flowers" (5 gold)'
            if check_if_item_in_inventory("Purple flowers", inventory):
                inventory[find_item_index_inventory("Purple flowers", inventory)]["count"] += 1
            else:
                inventory.append({"name": "Purple flowers", "status": ("counted", "flowers"), "count": 1})
            action = 0
        elif action == 2:
            screens["event"]["text"] = "You attack the plants, but the hissing gets louder and" \
                " louder until a swarm of angry wasps emerges and attacks you. -10 health"   
            state["health"] -= 10
            action = 0 

def purple_flowers_2(screens, state, inventory, action):
    if action != 0 and action - 1 < len(screens["purple_flowers_2"]["options"]):
        if action == 1:
            screens["event"]["text"] = "You try to pluck some of the purple flowers, but the hissing" \
                            " gets louder and louder until a swarm of angry wasps" \
                                " emerges and attacks you. -10 health"   
            state["health"] -= 10
            action = 0 
        elif action == 2:
            screens["event"]["text"] = "You attack the plants, and happen to hit a snake that was" \
                                " lurking in the flowers. You might get some money" \
                                    ' for it in the store. + "Dead snake" (5 gold)'
            if check_if_item_in_inventory("Dead snake", inventory):
                inventory[find_item_index_inventory("Dead snake", inventory)]["count"] += 1
            else:
                inventory.append({"name": "Dead snake", "status": ("counted", "snake"), "count": 1})
            action = 0

def solid_ground(screens, state, action):
    if action != 0 and action - 1 < len(screens["solid_ground"]["options"]):
        if action == 1:
            screens["event"]["text"] = "You exert all your strength to pull yourself out of the quicksand."
            if roll() >= 50:
                state["health"] -= 10
        elif action == 2:
            if roll() >= 50:
                state["mana"] -= 10
        action = 0

def creature_enemy(screens, flags, state, action):
    if action != 0 and action - 1 < len(screens["creature"]["options"]):
        if action == 1:
            flags["fight_creature"] = True
        elif action == 2:
            screens["event"]["text"] = "You cast a spell to create a loud noise," \
                            " which causes the creature to turn away from you."
            state["mana"] -= 10

def goblin_enemy(screens, flags, action):
    if action != 0 and action - 1 < len(screens["goblin"]["options"]):
        if action == 1:
            screens["fight"]["text"] = "How do you want to attack ?"
            flags["fight_goblin"] = True

def bribe_guards(state, flags):
    if flags["guards_near_swamps"]:
        state["gold"] -= 75
        flags["guards_near_swamps"] = False

def swamps_path(screens, flags, action):
    if len(screens["move"]["options"]) == 0:
        screens["move"]["options"].append(("Go to the Whispering Woods", "forest"))
    else:
        del_all_options(screens["move"]["options"])
        screens["move"]["options"].append(("Go to the Whispering Woods", "forest"))
        
    if action != 0 and action - 1 < len(screens["swamps_path"]["options"]):
        if screens["swamps_path"]["options"][action - 1][0] == "Continue" and flags["party_in_tavern"]:
            screens["swamps_path"]["text"] = "One of the guards steps forward and looks at you closely." \
                " Suddenly, his eyes light up. \\p\n"'"Hey, I remember you! You were at the tavern with us a' \
                ' few days ago. That was one wild night!" \\p\n'"The other guards nod in agreement, smiling. \\p\n" \
                '"'"We'll let you through this time, but don't make a habit of it. We wouldn't want to have" \
                ' to save you from the swamp creatures again, haha!"'
            
            del_option("swamps_path", screens["swamps_path"]["options"])
            flags["guards_near_swamps"] = False
            screens["swamps_path"]["options"].append(("Move on", "swamps"))
            action = 0

        elif screens["swamps_path"]["options"][action - 1][0] == "Continue" and not flags["party_in_tavern"]:
            del_option("swamps_path", screens["swamps_path"]["options"])
            screens["swamps_path"]["options"].append(("Look for a path around the guards", "find_path"))
            screens["swamps_path"]["options"].append(("Bribe the guards (75 gold)", "bribe_guards"))
            screens["swamps_path"]["options"].append(("Attack the guards", "fight_guards"))
            action = 0
        
        elif flags["party_in_tavern"] and len(screens["swamps_path"]["options"]) != 0:
            screens["swamps_path"]["text"] = "One of the guards steps forward and looks at you closely. Suddenly, his eyes light up." \
                                    '"Hey, I remember you! You were at the tavern with us a few days ago. That was one wild'  \
                                    'night!" The other guards nod in agreement, smiling.' \
                                    "We'll let you through this time, but don't make a habit of it." \
                                    "We wouldn't want to have to save you from the swamp creatures again, haha!" \
                                    "They step aside, allowing you to pass."
            del_all_options(screens["swamps_path"]["options"])
            flags["guards_near_swamps"] = False
            screens["swamps_path"]["options"].append(("Move on", "swamps"))

    return action

def fight_guards(screens, flags, action):
    if action != 0 and action - 1 < len(screens["fight_guards"]["options"]):
        if action == 1:
            flags["fight_guards"] = True
# ========================================================== END_SWAMPS_EVENTS ================================================= #