
# Rome Smart Mobility Pipeline

## 🌍 Panoramica
Un sistema automatizzato per la raccolta e l'analisi di dati urbani a Roma. Il progetto integra:
1. **Data Ingestion:** Script Python per il recupero dati tramite API.
2. **Data Storage:** Database relazionale (SQLite) tramite SQLAlchemy.
3. **Data Visualization:** Dashboard interattiva con Streamlit.

## 🛠 Tech Stack
- **Linguaggio:** Python
- **Database:** SQLite & SQLAlchemy
- **Data Pipeline:** Requests (API consumption)
- **Dashboard:** Streamlit & Plotly

## 🚀 Come avviare il sistema
1. Installa i requisiti: `pip install -r requirements.txt`
2. Configura le variabili d'ambiente in un file `.env` (API_KEY).
3. Inizializza il DB: `python database.py`
4. Avvia la raccolta dati: `python fetch_data.py`
5. Lancia la dashboard: `python -m streamlit run app.py`

## 📊 Obiettivi futuri
- Automatizzazione tramite CRON jobs (esecuzione in background).
- Integrazione mappe interattive (GeoPandas).
