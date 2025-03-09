import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
#Making the CSV more json like using dictionary key:str
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
#making csv into dict at scale
#with has some magic it will memory efficient will open and then close not hold open.
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)
#last step above it keeps laureates in memory as a list
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break

