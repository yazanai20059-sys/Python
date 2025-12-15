from urllib import request
f = request.urlopen('https://www.wikidex.net/wiki/WikiDex')
dades = f.read()
print(dades.decode('utf-8'))
