import requests
import json
from datetime import datetime

# Nota: Aquesta aplicació utilitzarà una API gratuïta en lloc de web scraping directe
# perquè és més fiable i legal. API utilitzada: Open-Meteo (sense necessitat de clau)

def obte_coordenades_ciutat(ciutat):
    """
    Obté les coordenades geogràfiques d'una ciutat
    Args:
        ciutat: nom de la ciutat
    Returns:
        tuple (latitud, longitud, nom_complet) o None si no es troba
    """
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciutat}&count=1&language=ca&format=json"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        if 'results' in dades and len(dades['results']) > 0:
            resultat = dades['results'][0]
            return (resultat['latitude'], resultat['longitude'], resultat['name'])
        return None
    except Exception as e:
        print(f"❌ Error obtenint coordenades: {e}")
        return None

def obte_temps_actual(latitud, longitud):
    """
    Obté informació meteorològica actual
    Args:
        latitud: latitud de la localització
        longitud: longitud de la localització
    Returns:
        diccionari amb dades meteorològiques o None si hi ha error
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&timezone=Europe/Madrid"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        return dades['current'] if 'current' in dades else None
    except Exception as e:
        print(f"❌ Error obtenint dades meteorològiques: {e}")
        return None

def obte_previsions(latitud, longitud, dies=7):
    """
    Obté previsions meteorològiques
    Args:
        latitud: latitud de la localització
        longitud: longitud de la localització
        dies: nombre de dies de previsió (màxim 16)
    Returns:
        diccionari amb previsions o None si hi ha error
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code&timezone=Europe/Madrid&forecast_days={dies}"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        return dades['daily'] if 'daily' in dades else None
    except Exception as e:
        print(f"❌ Error obtenint previsions: {e}")
        return None

def interpreta_codi_temps(codi):
    """
    Interpreta el codi WMO del temps
    Args:
        codi: codi WMO (0-99)
    Returns:
        tuple (descripció, emoji)
    """
    codis = {
        0: ("Cel clar", "☀️"),
        1: ("Majoritàriament clar", "🌤️"),
        2: ("Parcialment ennuvolat", "⛅"),
        3: ("Ennuvolat", "☁️"),
        45: ("Boira", "🌫️"),
        48: ("Boira amb gelada", "🌫️"),
        51: ("Plugim lleuger", "🌦️"),
        53: ("Plugim moderat", "🌦️"),
        55: ("Plugim intens", "🌧️"),
        61: ("Pluja lleugera", "🌧️"),
        63: ("Pluja moderada", "🌧️"),
        65: ("Pluja intensa", "🌧️"),
        71: ("Neu lleugera", "🌨️"),
        73: ("Neu moderada", "🌨️"),
        75: ("Neu intensa", "❄️"),
        77: ("Granissos", "🌨️"),
        80: ("Ruixats lleugers", "🌦️"),
        81: ("Ruixats moderats", "🌧️"),
        82: ("Ruixats intensos", "⛈️"),
        85: ("Ruixats de neu lleugers", "🌨️"),
        86: ("Ruixats de neu intensos", "❄️"),
        95: ("Tempesta", "⛈️"),
        96: ("Tempesta amb calamarsa", "⛈️"),
        99: ("Tempesta amb calamarsa intensa", "⛈️")
    }
    
    return codis.get(codi, ("Desconegut", "❓"))

