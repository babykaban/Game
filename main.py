import pygame
import random
import json
from events import *
from fights import *
from enemes import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1128, 634))
pygame.display.set_caption("Adventure Game")
# Load the background image
background = pygame.image.load("images//start.png")

# Create font objects
font_name_options_screens = "fonts//BlackChancery.ttf"
font_name_inventory_health_spells = "fonts//DragonHunter.otf"
font_size_options_screens = 22
font_size_health_spells = 20
font_size_inventory = 16
tip_text = ""


screen_font = pygame.font.Font(font_name_options_screens, font_size_options_screens)
options_font = pygame.font.Font(font_name_options_screens, font_size_options_screens)
health_mana_gold_font = pygame.font.Font(font_name_inventory_health_spells, font_size_health_spells)
inventory_font = pygame.font.Font(font_name_inventory_health_spells, font_size_inventory)

# Set up the clock
clock = pygame.time.Clock()

# Set the desired frame rate (in FPS)
frame_rate = 33

# Global veriables
screen_id = "forest"
watch_screen = "forest"
running = False
action = 0 
inventory_location = ""
location = ""
enemy = 0 

location_to_move = ""
location_of_end = ""
pay_for_rest = 20

# Read screens file

"""
 In this dictionary stored "screens". 
 "Screen" has a text that corresponds to game event, options and function.

 Option is a tuple: first element is option text, second element is a screen
 that will be displayed after clicking the corresponding option.

 Function: this is a certain fuction that changes text on screens
 or player state or other game events which happen or will happen  
 while player doing simething in the coresponding screen.

"""
with open("screens.json", "r") as file:
    screens = json.load(file)

# FLags to events
flags = {"hero_saw_bandits": False,
         "you_are_drunk": False,
         "party_in_tavern": False,
         "you_know_Jacob": False,
         "church_quest": False,
         "church_quest_done": False,
         "bandits_near_tavern": True, 
         "troll": False,
         "inventory_open": False,
         "you_know_where_jacob_live": False,
         "beer": False,
         "conversation_done": False,
         "path_to_shadow_peaks": False,
         "guards_near_swamps": True,
         "fight_guards": False,
         "fight_creature": False,
         "fight_goblin": False,
         "troll_in_forest": True,
         "fight_troll": False,
         "bear_lair": False,
         "fight_bear": False,
         "berries": False,
         "fight_wolves": False} 

def inventory_screen():
    if flags["inventory_open"]:
        if len(screens["inventory"]["options"]) == 0:
            add_inventory_in_screen()
        else:
            processingInventoryEvents()
            del_all_options(screens["inventory"]["options"])
            add_inventory_in_screen()        
# =========================================================== FIGHT_FUNCTIONS ======================================== #
def choose_guard():
    global screen_id
    global action
    global enemy
    if action - 1 < len(screens["choose_guard"]["options"]):
        if len(guards) > 1:
            if screens["choose_guard"]["options"][action - 1][0] == "Guard_1" or "Guard_2" or "Guard_3":
                if action == 1:
                    enemy = 1
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 2:
                    enemy = 2
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 3:
                    enemy = 3
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
        else:
            enemy = 0

def choose_wolf():
    global screen_id
    global action
    global enemy
    if action - 1 < len(screens["choose_wolf"]["options"]):
        if len(wolves) > 1:
            if screens["choose_wolf"]["options"][action - 1][0] == "Black wolf" or "Grey wolf" or "Brown wolf":
                if action == 1:
                    enemy = 1
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 2:
                    enemy = 2
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 3:
                    enemy = 3
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
        else:
            enemy = 0

def choose_bandit():
    global enemy
    global screen_id
    global action
    if action - 1 < len(screens["choose_bandit"]["options"]):
        if len(bandits) > 1:
            if screens["choose_bandit"]["options"][action - 1][0] == "Bandit_1" or "Bandit_2" or "Bandit_Leader":
                if action == 1:
                    enemy = 1
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 2:
                    enemy = 2
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
                elif action == 3:
                    enemy = 3
                    screen_id = "attack"
                    screens["attack"]["text"] = "How do you want to attack"
                    action = 0
        else:
            enemy = 0

def add_spells_to_screen():
    global spells
    if len(screens["spells"]["options"]) != 0:
        del_all_options(screens["spells"]["options"])
        for spell in spells:
            screens["spells"]["options"].append((spell["name"], "evade"))
    else:
        for spell in spells:
            screens["spells"]["options"].append((spell["name"], "evade"))
    
    screens["spells"]["options"].append(("Back", ""))

