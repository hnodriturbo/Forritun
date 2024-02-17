import json

# Read a JSON file
with open('filename.json', 'r') as file:
    data = json.load(file)
    
# Write to a JSON file
with open('filename.json', 'w') as file:
    json.dump(data, file, indent=4)


# Converting between JSON strings and Python objects:
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data['name'])  # Outputs: John

python_dict = {"name": "Doe", "age": 40, "city": "London"}
json_string = json.dumps(python_dict)
print(json_string)  # Outputs: {"name": "Doe", "age": 40, "city": "London"}

# If you're dealing with JSON data that's not in a file but is in the form of a string (which you might get from an API, for instance), you can use:

json.loads(): # To parse a JSON string into a Python object.
json.dumps(): # To convert a Python object into a JSON-formatted string.