def mostra_temps_actual(ciutat, dades):
    """
    Mostra la informació meteorològica actual de forma visual
    Args:
        ciutat: nom de la ciutat
        dades: diccionari amb dades meteorològiques
    """
    descripcio, emoji = interpreta_codi_temps(dades.get('weather_code', 0))
    
    print("\n" + "="*60)
    print(f"🌍 TEMPS ACTUAL A {ciutat.upper()}")
    print("="*60)
    print(f"\n{emoji} {descripcio}")
    print(f"\n🌡️  Temperatura: {dades.get('temperature_2m', 'N/A')}°C")
    print(f"🌡️  Sensació tèrmica: {dades.get('apparent_temperature', 'N/A')}°C")
    print(f"💧 Humitat: {dades.get('relative_humidity_2m', 'N/A')}%")
    print(f"🌧️  Precipitació: {dades.get('precipitation', 'N/A')} mm")
    print(f"💨 Vent: {dades.get('wind_speed_10m', 'N/A')} km/h")
    print(f"\n🕐 Actualitzat: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)

def mostra_previsions(ciutat, dades, dies=7):
    """
    Mostra les previsions meteorològiques
    Args:
        ciutat: nom de la ciutat
        dades: diccionari amb previsions
        dies: nombre de dies a mostrar
    """
    print("\n" + "="*60)
    print(f"📅 PREVISIÓ PER A {ciutat.upper()} ({dies} dies)")
    print("="*60)
    
    for i in range(min(dies, len(dades['time']))):
        data = dades['time'][i]
        temp_max = dades['temperature_2m_max'][i]
        temp_min = dades['temperature_2m_min'][i]
        precipitacio = dades['precipitation_sum'][i]
        codi = dades['weather_code'][i]
        
        descripcio, emoji = interpreta_codi_temps(codi)
        
        # Formatear la data
        data_obj = datetime.strptime(data, '%Y-%m-%d')
        dia_setmana = ['Dl', 'Dt', 'Dc', 'Dj', 'Dv', 'Ds', 'Dg'][data_obj.weekday()]
        data_format = data_obj.strftime('%d/%m')
        
        print(f"\n{emoji} {dia_setmana} {data_format} - {descripcio}")
        print(f"   🌡️  Màx: {temp_max}°C | Mín: {temp_min}°C")
        if precipitacio > 0:
            print(f"   🌧️  Precipitació: {precipitacio} mm")

def compara_ciutats(ciutats):
    """
    Compara el temps de múltiples ciutats
    Args:
        ciutats: llista de noms de ciutats
    """
    print("\n" + "="*60)
    print("📊 COMPARACIÓ DE CIUTATS")
    print("="*60)
    
    dades_ciutats = []
    
    for ciutat in ciutats:
        coordenades = obte_coordenades_ciutat(ciutat)
        if coordenades:
            lat, lon, nom_complet = coordenades
            temps = obte_temps_actual(lat, lon)
            if temps:
                dades_ciutats.append({
                    'nom': nom_complet,
                    'temperatura': temps.get('temperature_2m', 0),
                    'temps': interpreta_codi_temps(temps.get('weather_code', 0))
                })
    
    if not dades_ciutats:
        print("❌ No s'han pogut obtenir dades")
        return
    
    # Ordenar per temperatura
    dades_ciutats.sort(key=lambda x: x['temperatura'], reverse=True)
    
    print("\n🔥 Més càlides:")
    for i, ciutat in enumerate(dades_ciutats[:3], 1):
        emoji = ciutat['temps'][1]
        print(f"   {i}. {ciutat['nom']}: {ciutat['temperatura']}°C {emoji}")
    
    print("\n❄️  Més fredes:")
    for i, ciutat in enumerate(reversed(dades_ciutats[-3:]), 1):
        emoji = ciutat['temps'][1]
        print(f"   {i}. {ciutat['nom']}: {ciutat['temperatura']}°C {emoji}")

def historial_consultes(ciutat):
    """
    Simula un historial de consultes (guardant en fitxer)
    Args:
        ciutat: nom de la ciutat consultada
    """
    try:
        # Intentar carregar l'historial existent
        try:
            with open('historial_temps.json', 'r', encoding='utf-8') as f:
                historial = json.load(f)
        except FileNotFoundError:
            historial = []
        
        # Afegir nova consulta
        historial.append({
            'ciutat': ciutat,
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Mantenir només les últimes 20 consultes
        historial = historial[-20:]
        
        # Guardar historial
        with open('historial_temps.json', 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️  No s'ha pogut guardar l'historial: {e}")

def mostra_historial():
    """Mostra l'historial de consultes"""
    try:
        with open('historial_temps.json', 'r', encoding='utf-8') as f:
            historial = json.load(f)
        
        if not historial:
            print("\n📭 No hi ha consultes en l'historial")
            return
        
        print("\n" + "="*60)
        print("📜 HISTORIAL DE CONSULTES")
        print("="*60)
        
        for consulta in reversed(historial[-10:]):  # Últimes 10
            print(f"🌍 {consulta['ciutat']}")
            print(f"   📅 {consulta['data']}")
    except FileNotFoundError:
        print("\n📭 No hi ha consultes en l'historial")
    except Exception as e:
        print(f"❌ Error llegint l'historial: {e}")

def menu_meteorologia():
    """Mostra el menú de meteorologia"""
    print("\n" + "="*60)
    print("CONSULTA METEOROLÒGICA")
    print("="*60)
    print("\n1. Consultar temps actual d'una ciutat")
    print("2. Consultar previsió (7 dies)")
    print("3. Consultar previsió (14 dies)")
    print("4. Comparar múltiples ciutats")
    print("5. Veure historial de consultes")
    print("0. Tornar al menú principal")

def main():
    """Funció principal de l'aplicació 5"""
    
    print("\n⚠️  NOTA: Aquesta aplicació requereix connexió a Internet")
    print("Utilitza l'API gratuïta Open-Meteo per obtenir dades meteorològiques")
    
    while True:
        menu_meteorologia()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            ciutat = input("\n🌍 Nom de la ciutat: ").strip()
            if not ciutat:
                print("❌ Has d'introduir una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            print("\n🔍 Cercant informació...")
            coordenades = obte_coordenades_ciutat(ciutat)
            
            if not coordenades:
                print(f"❌ No s'ha pogut trobar '{ciutat}'")
                input("\nPrem ENTER per continuar...")
                continue
            
            lat, lon, nom_complet = coordenades
            temps = obte_temps_actual(lat, lon)
            
            if temps:
                mostra_temps_actual(nom_complet, temps)
                historial_consultes(nom_complet)
            else:
                print("❌ No s'han pogut obtenir les dades meteorològiques")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "2" or opcio == "3":
            dies = 7 if opcio == "2" else 14
            ciutat = input("\n🌍 Nom de la ciutat: ").strip()
            
            if not ciutat:
                print("❌ Has d'introduir una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            print("\n🔍 Cercant informació...")
            coordenades = obte_coordenades_ciutat(ciutat)
            
            if not coordenades:
                print(f"❌ No s'ha pogut trobar '{ciutat}'")
                input("\nPrem ENTER per continuar...")
                continue
            
            lat, lon, nom_complet = coordenades
            previsions = obte_previsions(lat, lon, dies)
            
            if previsions:
                mostra_previsions(nom_complet, previsions, dies)
                historial_consultes(nom_complet)
            else:
                print("❌ No s'han pogut obtenir les previsions")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "4":
            print("\n🌍 Introdueix ciutats per comparar (separades per comes)")
            print("Exemple: Barcelona, Madrid, València, Sevilla")
            entrada = input("\nCiutats: ").strip()
            
            if not entrada:
                print("❌ Has d'introduir almenys una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            ciutats = [c.strip() for c in entrada.split(',')]
            print("\n🔍 Obtenint informació...")
            compara_ciutats(ciutats)
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "5":
            mostra_historial()
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()