def attack_and_spell():
    global action
    global screen_id
    global location_to_move

    global guard_enemes
    global bandit_enemes
    global wolves_enemes
    
    global forest_events
    global forest_events_weights
    global numbered_forest_events
    global swamp_events
    global swamps_events_weights


    events = {"forest_events": {"events": forest_events, 
                                "weights": forest_events_weights, 
                                "numbered_events": numbered_forest_events},
              
              "swamp_events": {"events": swamp_events, 
                               "weights": swamps_events_weights}}

    add_spells_to_screen()
    if action != 0 and action <= len(screens["spells"]["options"]):
        if flags["hero_saw_bandits"] and flags["bandits_near_tavern"]:
            if screen_id == "spells":
                bandit_enemes, screen_id, action, location_to_move, events = \
                    attack_enemy_in_multiple_fight_spell(enemy, bandits, bandit_enemes, 
                    "choose_bandit", spells, parameters, events)
            
            elif action == 1 and screen_id != "spells":
                bandit_enemes, screen_id, action, location_to_move, events = \
                        attack_enemy_in_multiple_fight_weapon(enemy, bandits, bandit_enemes, 
                        "choose_bandit", parameters, events)

        elif flags["guards_near_swamps"] and flags["fight_guards"]:
            if screen_id == "spells":
                guard_enemes, screen_id, action, location_to_move, events = \
                    attack_enemy_in_multiple_fight_spell(enemy, guards, guard_enemes, 
                    "choose_guard", spells, parameters, events)
            
            elif action == 1 and screen_id != "spells":
                guard_enemes, screen_id, action, location_to_move, events = \
                        attack_enemy_in_multiple_fight_weapon(enemy, guards, guard_enemes, 
                        "choose_guard", parameters, events)

        elif flags["fight_wolves"]:
            if screen_id == "spells":
                wolves_enemes, screen_id, action, location_to_move, events = \
                    attack_enemy_in_multiple_fight_spell(enemy, wolves, wolves_enemes, 
                    "choose_wolf", spells, parameters, events)
            
            elif action == 1 and screen_id != "spells":
                wolves_enemes, screen_id, action, location_to_move, events = \
                        attack_enemy_in_multiple_fight_weapon(enemy, wolves, wolves_enemes, 
                        "choose_wolf", parameters, events)

        elif flags["fight_creature"]:
            if screen_id == "spells":
                screen_id, action, location_to_move, events = \
                    attack_enemy_spell(creature, spells, parameters, events)
            elif action == 1 and screen_id != "spells":
                screen_id, action, location_to_move, events = \
                        attack_enemy_weapon(creature, parameters, events)

        elif flags["fight_goblin"]:
            if screen_id == "spells":
                screen_id, action, location_to_move, events = \
                    attack_enemy_spell(goblin, spells, parameters, events)
            elif action == 1 and screen_id != "spells":
                screen_id, action, location_to_move, events = \
                        attack_enemy_weapon(goblin, parameters, events)

        elif flags["fight_troll"]:
            if screen_id == "spells":
                screen_id, action, location_to_move, events = \
                    attack_enemy_spell(troll, spells, parameters, events)
            elif action == 1 and screen_id != "spells":
                screen_id, action, location_to_move, events = \
                        attack_enemy_weapon(troll, parameters, events)

        elif flags["fight_bear"]:
            if screen_id == "spells":
                screen_id, action, location_to_move, events = \
                    attack_enemy_spell(bear_enemy, spells, parameters, events)
            elif action == 1 and screen_id != "spells":
                screen_id, action, location_to_move, events = \
                        attack_enemy_weapon(bear_enemy, parameters, events)

    forest_events = events["forest_events"]["events"]
    forest_events_weights = events["forest_events"]["weights"]
    numbered_forest_events = events["forest_events"]["numbered_events"]
    swamp_events = events["swamp_events"]["events"]
    swamps_events_weights = events["swamp_events"]["weights"]

