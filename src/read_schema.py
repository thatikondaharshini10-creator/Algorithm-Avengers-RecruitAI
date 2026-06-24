import json
from pprint import pprint

with open("data/candidate_schema.json", "r", encoding="utf-8") as file:
    schema = json.load(file)

pprint(schema)