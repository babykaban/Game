import json

screens = {
    "intro": {"text": "You have arrived in the village of Havencross looking for a magical stone - the Heart of "
                      "Elders. You believe the artifact is hidden in the nearby mountains known as the Shadow "
                      "Peaks. You hope to use the artifact's power to create a cure for the deadly sickness that "
                      "claimed the lives of your family. You have faced many challenges on the journey, "
                      "but you remain determined in your search.",

              "options": [("Go to the Havencross", "village"),
                          ("Go to the Gorn's Shop", "store"),
                          ("Go to the Whispering Woods", "forest"),
                          ("Go to the Drunken Dragon tavern", "tavern")]},
    "move": {"text": "Choose location to move",
             "options": []},
    "inventory": {"text": "Items:",
                  "options": [],
                  "function": "inventory_screen"}, # Function in str

    # ========================================VILLAGE================================================================= #
    "village": {"text": "You walk into the village on a sunny morning and observe the bustle of activity around you. "
                        "You see a man sitting on a bench, looking sad and lost in thought. A  group of women are "
                        "chattering near the well, while in the distance you can see the towering spire of a church.",

                "options": [("Visit the church", "church"),
                            ("Approach the sad man", "sad_man"),
                            ("Approach a group of women", "women")],
                "function": "village"}, # Function in str

    "church": {"text": 'A monk greets you with a nod and a warm smile. \\p\n "Good morning, traveler! May I offer you a '
                       'moment of respite and healing at our church? For a small fee, of course."',
               "options": [("Rest and heal (20 Gold)", "church"),
                           ("Ask if they need help with anything", "church_quest"),
                           ("Leave", "village")],
                "function": "church"}, # Function in str
    "church_jacob": {"text": '"Jacob, you say? I do not hold kindly to that man, he rarely shows his face at the '
                             "church. And as for where he might be, I haven't seen him in weeks. Some say he spends "
                             'his days locked up in his cottage, but I would not know for certain."',
                     "options": [("* . . . *", "church")],
                     "function": "church_jacob"}, # Function in str

    "sad_man": {"text": 'You see a young man sitting with his head in his hands. He looks up as you approach and you'
                        'can see the tears in his eyes. You ask what happened. \\p\n"My family heirloom, a necklace passed '
                        'down from generation to generation, was stolen by a goblin! I feel like a part of me is gone,'
                        " and I don'"'t know what to do!"',
                "options": [("Leave him be", "village")],
                "function": "sad_man"}, # Function in str

    "man_jacob": {"text": "I'm sorry, I don't know anyone by that name.",
                  "options": [("* . . . *", "sad_man")],
                  "function": "man_jacob"}, # Function in str

    "women": {"text": "* . . . *",
              "options": [("Ask about the area", "women_area"),
                          ("Ask about their problems", "problems"),
                          ("Leave", "village")]},

    "women_area": {"text": "Women suggest visiting the local tavern, where one can find travelers and locals alike. "
                           "They mention the nearby forest, filled with an abundance of herbs and wildlife. "
                           "They warn you about the swamp, home to many dangerous creatures.One of them tells "
                           "you about a Troll that lives under the bridge on the way to the mountains. The Troll is a "
                           "grumpy and greedy creature, who demands toll from anyone who wants to cross the bridge.",
                   "options": [("* . . . *", "women")]},
    "women_jacob": {"text": '"Jacob is a strange man, always talking about legends and tales from the past. '
                            "He's not well-liked you know. He lives in the old hut at the edge of the village. Just "
                            "follow the path that leads towards the forest and you can't miss it.",
                    "options": [("*you know where Jacob lives*", "women")],
                    "function": "women_jacob"}, # Function in str

    "problems": {"text": "Women mention guards stationed on the path to the swamp, who they say have been causing "
                         "trouble for travelers. Also they complain about mischievous goblin who has been stealing "
                         "things from the villagers. One girl warns you about the griffin that resides in the "
                         "mountains, known to attack travelers who venture too close to its nest. Others giggle to "
                         "that.",
                 "options": [("* . . . *", "women")]},

    "church_quest": {"text": '"As a matter of fact, we are in need of herbs that we use to prepare our potions. They '
                             'grow in the forest, and if you could bring some to us, we would be most grateful."',
                     "options": [("*gather herbs in the forest, bring "
                                  "here \\p\nto get discount and healing potions*", "church")],
                     "function": "church_quest"}, # Function in str
    "jacob_home": {"text": "Jacob's home is a small, run-down cottage located on the outskirts of the village. It "
                           "is surrounded by overgrown shrubs and trees, and the roof is partially caved in.",
                   "options": [("Knock on the door", "jacob_home"),
                               ("Yell Jacob's name", "jacob_home")],
                    "function": "jacob_home"}, # Function in str
    "inside_jacob_house": {"text": "The door is not locked. You see that the inside of the house is a mess. Furniture"
                                   " is overturned and there's a trail of broken objects leading to the back room. You"
                                   " call out Jacob's name again, but there's still no response. You decide to "
                                   "investigate further to see if Jacob is okay.",
                           "options": [("Look around", "inside_jacob_house")],
                           "function": "inside_jacob_house"}, # Function in str

    # ======================================END_VILLAGE=============================================================== #

    # ==========================================BANDITS=============================================================== #

    "fight_bandits": {"text": "You step out of the Drunken Dragon tavern, and the three shady figures you saw earlier "
                              "move to surround you. The tall bandit leader steps forward and demands your coin "
                              "purse, but you are ready to defend yourself.",
                      "options": [("Fight", "choose_bandit")]},
    
    "you_got_drunk": {"text": "You stumble out of the Drunken Dragon tavern, and the three shady figures you saw" 
                                "earlier move to surround you. The tall bandit leader steps forward and demands" 
                                "your coin purse, but you are in no shape to fight. The alcohol has dulled your" 
                                "senses, and you can barely even stand up straight. You feel something heavy hit" 
                                "your head, and fall into darkness. You wake up in the morning with a terrible headache." 
                                "The bandits took all your gold, and there is no sign of them.",
                    "options": [("Continue", "tavern")],
                    "function": "you_got_drunk"}, # Function in str

    "fight": {"text": "oooopis",
              "options": [("Attack with your weapon", "evade"),
                          ("Attack with spell", "spells")],
              "function": "attack_and_spell"}, # Function in str

    "attack": {"text": "",
                     "options": [("Attack with your weapon", "evade"),
                                 ("Attack with spell", "spells")],
                     "function": "attack_and_spell"}, # Function in str

    "spells": {"text": "Choose spell",
               "options": [],
               "function": "attack_and_spell"}, # Function in str

    "evade": {"text": "",
                    "options": [("Attempt to evade", "evade"),
                                ("Try to parry", "evade"),
                                ("Block with magic shield", "evade")],
                    "function": "evade"}, # Function in str
    "loot": {"text": "",
             "options": [("Move on", "")]},
    
    "choose_bandit": {"text": "Choose bandit to attack",
                      "options": [("Bandit_1", "attack"),
                                  ("Bandit_2", "attack"),
                                  ("Bandit_Leader", "attack")],
                      "function": "choose_bandit"}, # Function in str
    # =========================================END_BANDITS============================================================ #

    # ========================================TAVERN================================================================== #
    "tavern": {"text": "As you approached the Drunken Dragon tavern, you felt a sudden sense of unease upon seeing "
                       "three shady figures. The tall man with a thick beard and a sly grin and the massive brute "
                       "with bulging "
                       "muscles exuded a dangerous aura. You took a deep breath and entered the tavern, ready for any "
                       "danger that may come his way. ",

               "options": [("Step into the tavern", "in_tavern"),
                           ("Go to the Gorn's Shop", "store"),
                           ("Go to the Havencross", "village"),
                           ("Go to the Whispering Woods", "forest")]},
    "in_tavern": {
        "text": "You step into the Drunken Dragon tavern. The innkeeper greets you from behind the bar with a smile. "
                "In the center of the room, a group of rowdy patrons are gathered, shouting and laughing as"
                "they down their drinks. You also spot an old woman sitting alone at a table in the corner.",
        "options": [("Talk to the innkeeper", "innkeeper"),
                    ("Join the party", "party"),
                    ("Approach an old woman", "old_woman"),
                    ("Leave", "tavern")],
        "function": "in_tavern"}, # Function in str

    "innkeeper": {"text": "You approach the innkeeper."
                          '"What can I get for you today?" he asks, his eyes twinkling.'
                          "You ask innkeeper if he heard about the Heart of Elders."
                          '"I might. What is it worth to you?"',
                  "options": [("Pay 10 gold.", "innkeeper_lose_10_gold"),
                              ("Pay 30 gold.", "innkeeper_lose_30_gold"),
                              ("Buy beer", "innkeeper"),
                              ("Walk away.", "in_tavern")],
                 "function": "innkeeper"}, # Function in str

    "innkeeper_lose_10_gold": {
        "text": '"Ha! You really think a few coins will buy you knowledge that even the greatest sages have failed to '
                'uncover?"'
                "Dream on, traveler. If you wanxxt to know about the Heart of Elders, you'll have to look elsewhere.",
        "options": [("*the innkeeper doesn't want to talk to you anymore*", "in_tavern")],
        "function": "innkeeper_lose_10_gold"}, # Function in str

    "innkeeper_lose_30_gold": {
        "text": '"Ah, you want to know about the Heart of Elders, are you? Well, let me tell you a story. It was '
                'created by the first wizards, you see, to bring balance to the world. So powerful was it that they '
                'decided to hide it away, deep within the mountains, to protect it from falling into the wrong hands. '
                'Many have searched for it, but few have returned to tell the tale."',
        "options": [("*you hasn't learned anything new*", "in_tavern")],
        "function": "innkeeper_lose_30_gold"}, # Function in str

    "party": {"text": "You approach the group of merrymakers, and they warmly welcome you to join their festivities. "
                      "As you down mug after mug of ale, you find yourself losing track of time and becoming more and "
                      "more inebriated. Eventually, you can barely stand and stumble out of the tavern, "
                      "swaying unsteadily on your feet as you make your way back to your room.",
              "options": [("*you've got drunk*", "in_tavern")],
              "function": "party"}, # Function in str

    "old_woman": {"text": 'You sit at the table with the old woman, you hear her muttering to herself. You ask her if '
                          'she knows anything about the Heart of Elders. She looks up at you and grumps "That old '
                          "man, Jacob, is the one you should talk to. He talks about it all the time. I'd rather "
                          'listen to the howling wind than hear him go on and on about it."',
                  "options": [("*remember that you should find Jacob*", "in_tavern")],
                  "function": "old_woman"}, # Function in str
    # ==========================================END_TAVERN============================================================ #

    # ==============================================SWAMPS============================================================ #
    "swamps": {"text": '"The Stinky Swamps" - a murky expanse of stagnant water and twisted trees,'
                                'home to dangerous creatures and dark magic.',
                "options": [("Explore the swamp", "swamps"),
                            ("Move back to the Whispering Woods", "forest")], 
                "function": "swamps"}, # Function in str

    "swamps_path": {"text": "As you approach the path leading to the swamps, you're stopped "
                            "by three guards. They stand in front of the entrance, blocking "
                            "your way. One of the guards steps forward. \\p\n"
                            '"No one is allowed to enter the swamps.'" It's too dangerous."
                            " \\p\nYou explain that you can handle yourself. The guards exchange"
                            " skeptical glances, sizing you up. \\p\n"'"Even if that is true we can'
                            "'t make any exceptions. No one is allowed in."'"',
               "options": [("Continue", "swamps_path")],
               "function": "swamps_path"}, # Function in str
    
    "find_path": {"text": "As you consider making a detour around the guards, one of them speaks up." \
                            "Don't even think about it. That swamp is treacherous. The ground is unstable," \
                            "and there are creatures in there that would make a meal out of you in a heartbeat." \
                            "Trust me, you don't want to go that way." \
                            "The guard shudders at the thought of the dangers in the swamp," \
                            "and the other two nod in agreement.",
                    "options": [("Ignore the warning and go around", "GAME_OVER"),
                                ("Heed the advice", "swamps_path")]},
    
    "bribe_guards": {"text": "You reach into your pocket and pull out a pouch of coins, offering it to the guards." 
                                "They take a look at each other, then back at you, considering the offer. \\p\n"
                                '"'"Well, we could make an exception for the right price. But you're taking your own risk, adventurer."
                            "They each take a coin from the pouch and step aside, letting you pass.",
                     "options": [("Move on", "swamps")],
                     "function": "bribe_guards"}, # Function in str

    "fight_guards": {"text": "",
                     "options": [("Fight", "choose_guard")],
                     "function": "fight_guards"}, # Function in str

    "choose_guard": {"text": "Choose guard to attack",
                     "options": [("Guard_1", "attack"),
                                  ("Guard_2", "attack"),
                                  ("Guard_3", "attack")],
                     "function": "choose_guard"}, # Function in str
    #Swamp events
    "event": {"text": "",
                "options": [("Countinue", "swamps")]},

    "statue": {"text": "You stumble upon a clearing in the swamp and find a"
                        " strange stone statue. As you examine it, you notice"
                        " that the statue is imbued with magical energy.",
                "options": [("Cast a spell on the statue.", "event"),
                            ("Investigate the statue more closely.", "event"),
                            ("Leave the statue alone.", "event")],
                "function": "statue"}, # Function in str
   
    "obelisk": {"text": "You've found a mysterious obelisk, its surface covered"
                        " in glowing runes. As you approach, you feel a strange"
                        " energy emanating from the stone.",
                "options": [("Touch the obelisk.", "event"),
                            ("Examine the obelisk.", "event"),
                            ("Ignore the obelisk.", "swamps")],
                "function": "obelisk"}, # Function in str
   
    "rusted_sword": {"text": "You come across a rusted sword half-buried in the mud."
                            " As you pull it free, the blade gleams in the sunlight.",
                        "options": [("Pick up the sword.", "event"),
                                    ("Attempt to clean the sword before picking it up.", "event"),
                                    ("Move on", "swamps")],
                        "function": "rusted_sword"}, # Function in str
    
    "purple_flowers_1": {"text": "As you move through the swamp, you notice some beautiful"
                                " purple flowers growing along the path. Suddenly, you hear"
                                " a faint hissing noise coming from the plants.",
                            "options": [("Pick some flowers.", "event"),
                                        ("Attack the plants.", "event"),
                                        ("Move on", "swamps")],
                            "function": "purple_flowers_1"}, # Function in str
    
    "purple_flowers_2": {"text": "As you move through the swamp, you notice some beautiful"
                                " purple flowers growing along the path. Suddenly, you hear"
                                " a faint hissing noise coming from the plants.",
                            "options": [("Pick some flowers.", "event"),
                                        ("Attack the plants.", "event"),
                                        ("Move on", "swamps")],
                            "function": "purple_flowers_2"}, # Function in str
    
    "solid_ground": {"text": "You step on a patch of seemingly solid ground, but as you put"
                            " your full weight on it, you suddenly start sinking in quicksand."
                            " You struggle to free yourself but it's no use - you're stuck.",
                        "options": [("Attempt to free yourself by force.", "event"),
                                    ("Cast a spell to create solid ground under your feet.", "swamps")],
                        "function": "solid_ground"}, # Function in str
    
    "creature": {"text": "You hear a loud splashing noise and a giant, slimy creature emerges from the swamp."
                        " It looks like a cross between an octopus and a crocodile.",
                    "options": [("Attack the creature.", "fight"),
                                ("Use a spell to distract the creature.", "event")],
                    "function": "creature_enemy"}, # Function in str

    "goblin": {"text": 'You hear a soft rustle behind you and turn to see a small green goblin clutching a shiny'
                        ' object. "This trinket is mine now!" he shouts, brandishing a rusty dagger.',
                    "options": [("Attack the goblin", "fight")],
                    "function": "goblin_enemy"}, # Function in str
    # ===============================================END_SWAMPS======================================================= #

    # ================================================FOREST========================================================== #
    "forest": {"text": "As you enter the Forest, the sound of rustling leaves and chirping birds fills your ears." 
                        "The sunlight filtering through the trees creates a dappled pattern on the forest floor.",
               "options": [("Explore the forest", "forest"),
                           ('Go to the "The Shadow Peaks" mountains', "shadow_peaks_path")],
               "function": "forest"}, # Function in str
    "villagers": {"text": "You come across a group of villagers who are gathering berries."
                          " They offer you some berries, and also warn you of a dangerous"
                          " bear that has been spotted in the area.",
                  "options": [("Accept the berries and continue on your way.", "berries"),
                              ("Ask the villagers for more information about the bear.", "bear_warnning"),
                              ("Offer to help the villagers gather berries " \
                                "in exchange for information on the bear. (20 mana)", "villagers")],
                  "function": "villagers"}, # Function in str
    
    "berries": {"text": "You thank the villagers and take the berries with you. \\p\n"
                        '+ "Berries"',
                "options": [("Move on", "forest")]},
    
    "bear_warnning": {"text": "The villagers tell you that the bear is known to be"
                                " aggressive and advise you to stay away from it.",
                      "options": [("Move on", "forest")]},
    
    "help_villagers": {"text": "You spend some time gathering berries with the villagers, "
                                "and they tell you about a nearby cave where the bear is rumored to live. \\p\n"
                                '-20 mana \\p\n + "Berries"',
                       "options": [("Countinue", "forest")]},
    
    "herbs": {"text": "As you wander through the forest, you notice a patch of"
                        " vibrant green leaves growing by the base of a tree.",
              "options": [("Collect the leaves.", "collect_herbs"),
                          ("Leave the leaves alone.", "forest")],
              "function": "herbs"}, # Function in str
    
    "collect_herbs": {"text": "You carefully gather the leaves and place them in your pouch. \\p\n"
                              '+1 "Herbs" (5 gold)',
                      "options": [("Move on", "forest")]},
    
    "boar": {"text": "As you wander through the forest, you spot a wild boar rustling in the bushes.",
             "options": [("Hunt the boar.", "boar"),
                         ("Leave the boar alone.", "forest")],
             "function": "boar"}, # Function in str
    
    "success_hunt_boar": {"text": "You successfully hunt the boar and collect some meat and leather. \\p\n"
                                  '+ "Boar meat" (10 gold) \\p\n + "Boar leather" (10 gold)',
                          "options": [("Move on", "forest")]},
    
    "failure_hunt_boar": {"text": "The boar senses your presence and charges at you, forcing you to retreat.",
                          "options": [("Move on", "forest")]},
    
    "travelers": {"text": "You come across a small clearing in the forest,"
                          " and notice a group of people gathered around a campfire.",
                  "options": [("Approach the group.", "travelers"),
                              ("Move on", "forest")],
                  "function": "travelers"}, # Function in str

    "good_travelers": {"text": "As you approach, the people welcome you warmly and invite "
                                "you to join them by the fire. They share their food and "
                                "stories with you, and you feel a sense of belonging. \\p\n"
                                "Restore +20 health and +20 mana",
                       "options": [("Countinue", "forest")]},
    
    "bad_travelers": {"text": "You notice that they are heavily armed and don't seem friendly. "
                              "But it's too late now. They demand that you hand over all "
                              "your valuables, revealing themselves to be bandits. \\p\nLose all gold",
                      "options": [("Countinue", "forest")]},
    
    "mushrooms": {"text": "As you wander through the forest, your eyes catch sight of some"
                          " peculiar-looking mushrooms growing on the base of a tree.",
                  "options": [("Pick up and eat the mushrooms.", "mushrooms"),
                              ("Don't touch the mushrooms.", "forest")],
                  "function": "mushrooms"}, # Function in str
    
    "stone": {"text": "As you wander through the forest, you stumble upon a clearing in"
                      " which stands a circle of ancient stones. You feel a strange energy"
                      " emanating from the center of the circle.",
              "options": [("Investigate the stones", "investigate_stone"),
                          ("Meditate in the circle", "meditate"),
                          ("Wait for the druids to return to the circle.", "stone"),
                          ("Leave", "forest")],
              "function": "stone"}, # Function in str
    
    "investigate_stone": {"text": "You notice that the stones are covered in intricate symbols"
                                  " that you don't recognize. However, you feel a strange pull"
                                  " towards them and a sense of peace washes over you.",
                          "options": [("*wolves and bear attack will never happen*", "forest")]},
    
    "meditate": {"text": "You feel a strong connection to nature. You are able to hear the"
                         " sounds of the forest more clearly and feel the breeze on your skin."
                         " \\p\nRestore +40 health and full mana, gain +5 max mana",
                 "options": [("Move on", "forest")]},
    
    "wait_druinds": {"text": "The forest grows darker and the night turns cold."
                            " You eventually give up waiting and decide to leave. \\p\n-20 mana",
                    "options": [("Leave", "forest")]},

    "bear": {"text": "As you wander deeper into the forest, a sudden rustling catches"
                            " your attention. Before you can react, a massive bear charges out"
                            " of the underbrush and barrels toward you.",
                    "options": [("Fight bear", "fight"),
                                ("Run away from the bear. (50 mana)", "bear")],
                    "function": "bear"}, # Function in str
     
    "run_away_bear": {"text": "You turn and flee as fast as you can, hoping to outpace the bear."
                              " Fortunately, at some point the bear stopped chasing you.",
                      "options": [("Countinue", "forest")]},

    "bear_lair": {"text": "As you push through the underbrush, you come across a small cave entrance."
                          " Inside, you spot the bear's lair and the glint of something shiny on the floor.",
                  "options": [("Search the lair", "bear_lair"),
                              ("Leave", "forest")],
                  "function": "bear_lair"}, # Function in str
    
    "ring": {"text": "As you rummage through the bear's stash, you spot a glint of silver,"
                     " and pick up a beautiful ring."
                     ' \\p\n+ "Silver ring" (30 gold)',
             "options": [("Move on", "bear_lair")]},
    
    "coat": {"text": "You find a well-worn coat among the bear's belongings, it's made of fur and looks warm."
                     ' \\p\n+ "Warm coat" (armor, -5% physical damage, 10 gold)',
             "options": [("Move on", "bear_lair")]},
    
    "gold_1": {"text": "You discover a small pouch containing various coins and gems."
                        " \\p\n+25 gold",
             "options": [("Move on", "bear_lair")]},
    
    "lair_herbs": {"text": "You come across a stash of rare herbs, carefully arranged and preserved."
                           ' \\p\n +3 "Herbs"',
             "options": [("Move on", "bear_lair")]},
    
    "pendant": {"text": "You notice a faint glow coming from a small pendant in the bear's"
                        " lair, it's unlike anything you've seen before."
                        ' \\p\n+ "Magic pendant" (-10% all enemy damage)',
             "options": [("Move on", "bear_lair")]},
    
    "backpack": {"text": "You discover an old backpack that appears to have belonged"
                         " to a traveler, still in good condition despite being weathered."
                         ' \\p\n+ "Old backpack" (15 gold)',
             "options": [("Move on", "bear_lair")]},
    
    "tools": {"text": "Hidden in a corner, you find a set of tools that could be useful for crafting or repairing."
                      ' \\p\n+ "Crafting tools" (30 gold)',
             "options": [("Move on", "bear_lair")]},

    "dagger": {"text": "Your eyes catch a glimmer of metal beneath a pile of leaves,"
                       " revealing a rusted but sturdy dagger."
                       ' \\p\n+ "Rusty dagger" (8 damage, 10 gold)',
             "options": [("Move on", "bear_lair")]},
    
    "gold_2": {"text": "You uncover a small box filled with various trinkets,"
                       " including a silver hairpin and a polished stone.  \\p\n+25 gold",
             "options": [("Move on", "bear_lair")]},
    
    "lair_key": {"text": "As you inspect a pile of rocks, you discover a small key and decide to take it."
                         ' \\p\n+ "A key from the bear''s lair"',
             "options": [("Move on", "bear_lair")]},
    
    "wolves": {"text": "You are walking through the forest when you hear a low growl."
                       " Looking around, you see a pack of wolves staring at you,"
                       " their eyes glinting in the moonlight.",
               "options": [("Fight the wolves.", "choose_wolf"),
                           ("Try to runaway.", "run_away_wolves"),
                           ('Use a "Magic flute" (20 mana)', "use_magic_wolves")],
               "function": "wolves_func"}, # Function in str

    "choose_wolf": {"text": "Choose wolf to attack",
                      "options": [("Black wolf", "attack"),
                                  ("Grey wolf", "attack"),
                                  ("Brown wolf", "attack")],
                      "function": "choose_wolf"}, # Function in str
    
    "use_magic_wolves": {"text": "You cast a spell and the wolves become docile and friendly, "
                                 "licking your hand and wagging their tails. After a few moments,"
                                 " they trot off back into the woods, leaving you unharmed.",
                         "options": [("Move on", "forest")]},

    "run_away_wolves": {"text": "",
                        "options": [("Countinue", "forest")]},
    
    "throw_meat": {"text": "You rummage through your pack and find some meat. You throw it to"
                           " the wolves and they eagerly pounce on it, giving you a "
                           "chance to slip away unnoticed.",
                   "options": [("Countinue", "forest")]},
    # ===================================================END_FOREST=================================================== #
    
    # ===================================================SHADOW_PEAKS=================================================== #
    "shadow_peaks_path": {"text": "You make your way from the forest to the mountains and come across a river." 
                                    "You approach the bridge and a loud voice booms out: \\p\n"
                                    '"Who goes? Stop! No passes without pay! 500 gold!" \\p\n'
                                    "A massive, ugly troll emerges from beneath the bridge, "
                                    "his eyes fixed on you with a greedy glint.",
                          "options": [("Try to negotiate with the Troll.", "negotiate_troll"),
                                      ("Ask when was the last time he let someone to cross", "ask_troll"),
                                      ("Pay 500 gold", "shadow_peaks_path"),
                                      ("Offer the Troll something else of value instead of money.", "offer_troll"),
                                      ("Attack the Troll", "fight_troll")],
                          "function": "shadow_peaks_path"}, # Function in str
    
    "negotiate_troll": {"text": "The Troll listens to your proposal and considers it for" 
                                "a moment, but then shakes its head. \\p\n"
                                '"No deal. Troll needs gold, not promises." \\p\n'
                                "It then takes a step closer, brandishing its club menacingly."
                                '"Pay up, or turn back."',
                        "options": [("Continue", "shadow_peaks_path")],
                        "function": "negotiate_troll"}, # Function in str
    
    "ask_troll": {"text": "The Troll scratches his head and looks thoughtful for a moment. \\p\n"
                          '"Hmm, I can'"'"'t member. But you pay to cross!"',
                  "options": [("Countinue", "shadow_peaks_path")],
                  "function": "ask_troll"}, # Function in str
    
    "pay_troll": {"text": '"You may go." He steps aside and lets you cross the bridge.',
                  "options": [("Move on", "shadow_peaks")],
                  "function": "pay_troll"}, # Function in str
    
    "offer_troll": {"text": "",
                    "options": [],
                    "function": "offer_troll"}, # Function in str
    
    "troll_golden_locket": {"text": "The Troll's eyes light up with greed "
                                    "as he snatches the golden locket from your hand. \\p\n"
                                    '"A fine shiny goodie," he says, examining the locket closely. \\p\n'
                                    '"You may go." He steps aside and lets you cross'
                                    ' the bridge, grumbling to himself as you walk.',
                            "options": [("Move on", "shadow_peaks")],
                            "function": "troll_golden_locket"}, # Function in str
    
    "equipment_troll": {"text": "He takes the item from you, and then tosses it over"
                                " his shoulder while still blocking your path. \\p\n"
                                '"No gold, no pass." \\p\n'
                                "You feel a sinking feeling in your stomach as you realize this was futile.",
                        "options": [("Countinue", "offer_troll")]}, 
    
    "else_items_troll": {"text": '"NO!"',
                         "options": [("Countinue", "offer_troll")]},
    
    "fight_troll": {"text": " adasdawdasd",
                    "options": [("Fight", "fight")],
                    "function": "troll_enemy"}, # Function in str
     
    "shadow_peaks": {"text": "adasdasd",
                     "options": [("Move back", "forest")]},
    # ===================================================END_SHADOW_PEAKS=================================================== #

    # =============================================STORE============================================================== #
    "store": {"text": "Gorn's Shop sells weapons, potions and spells.",

              "options": [("Sell", "sell"),
                          ("Buy", "buy")],
              "function": "store_screen"}, # Function in str

    "sell": {"text": "Items you can sell",
             "options": [],
             "function": "buy_and_sell"}, # Function in str

    "buy": {"text": "Items you can buy",
            "options": [],
            "function": "buy_and_sell"}, # Function in str
    # =============================================ENDSTORE=========================================================== #

    "GAME_OVER": {"text": "",
                  "options": [("Close Game", "GAME_OVER")]},
}

with open("screens.json", "w") as f:
    json.dump(screens, f, default=str)
