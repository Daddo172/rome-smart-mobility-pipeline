import requests
import datetime
from database import session, ParkingData # Importiamo il database creato prima

# La tua API Key
API_KEY = "f1679040da18adbf93b37fffff9d9876"
CITY = "Rome"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

def fetch_and_save():
    # 1. Chiamata API
    response = requests.get(URL)
    data = response.json()
    
    # Debug: stampiamo cosa abbiamo ricevuto
    print(data) 
    
    if 'main' not in data:
        print("Errore: la chiave 'main' non è presente. Controlla la tua API KEY o l'URL.")
        return

    temp = data['main']['temp'] - 273.15 # Convertiamo da Kelvin a Celsius
    
    # 3. Creazione record per il DB
    nuovo_record = ParkingData(
        nome_parcheggio=f"Meteo Roma - {datetime.datetime.now().strftime('%H:%M')}",
        posti_totali=int(temp) # Usiamo un campo esistente per test
    )
    
    # 4. Salvataggio nel database
    session.add(nuovo_record)
    session.commit()
    print(f"Dato salvato: {temp:.2f}°C")

if __name__ == "__main__":
    fetch_and_save()