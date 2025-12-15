import json

dadesjson = '{"nom":"Joan","edad":45}'
dades = json.loads(dadesjson) 
print(dades)