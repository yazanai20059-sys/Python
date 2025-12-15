import os
import json

if os.path.isfile("ex1.json"):
    os.rename("ex1.json","ex2.json")
    with open("ex2.json", "r") as f:
        dades=json.load(f)
        print(dades)
else:
    print("el fitxer no ecsisteix")