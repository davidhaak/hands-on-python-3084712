import csv
import json
from pprint import pprint

#Converting csv to json
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

#Doing this at scale
with open("laureates.csv", "r") as f: #as f makes it an object
    reader = csv.DictReader(f)
    laureates = list(reader)

#open a new file in write mode (creates empty file for writing)
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)#dump has no s becuase adding all