def evade():
    global bandit_enemes
    global guard_enemes
    global wolves_enemes

    global action
    global screen_id
   
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["hero_saw_bandits"] and \
        flags["bandits_near_tavern"]:
        if screens["evade"]["options"][0][1] == "attack":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "evade"))
            screens["evade"]["options"].append(("Try to parry", "evade"))
            screens["evade"]["options"].append(("Block with magic shield", "evade"))
        
        if bandit_enemes == 1:
            bandit_enemes, action = evade_enemes(bandits, bandit_enemes, "choose_bandit", parameters)
            if len(bandits) > 1:
                screen_id = "choose_bandit"
                action = 0
            else:
                screen_id = "attack"
                action = 0
        else:
            bandit_enemes, action = evade_enemes(bandits, bandit_enemes, "choose_bandit", parameters)
    
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["guards_near_swamps"] \
        and flags["fight_guards"]:
        
        if screens["evade"]["options"][0][1] == "attack":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "evade"))
            screens["evade"]["options"].append(("Try to parry", "evade"))
            screens["evade"]["options"].append(("Block with magic shield", "evade"))

        if guard_enemes == 1:
            guard_enemes, action = evade_enemes(guards, guard_enemes, "choose_guard", parameters)
            if len(guards) > 1:
                screen_id = "choose_guard"
                action = 0
            else:
                screen_id = "attack"
                action = 0
        else:
            guard_enemes, action = evade_enemes(guards, guard_enemes, "choose_guard", parameters)
    
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["fight_wolves"] :
        
        if screens["evade"]["options"][0][1] == "attack":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "evade"))
            screens["evade"]["options"].append(("Try to parry", "evade"))
            screens["evade"]["options"].append(("Block with magic shield", "evade"))

        if wolves_enemes == 1:
            wolves_enemes, action = evade_enemes(wolves, wolves_enemes, "choose_wolf", parameters)
            if len(wolves) > 1:
                screen_id = "choose_wolf"
                action = 0
            else:
                screen_id = "attack"
                action = 0
        else:
            wolves_enemes, action = evade_enemes(wolves, wolves_enemes, "choose_wolf", parameters)

    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["fight_creature"]:
        if screens["evade"]["options"][0][1] == "evade":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "attack"))
            screens["evade"]["options"].append(("Try to parry", "attack"))
            screens["evade"]["options"].append(("Block with magic shield", "attack"))
        
        screen_id, action = evade_enemy(creature, parameters)
    
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["fight_goblin"]:
        if screens["evade"]["options"][0][1] == "evade":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "attack"))
            screens["evade"]["options"].append(("Try to parry", "attack"))
            screens["evade"]["options"].append(("Block with magic shield", "attack"))
        screen_id, action = evade_enemy(goblin, parameters)
    
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["fight_troll"]:
        if screens["evade"]["options"][0][1] == "evade":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "attack"))
            screens["evade"]["options"].append(("Try to parry", "attack"))
            screens["evade"]["options"].append(("Block with magic shield", "attack"))
        screen_id, action = evade_enemy(troll, parameters)
    
    if action != 0 and action - 1 < len(screens["evade"]["options"]) and flags["fight_bear"]:
        if screens["evade"]["options"][0][1] == "evade":
            del_all_options(screens["evade"]["options"])
            screens["evade"]["options"].append(("Attempt to evade", "attack"))
            screens["evade"]["options"].append(("Try to parry", "attack"))
            screens["evade"]["options"].append(("Block with magic shield", "attack"))
        
        screen_id, action = evade_enemy(bear_enemy, parameters)

# ======================================================= FIGHT_FUNCTIONS ============================================== #

# ======================================================= RenderTextFunction =========================================== #
def renderTextAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            if words[0] == "\\p":
                words.pop(0)
                break
            else:
                line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            
            if fw >= allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x
        ty = y + y_offset
        y_offset += fh

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))
# ======================================================= END_RenderTextFunction ======================================= #

# NOTE: for testing["Bastion Sword", "equip", {"type_of_weapon": "sword", "damage": 20}]

store = [{"name": "Bastard sword", "price": 40, "type": ("weapon", "weapon"), "stats": {"type": "sword", "damage": 30}}, 
        {"name": "Heal Potion", "price": 10, "type": ("counted", "potion")}, 
        {"name": "Mana Potion", "price": 10, "type": ("counted", "potion")}, 
        {"name": "Hunting Bow", "price": 30, "type": ("tools", "tool")}, 
        {"name": "Axe's Axe", "price": 30, "type": ("weapon", "weapon"), "stats": {"type": "axe", "damage": 20}}, 
        {"name": "FireBall", "price": 40, "type": ("spell", "spell"), "stats": {"effect": "fire", "damage": 30, "mana_cost": 60}}, 
        {"name": "FrostBall", "price": 30, "type": ("spell", "spell"), "stats": {"effect": "ice", "damage": 25, "mana_cost": 40}}]

# TODO: merchant in the forest
travelling_merchant = ["Lighting Bolt", "Beather armor", "Heal Potion", "Mana Potion"]

