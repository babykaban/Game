import random

def find_equipped_item_index_inventory(inventory):
    count = 0
    for item in inventory:
        if item["status"][0] == "equipped":
            break
        count += 1
    print(count)
    return count

def roll():
    return random.randint(0, 100)

def find_specific_item_status(key, inventory):
    indexes = []
    count = 0
    for item in inventory:
        if item["status"][1] == key:
            indexes.append(count)
        count += 1
    if len(indexes) > 0:
        return indexes, True
    else:
        return indexes, False

def find_index_in_sell_prices(key, items_sell_prices):
    index = 0
    for item in items_sell_prices:
        if item["item"] == key:
            break
        index += 1
    return index

def compute_chances(weights):
    events_chances = []
    for weight in weights:
         events_chances.append(round(weight / (sum(weights) - weight), 2))
    return events_chances

def choose_random_event(events, events_weights):
    event = random.choices(events, compute_chances(events_weights))
    return event

def find_object_index_array(key, array):
    count = 0
    for obj in array:
        if obj == key:
            break
        count += 1
    return count

def del_all_options(options):
    while len(options) != 0:
        del options[0]

def del_all_options_for_key(key, options):
    count = 0
    for opt in options:
        if opt[1] == key:
            del options[count]
        count += 1
        
def find_option(key, options):
    i = 0
    for opt in options:
        if opt[1] == key:
            break
        i += 1
    return options[i], i

def check_if_option_in_screen(key, options):
    for opt in options:
        if opt[1] == key:
            return True
    return False
    
def del_option(key, options):
    _, i = find_option(key, options)
    del options[i]

def find_item_index_inventory(key, inventory):
    count = 0
    for item in inventory:
        if item["name"] == key:
            break
        count += 1
    return count
    

def check_if_item_in_inventory(key, inventory):
    for item in inventory:
        if item["name"] == key:
            return True
    return False

def check_if_object_in_array(key, array):
    for object in array:
        if object == key:
            return True
    return False

def find_spell(key, spells):
    count = 0
    for spell in spells:
        if spell["name"] == key:
            break
        count += 1
    return count

def check_mana(mana_needed, state):
    if mana_needed <= state["mana"]:
        return True
    else:
        return False