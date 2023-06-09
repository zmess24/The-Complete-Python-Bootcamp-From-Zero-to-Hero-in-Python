import json

companies = []
file = open('company_data.json', 'r')

parsed = json.load(file)

for company in parsed:
    print(company['name'])