items_sell_prices = [{"item": "Heal Potion", "sell_price": 5},
                     {"item": "Mana Potion", "sell_price": 5},
                     {"item": "Metal sword", "sell_price": 10},
                     {"item": "Axe's Axe", "sell_price": 15},
                     {"item": "Bastard sword", "sell_price": 20},
                     {"item": "Dead snake", "sell_price": 5},
                     {"item": "Purple flowers", "sell_price": 5},
                     {"item": "Gem", "sell_price": 50},
                     {"item": "Rusty sword", "sell_price": 5},
                     {"item": "Fine sword", "sell_price": 30},
                     {"item": "Golden Locket", "sell_price": 100},
                     {"item": "Long sword", "sell_price": 100},
                     {"item": "Berries", "sell_price": 10},
                     {"item": "Silver ring", "sell_price": 30},
                     {"item": "Warm coat", "sell_price": 10},
                     {"item": "Herbs", "sell_price": 5},
                     {"item": "Old backpack", "sell_price": 15},
                     {"item": "Crafting tools", "sell_price": 30},
                     {"item": "Rusty dagger", "sell_price": 5},
                     {"item": "Boar meat", "sell_price": 10},
                     {"item": "Boar leather", "sell_price": 10},
                     {"item": "Beer", "sell_price": 5},
                     {"item": "Troll hide", "sell_price": 100},
                     {"item": "Bear hide", "sell_price": 80},
                     {"item": "Bastion Sword", "sell_price": 20},
                     {"item": "Wolven hide", "sell_price": 15},
                     {"item": "", "sell_price": 0}]


# Player state, inventory, spells, store

# {"name": "Bastion Sword", "status": "equip", "stats": {"type_of_weapon": "sword", "damage": 20}}
inventory = [{"name": "Metal sword", "status": ["equipped", "weapon"], "stats":{"type_of_weapon": "sword", "damage": 10}},
             {"name": "Bastion Sword", "status": ["equip", "weapon"], "stats": {"type_of_weapon": "sword", "damage": 20}},
             {"name": "Heal Potion", "status": ("counted", "potion"), "count": 2},
             {"name": "Mana Potion", "status": ("counted", "potion"), "count": 2},
             {"name": "Pork", "status": ("counted", "meat"), "count": 4}]

# NOTE: for testing ["FireBall", {"effect": "fire", "damage": 30, "mana_cost": 60}]
spells = [{"name": "Arcane Misile", "stats" :{"effect": "nothing", "damage": 15, "mana_cost": 10}}]

state = {"health": 100,
         "max_mana": 100,
         "mana": 100,
         "gold": 100}

# Explore events in swamps
swamp_events = ["statue", "obelisk", "rusted_sword", "purple_flowers_1", 
                "purple_flowers_2", "solid_ground", "creature", "goblin"]

swamps_events_weights = [10, 10, 20, 15, 15, 20, 15, 10]

# Explore events in forest
numbered_forest_events = {"herbs": 10, "boar": 10, "travelers": 3, "wolves": 4}

forest_events = ["villagers", "bear", "herbs", "boar", 
                 "travelers", "wolves", "mushrooms", "merchant", "stone", "bear_lair"]

forest_events_weights = [10, 10, numbered_forest_events["herbs"] * 3, 
                         numbered_forest_events["boar"] * 3,
                         numbered_forest_events["travelers"] * 10, 
                         numbered_forest_events["wolves"] * 400, 1, 15, 5, 0]

# Explore events bear lair

lair_events = ["ring", "coat", "gold_1", "lair_herbs", 
               "pendant", "backpack", "tools", "dagger", "gold_2", "lair_key"]
lair_weights = {"counter": 0, "bear_attack_chance": 0}

def showSpells():
    text = "Your spells: \\p\n"
    for spell in spells:
        text += spell["name"] + " \\p\n"
    
    renderTextAt(text, inventory_font, (0, 0, 0), 690, 320, screen, 800)

def check_mana_health_gold(screen_id):

    if state["health"] > 100:
        state["health"] = 100
    elif state["health"] <= 0:
        screen_id = "GAME_OVER"
    
    if state["mana"] > state["max_mana"]:
        state["mana"] = state["max_mana"]
    
    if state["gold"] <= 0:
        state["gold"] = 0
    
    return screen_id


def changeScreen(action):
    global screen_id
    if action != 0 and action <= len(watch_screen["options"]):
        screen_id = watch_screen["options"][action - 1][1]
        action = 0
    return action

def showHealth():
    state_text = "Health: {} / 100  Mana: {} / {}  Gold: {}".format(state["health"], 
                                                           state["mana"], 
                                                           state["max_mana"], 
                                                           state["gold"])
    renderTextAt(state_text, health_mana_gold_font, (0, 0, 0), 5, 5, screen, 800)


def showInventory():
    if screen_id != "inventory":
        text = "Inventory: \\p\n"
        for item in inventory:
            if item["status"][0] == "equipped":
                text += item["name"] + "(" + item["status"][0] + ")" + " \\p\n"
            elif item["status"][0] == "equip":
                    text += item["name"] + " \\p \n"
            elif item["status"][0] == "counted":
                text += item["name"] + " " + str(item["count"]) + " \\p\n"
            else:
                text += item["name"] + " \\p\n"

        renderTextAt(text, inventory_font, (0, 0, 0), 865, 320, screen, 800)
    else:
        text = ""
        renderTextAt(text, inventory_font, (0, 0, 0), 865, 320, screen, 800)

