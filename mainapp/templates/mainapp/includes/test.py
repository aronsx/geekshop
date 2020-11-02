import os
import json


with open("locations.json") as f:
    pop_data = json.load(f)

print(pop_data)

# with open("locations.json", "r") as read_file:
#     loc = json.loads(read_file)
#     print(loc)
