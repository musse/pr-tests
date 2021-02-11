import json

with open('content/model.json') as f:
    model = json.load(f)

print(f"Model {model['name']} has type {model['type']}")