# TODO: Move to the events.py
def add_inventory_in_screen():
    text = ""
    if screen_id == "inventory":
        for item in inventory:
            if item["status"][0] == "counted":
                screens["inventory"]["options"].append((item["name"] + " " + str(item["count"]), "inventory"))
            else:
                if item["status"][0] == "equipped":
                    screens["inventory"]["options"].append((item["name"] + " (" + item["status"][0] + ")", "inventory"))
                elif item["status"][0] == "equip":
                    screens["inventory"]["options"].append((item["name"], "inventory"))
                elif item ["status"][0] == "item" or item["status"][0] == "tools":
                    text += item["name"] + " \\p\n"
        renderTextAt(text, inventory_font, (0, 0, 0), 350, 150, screen, 800)
    else:
        text = ""
        renderTextAt(text, inventory_font, (0, 0, 0), 350, 150, screen, 800)


def processingInventoryEvents():
    global action
    if action != 0 and action - 1 < len(inventory):
        item = inventory[action - 1]
        
        if item["status"][0] == "counted":
            if item["name"] == "Heal Potion":
                state["health"] += 20
                inventory[action - 1]["count"] -= 1
                if inventory[action - 1]["count"] == 0:
                    del inventory[action - 1]
                    action = 0
            elif item["name"] == "Mana Potion":
                state["mana"] += 20
                inventory[action - 1]["count"] -= 1
                if inventory[action - 1]["count"] == 0:
                    del inventory[action - 1]
                    action = 0
            elif item["name"] == "Beer":
                state["health"] += 10
                inventory[action - 1]["count"] -= 1
                if inventory[action - 1]["count"] == 0:
                    del inventory[action - 1]
                    action = 0

        elif item["status"][0] == "equip":
            inventory[find_equipped_item_index_inventory(inventory)]["status"][0] = "equip"
            inventory[action - 1]["status"][0] = "equipped"
            action = 0


def showScreen(screen, screen_font, options_font, tip_text):  
    global background
    if screen_id == "inventory":
        options_text = ""
        i = 1
        for opt in watch_screen["options"]:
            options_text += "{} . {} \p ".format(i, opt[0])
            i += 1

        background = pygame.image.load("images//inventory.png")
        renderTextAt(watch_screen["text"], screen_font, (0, 0, 0), 40, 115, screen, 850)
        renderTextAt(options_text, options_font, (0, 0, 0), 40, 150, screen, 450)
        renderTextAt(tip_text, screen_font, (0, 0, 0), 685, 5, screen, 850)
    elif screen_id == "sell" or screen_id == "buy" or screen_id == "offer_troll":
        options_text = ""
        i = 1
        for opt in watch_screen["options"]:
            options_text += "{} . {} \p ".format(i, opt[0])
            i += 1

        background = pygame.image.load("images//store.png")
        renderTextAt(watch_screen["text"], screen_font, (0, 0, 0), 40, 115, screen, 850)
        renderTextAt(options_text, options_font, (0, 0, 0), 40, 150, screen, 450)
        renderTextAt(tip_text, screen_font, (0, 0, 0), 685, 5, screen, 850)
    elif screen_id == "spells":
        options_text = ""
        i = 1
        for opt in watch_screen["options"]:
            options_text += "{} . {} \p ".format(i, opt[0])
            i += 1

        background = pygame.image.load("images//spells_image.png")
        renderTextAt(watch_screen["text"], screen_font, (0, 0, 0), 40, 115, screen, 850)
        renderTextAt(options_text, options_font, (0, 0, 0), 40, 150, screen, 450)
        renderTextAt(tip_text, screen_font, (0, 0, 0), 685, 5, screen, 850)
    else:
        if screen_id == "forest":
            background = pygame.image.load("images//forest.png")
        elif screen_id == "move":
            background = pygame.image.load("images//map.png")
        elif screen_id == "swamps":
            background = pygame.image.load("images//swamps.png")
        elif screen_id == "shadow_peaks_path":
            background = pygame.image.load("images//bridge_forest.png")    
        else:
            background = pygame.image.load("images//text_box.png")
    
        options_text = ""
        i = 1
        for opt in watch_screen["options"]:
            options_text += "{} . {} \p ".format(i, opt[0])
            i += 1
        
        renderTextAt(watch_screen["text"], screen_font, (0, 0, 0), 30, 115, screen, 850)
        renderTextAt(options_text, options_font, (0, 0, 0), 30, 370, screen, 500)
        renderTextAt(tip_text, screen_font, (0, 0, 0), 685, 5, screen, 850)


