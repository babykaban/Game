import json

# sample array of dictionaries
data = [
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 25},
    {'name': 'Bob', 'age': 40}
]

# convert the array of dictionaries into a string
json_string = json.dumps(data)

# open the file in write mode and write the string to the file
with open('data.txt', 'w') as file:
    file.write(json_string)
