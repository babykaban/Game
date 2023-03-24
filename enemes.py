# =========================== ENEMES ========================= #
from fights import loot_bandit, loot_creature, loot_goblin, loot_guard, loot_troll, \
    loot_bear, loot_wolf

# Bandits
bandit_1 = {
            # Enemy stats
            "name": "Bandit_1",
            "health": 20,
            "damage": [10, 20],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 30,
            "spell_miss_chance": 15,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 100,
            "evade": 20,
            "magic_shield": 95,
            "parry_damage": 0.3,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_bandit}

bandit_2 = {
            # Enemy stats
            "name": "Bandit_2",
            "health": 20,
            "damage": [10, 20],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 30,
            "spell_miss_chance": 15,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 100,
            "evade": 20,
            "magic_shield": 95,
            "parry_damage": 0.3,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_bandit}


bandit_leader = {
            # Enemy stats
            "name": "Bandit_Leader",
            "health": 40,
            "damage": [10, 20],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 30,
            "spell_miss_chance": 15,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 100,
            "evade": 20,
            "magic_shield": 95,
            "parry_damage": 0.3,
            "magic_shield_damage": 0,
            
            # Function
            "loot": loot_bandit}

bandits = [bandit_1, bandit_2, bandit_leader]
bandit_enemes = len(bandits)
# End Bandits

# Guards
guard_1 = {
            # Enemy stats
            "name": "Guard_1",
            "health": 20,
            "damage": [20, 30],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1.5,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 0.5,
            "axe_damage": 1.2,

            # Evade
            "parry": 100,
            "evade": 90,
            "magic_shield": 100,
            "parry_damage": 0.5,
            "magic_shield_damage": 0.2,
            
            # Function
            "loot": loot_guard}

guard_2 = {
            # Enemy stats
            "name": "Guard_2",
            "health": 20,
            "damage": [20, 30],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1.5,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 0.5,
            "axe_damage": 1.2,

            # Evade
            "parry": 100,
            "evade": 90,
            "magic_shield": 100,
            "parry_damage": 0.5,
            "magic_shield_damage": 0.2,
            
            # Function
            "loot": loot_guard}

guard_3 = {
            # Enemy stats
            "name": "Guard_3",
            "health": 20,
            "damage": [20, 30],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1.5,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 0.5,
            "axe_damage": 1.2,

            # Evade
            "parry": 100,
            "evade": 90,
            "magic_shield": 100,
            "parry_damage": 0.5,
            "magic_shield_damage": 0.2,
            
            # Function
            "loot": loot_guard}

guards = [guard_1, guard_2, guard_3]
guard_enemes = len(guards)
# End Guards


# Creature
creature = {
            # Enemy stats
            "name": "Croctopus",
            "health": 20,
            "damage": [5, 10],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 3,
            
            # Attack
            "weapon_damage": 0.8,
            "spell_damage": 1.2,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 20,
            "evade": 80,
            "magic_shield": 60,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_creature}

# End Creature 

# Goblin
goblin = {
            # Enemy stats
            "name": "Goblin",
            "health": 60,
            "damage": [20, 30],
            "vulnerability": "fire",
            "vulnerability_factor": 2,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 30,
            "spell_miss_chance": 15,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 80,
            "evade": 10,
            "magic_shield": 80,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_goblin}
# End Goblin

# Troll
troll = {
            # Enemy stats
            "name": "Troll",
            "health": 500,
            "damage": [30, 50],
            "vulnerability": "fire",
            "vulnerability_factor": 4,
            "number": 1,
            
            # Attack
            "weapon_damage": 0.6,
            "spell_damage": 1.2,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 100,
            "evade": 60,
            "magic_shield": 100,
            "parry_damage": 0.9,
            "magic_shield_damage": 0.3,
            
            # Function
            "loot": loot_troll}

# End Troll

# Bear
bear_enemy = {
            # Enemy stats
            "name": "Bear",
            "health": 50,
            "damage": [20, 30],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 0,
            "evade": 70,
            "magic_shield": 80,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_bear}
# End Bear

# Wolves
wolf_enemy_1 = {
            # Enemy stats
            "name": "Black wolf",
            "health": 15,
            "damage": [10, 10],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 40,
            "evade": 30,
            "magic_shield": 95,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_wolf}

wolf_enemy_2 = {
            # Enemy stats
            "name": "Grey wolf",
            "health": 15,
            "damage": [10, 10],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 40,
            "evade": 30,
            "magic_shield": 95,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_wolf}

wolf_enemy_3 = {
            # Enemy stats
            "name": "Brown wolf",
            "health": 15,
            "damage": [10, 10],
            "vulnerability": "",
            "vulnerability_factor": 0,
            "number": 1,
            
            # Attack
            "weapon_damage": 1,
            "spell_damage": 1,
            "weapon_miss_chance": 0,
            "spell_miss_chance": 0,
            "sword_damage": 1,
            "axe_damage": 1,

            # Evade
            "parry": 40,
            "evade": 30,
            "magic_shield": 95,
            "parry_damage": 1,
            "magic_shield_damage": 1,
            
            # Function
            "loot": loot_wolf}

wolves = [wolf_enemy_1, wolf_enemy_2, wolf_enemy_3]
wolves_enemes = len(wolves)

# End Wolves
# ==================== END_ENEMES ===================== #