"""
This function performs processes that occur in the game. 
It checks the event and calls the corresponding function to this event

"""
def processingEvents():
    global tip_text
    global screen_id
    global action
    global pay_for_rest

    if screen_id in screens:
        print(screen_id)
        # ===============================================================TAVERN======================================= #
        if state["health"] <= 0:
            location_of_end = "Tavern_bandits"
            screen_id = "GAME_OVER"
        
        if flags["you_know_Jacob"]:
            screens["sad_man"]["options"].append(("Ask him about Jacob", "man_jacob"))
            screens["church"]["options"].append(("Ask the monk if he knows where  \\p\n" \
                                                    "to find Jacob", "church_jacob"))
            screens["women"]["options"].append(("Ask if they know Jacob", "women_jacob"))
            flags["you_know_Jacob"] = False

        if flags["you_know_where_jacob_live"]:
            screens["village"]["options"].append(("Find Jacob's place", "jacob_home"))
            flags["you_know_where_jacob_live"] = False

        if screen_id == "village" or screen_id == "store" or \
                screen_id == "forest" or screen_id == "swamps" or screen_id == "swamps_path":
            tip_text = "To open an inventory press ' I ' \\p\n To move to another location press ' M '" 
        
        elif screen_id == "shadow_peaks_path":
            tip_text = "To open an inventory press ' I ' \\p\n To move back press ' M '" 
        
        elif screen_id == "fight" or screen_id == "attack" or \
            screen_id == "evade" or screen_id == "spells" or screen_id == "loot" or \
            screen_id == "choose_bandit" or screen_id == "choose_guard":
            tip_text = "To open an inventory press ' I ' \\p\n"
       
        elif screen_id == "buy" or screen_id == "sell":
            tip_text = "To  exit press ' Esc '"
        
        elif screen_id == "move":
            tip_text = "To open an inventory press ' I ' \\p\n Cancel movement ' Esc '" 
        elif screen_id != "inventory":
            tip_text = "To open an inventory press ' I '" 
        

        if screen_id == "innkeeper_lose_10_gold":
            func = eval(screens[screen_id]["function"])
            func(state, screens)
        
        if screen_id == "innkeeper_lose_30_gold":
            func = screens["innkeeper_lose_30_gold"]["function"]
            func(state, screens)

        elif screen_id == "innkeeper":
            func = eval(screens[screen_id]["function"])
            func(action, screens, inventory, state)

        elif screen_id == "party":
            func = eval(screens[screen_id]["function"])
            func(flags, screens)

        elif screen_id == "old_woman":
           func = eval(screens[screen_id]["function"])
           func(flags, screens)
        
        elif screen_id == "village":
            func = eval(screens[screen_id]["function"])
            func(screens)
 
        elif screen_id == "store":
            func = eval(screens[screen_id]["function"])
            func(screens)
        
        elif screen_id == "forest":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(flags, screens, screen_id, action, inventory,
           forest_events, forest_events_weights, numbered_forest_events)
        
        elif screen_id == "villagers":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screen_id, action, inventory, flags, state, forest_events, forest_events_weights)
        
        elif screen_id == "herbs":
            func = eval(screens[screen_id]["function"])
            func(action, inventory, numbered_forest_events, forest_events_weights, forest_events)
        
        elif screen_id == "boar":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(action, screen_id, inventory, 
                        numbered_forest_events, forest_events_weights, forest_events)
        
        elif screen_id == "travelers":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(action, screen_id, numbered_forest_events, 
                                    forest_events_weights, forest_events, state)

        elif screen_id == "mushrooms":
            func = eval(screens[screen_id]["function"])
            screen_id, action, location_of_end = func(screen_id, action, location_of_end)
        
        elif screen_id == "bear":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screens, screen_id, action, inventory, flags, state)
        
        elif screen_id == "bear_lair":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screen_id, action, lair_events, lair_weights, forest_events, inventory, state)
        
        elif screen_id == "choose_wolf":
            func = eval(screens[screen_id]["function"])
            func()

        elif screen_id == "wolves":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screens, screen_id, action, flags, state, inventory)

        elif screen_id == "stone":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screen_id, action, forest_events, forest_events_weights, state)

        elif screen_id == "buy" or screen_id == "sell":
            func = eval(screens[screen_id]["function"])
            action = func(screen_id, screens, state, inventory, spells, store, items_sell_prices, action)
        
        elif screen_id == "women_jacob":
            func = eval(screens[screen_id]["function"])
            func(flags, screens)

        elif screen_id == "man_jacob":
            func = eval(screens[screen_id]["function"])
            func(screens)

        elif screen_id == "find_path" and action == 1:
            func = eval(screens[screen_id]["function"])
            location_of_end = "Swamps: tried to find path"
        
        elif screen_id == "swamps":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screens, screen_id, flags, swamp_events, swamps_events_weights, action)
        
        elif screen_id == "swamps_path":
            func = eval(screens[screen_id]["function"])
            action = func(screens, flags, action)

        elif screen_id == "church_jacob":
            func = eval(screens[screen_id]["function"])
            func(screens)
        
        elif screen_id == "choose_guard":
            func = eval(screens[screen_id]["function"])
            func()
        
        elif screen_id == "bribe_guards":
            func = eval(screens[screen_id]["function"])
            func(state, flags)
        
        elif screen_id == "fight_guards":
            func = eval(screens[screen_id]["function"])
            func(screens, flags, action)
        
        elif screen_id == "in_tavern":
            func = eval(screens[screen_id]["function"])
            func(flags, screens)

        elif screen_id == "choose_bandit":
            func = eval(screens[screen_id]["function"])
            func()

        elif (screen_id == "attack" or screen_id == "spells" or screen_id == "fight"):
            func = eval(screens[screen_id]["function"])
            func()
        
        elif screen_id == "evade":
            func = eval(screens[screen_id]["function"])
            func()
        
        elif screen_id == "inventory":
            func = eval(screens[screen_id]["function"])
            func()
        
        elif screen_id == "church":
            func = eval(screens[screen_id]["function"]) 
            func(screens, flags, state, action, pay_for_rest)

        elif screen_id == "church_quest":
            func = eval(screens[screen_id]["function"])
            # TODO: Fix rest action
            pay_for_rest = func(screens, flags, inventory, action, pay_for_rest)

        elif screen_id == "sad_man":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(parameters)

        elif screen_id == "jacob_home" :
            func = eval(screens[screen_id]["function"])
            action = func(screens, flags, action)
        
        elif screen_id == "inside_jacob_house":
            func = eval(screens[screen_id]["function"])
            action = func(screens, flags, inventory, action)   

        elif screen_id == "you_got_drunk":
            func = eval(screens[screen_id]["function"])
            func(flags, state, screens)   

        elif screen_id == "statue":
            func = eval(screens[screen_id]["function"])
            func(screens, state, inventory, action)
       
        elif screen_id == "obelisk":
            func = eval(screens[screen_id]["function"])
            func(screens, state, spells, action)
       
        elif screen_id == "rusted_sword":
            func = eval(screens[screen_id]["function"])
            func(screens, state, inventory, action)
       
        elif screen_id == "purple_flowers_1":
            func = eval(screens[screen_id]["function"])
            func(screens, state, inventory, action)
        
        elif screen_id == "purple_flowers_2":
            func = eval(screens[screen_id]["function"])
            func(screens, state, inventory, action)
        
        elif screen_id == "solid_ground":
            func = eval(screens[screen_id]["function"])
            func(screens, state, action)

        elif screen_id == "creature":
            func = eval(screens[screen_id]["function"])
            func(screens, flags, state, action)
        
        elif screen_id == "goblin":
            func = eval(screens[screen_id]["function"])
            func(screens, flags, action)
        
        elif screen_id == "shadow_peaks_path":
            func = eval(screens[screen_id]["function"])
            screen_id, action = func(screens, screen_id, action, state, flags)
            
        elif screen_id == "negotiate_troll":
            func = eval(screens[screen_id]["function"])
            func(screens)
        
        elif screen_id == "ask_troll":
            func = eval(screens[screen_id]["function"])
            func(screens)
        
        elif screen_id == "pay_troll":
            func = eval(screens[screen_id]["function"])
            func(screens)
 
        elif screen_id == "offer_troll": 
            func = eval(screens[screen_id]["function"])
            func(screens, inventory, action)

        elif screen_id == "troll_golden_locket": 
            func = eval(screens[screen_id]["function"])
            func(screens)
        
        elif screen_id == "fight_troll":
            func = eval(screens[screen_id]["function"])
            func(screens, flags, action)

        elif screen_id == "church" or screen_id == "sad_man" or screen_id == "women":
            screens["village"]["text"] = '"Havencross" - a bustling settlement surrounded by fertile farmland and ' \
                                         'dotted with homes.'

        elif screen_id == "GAME_OVER":
            if screen_id == "GAME_OVER" and action != 0 and action - 1 < len(screens["GAME_OVER"]["options"]):
                if screens["GAME_OVER"]["options"][action - 1][0] == "Close Game":
                    exit()
            elif location_of_end == "Swamps: tried to find path":
                type_of_death = random.randint(1, 3)
                if type_of_death == 1:
                    screens["GAME_OVER"]["text"] = "You ignored the guards' warning and ventured into the swamp." \
                                                    "Your steps sink into the murky water as hidden predator pulls you under." \
                                                    "The last thing you feel is the sharp teeth of a swamp monster piercing your skin."
                elif type_of_death == 2:
                    screens["GAME_OVER"]["text"] = "Despite the warnings, you forge ahead. Then the ground gives way beneath your" \
                                                    "feet and you fall. Struggling to escape, you slowly sink deeper and deeper" \
                                                    "into the swamp's murky depths, never to be seen again."
                elif type_of_death == 3:
                    screens["GAME_OVER"]["text"] = "You ignore the guards' warning and try to find a way around. Suddenly you" \
                                                    "feel a sharp pain in your leg. Looking down, you see a venomous snake has" \
                                                    "bitten you. You try to drag yourself to safety, but it's too late. The" \
                                                    "snake's venom is too strong and you collapse into the murky water."
                location_of_end = ""
            elif location_of_end == "Tavern_bandits":
                screens["GAME_OVER"]["text"] = "You was defited by bandits"
                location_of_end = ""
            
            elif location_of_end == "mushrooms":
                screens["GAME_OVER"]["text"] = "As you consume the magic mushrooms, you feel the world" \
                    " around you transform into something fantastical and otherworldly. The colors of the" \
                    " forest become brighter, and the sounds of the animals become more vibrant. Your mind" \
                    " begins to wander, and you find yourself questioning the purpose of your quest. You" \
                    " begin to feel that perhaps it is all meaningless, and that there is more to life than" \
                    " chasing after some grand goal. In this altered state, you decide to abandon your quest" \
                    " and instead spend your days exploring the natural wonders of the forest, living in the" \
                    " present moment and enjoying the simple pleasures of life."
                location_of_end = ""
        
