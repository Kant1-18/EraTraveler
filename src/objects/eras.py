from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from src.db_config import Session


Base = declarative_base()

class ERA(Base):
    __tablename__ = "eras"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR, unique=True)

    def __init__(self, id: None, name) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"ERA ==> id: {self.id}, name: {self.name}"
    
    @staticmethod
    def add(era):
        with Session() as session:
            session.add(era)
            session.commit()
            print(era)
        return era

    @staticmethod
    def get_byID(idEra):
        with Session() as session:
            era = session.query(ERA).filter_by(id=idEra).first()

            if era:
                return era
            else:
                return None
        
    @staticmethod
    def get_byName(nameEra):
        with Session() as session:
            era = session.query(ERA).filter_by(name=nameEra).first()

            if era:
                return era
            else:
                return None
        
    @staticmethod
    def delete(nameEra):
        with Session() as session:
            era = ERA.get_byName(nameEra)

            if era:
                session.delete(era)
                session.commit()
