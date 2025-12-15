import json
with open("ex2.json", "r") as f:
    dades=json.load(f)
    print(dades)

with open("ex2.json", "w+") as f:
    dades["colors"]=["blanc","negre"]
    json.dump(dades,f)


