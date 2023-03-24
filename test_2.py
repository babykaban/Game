import json
with open("test_screens.json", "r") as file:
    screens = json.load(file)

for screen in screens:
    print(screens[screen]["options"])