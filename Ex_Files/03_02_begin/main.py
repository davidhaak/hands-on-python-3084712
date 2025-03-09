import csv
from datetime import datetime
from pprint import pprint
#adding datetime datastructures

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")#creates the litte divider
        year_date = datetime.strptime(laureate["year"], "%Y") #telling parser how to parse (just get year)
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        print("age", year_date.year - born_date.year)#doing math inline
        break
