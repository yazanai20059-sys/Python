import requests
# Sol·licita el nom de la ciutat
ciutat=input("Indiqui el nom de la ciutat:")
# Cream un diccionari amb les dades de la petició
parametres={"q":ciutat,
        	"units":"metric",
        	"APPID":"ee3b97040fe64db3643b368c530acc27"}
# Fem la petició indicant l'url i els paràmetres
res=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametres)
# Si retorna el codi d'estat 200, ha anat bé i podem fer feina, si no sortim
if res.status_code == 200:
# Convertim la resposta JSON en un diccionari
    dades = res.json()
# Imprimir els valors del diccionari que volem
    print("La temperatura actual és:", dades["main"]["temp"],"ºC")
    print("La sensació tèrmica és:", dades["main"]["feels_like"],"ºC")
    print("La temperatura mínima és:", dades["main"]["temp_min"],"ºC")
    print("La temperatura màxima és:", dades["main"]["temp_max"],"ºC")
    print("La pressió és:",dades["main"]["pressure"],"hPa")
    print("La humitat és:",dades["main"]["humidity"],"%")
else:
    print("No hi ha dades d'aquesta ciutat.")