# Main game loop
global_running = True
while global_running:
    if screen_id in screens:
        watch_screen = screens[screen_id]
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global_running = False
        elif event.type == pygame.KEYDOWN:
            # A key was pressed
            if event.key == pygame.K_ESCAPE and running and flags["inventory_open"]:
                # The Esc key was pressed, exit the game
                screen_id = inventory_location
                flags["inventory_open"] = False
            elif event.key == pygame.K_ESCAPE and running and (screen_id == "buy" or screen_id == "sell"):
                screen_id = "store"
            elif event.key == pygame.K_SPACE:
                # The Space key was pressed, do something
                running = True
            elif event.key == pygame.K_1:
                action = 1
                print("Key 1 pressed")
            elif event.key == pygame.K_2:
                action = 2
                print("Key 2 pressed")
            elif event.key == pygame.K_3:
                action = 3
                print("Key 3 pressed")
            elif event.key == pygame.K_4:
                action = 4
                print("Key 4 pressed")
            elif event.key == pygame.K_5:
                action = 5
                print("Key 5 pressed")
            elif event.key == pygame.K_6:
                action = 6
                print("Key 6 pressed")
            elif event.key == pygame.K_7:
                action = 7
                print("Key 7 pressed")
            elif event.key == pygame.K_8:
                action = 8
                print("Key 8 pressed")
            elif event.key == pygame.K_9:
                action = 9
                print("Key 9 pressed")
            elif event.key == pygame.K_m and running and (screen_id == "village" or screen_id == "store" or
                                            screen_id == "forest" or screen_id == "swamps_path"):
                location = screen_id
                screen_id = "move"
            elif event.key == pygame.K_m and running and screen_id == "shadow_peaks_path":
                screen_id = "forest"
            elif event.key == pygame.K_i and running and screen_id != "inventory"\
                        and screen_id != "sell" and screen_id != "buy":
                inventory_location = screen_id
                screen_id = "inventory"
                tip_text = "To close an inventory press ' Esc '" 
                flags["inventory_open"] = True

    if running:
        # Update game state
        # Global parameters that passes into fighting functions
        parameters = {"state": state, 
                "inventory": inventory,
                "screens": screens,
                "screen_id": screen_id,
                "flags": flags,
                "action": action,
                "location_to_move": location_to_move
                }

        processingEvents()
        screen_id = check_mana_health_gold(screen_id)
        action = changeScreen(action)
       
        # Blit the background image onto the screen
        screen.blit(background, (0, 0))
        # Draw to the screen
        showScreen(screen, screen_font, options_font, tip_text)
        showHealth()
        showInventory() 
        showSpells()
    else:
        screen.blit(background, (0, 0))

    pygame.display.flip()
    # Add drawing code here

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(frame_rate)
    print(clock.tick(frame_rate), "action = ", action)
    

# Clean up
pygame.quit()
