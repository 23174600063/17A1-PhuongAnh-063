import json

data = [
    {"name": "phanh", "age": 15, "school": "uneti"},
    {"name": "pun", "age": 12, "school": "ba"},
    {"name": "bun", "age": 14, "school": "tmu"}
]

data_sorted = sorted(data, key=lambda x: x['name'])
data_json = json.dumps(data_sorted, indent=4)

print(data_json)
