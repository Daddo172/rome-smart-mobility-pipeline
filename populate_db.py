import pandas as pd
from database import Session, ParkingData

def populate():
    # Leggi il CSV (verifica il separatore, se da errore usa ',')
    df = pd.read_csv('parcheggi_roma.csv', sep=';')
    
    session = Session()
    # Pulisci i dati dai valori non numerici
    df['P_Totali'] = pd.to_numeric(df['P_Totali'], errors='coerce').fillna(0)
    
    for _, row in df.iterrows():
        record = ParkingData(
            nome_parcheggio=str(row['Nome']),
            posti_totali=int(row['P_Totali'])
        )
        session.add(record)
    
    session.commit()
    session.close()
    print("Database popolato con successo!")

if __name__ == "__main__":
    populate()