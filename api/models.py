from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()

class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_hora = Column(DateTime, default=datetime.datetime.now)

# SQLite simple
DATABASE_URL = "sqlite:///./turnos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
