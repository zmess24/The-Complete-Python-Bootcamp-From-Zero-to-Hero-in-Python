import json

companies = []
file = open('company_data.json', 'r')

parsed = json.load(file)

print(parsed)