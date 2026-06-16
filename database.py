from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

# Creazione del database SQLite
engine = create_engine('sqlite:///mobility.db')
Base = declarative_base()

# Definizione della tabella
class ParkingData(Base):
    __tablename__ = 'parking_stats'
    id = Column(Integer, primary_key=True)
    nome_parcheggio = Column(String)
    posti_totali = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Creazione tabella
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)