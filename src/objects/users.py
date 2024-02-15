from datetime import datetime

from sqlalchemy import Column, Integer, Text, Date, BLOB
from sqlalchemy.ext.declarative import declarative_base

from src.db_config import Session


Base = declarative_base()

class USER(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text, unique=True)
    password = Column(BLOB)
    creationDate = Column(Date)

    def __init__(self, id: None, name, password, creationDate: None) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.creationDate = datetime.now().date()

    def __str__(self) -> str:
        return f"USER ==> id: {self.id}, name: {self.name}, password: {self.password}, creationDate: {self.creationDate}"

    @staticmethod
    def add(user):
        with Session() as session:
            session.add(user)
            session.commit()
            print(user)
        return user
    
    @staticmethod
    def get_byID(id):
        with Session() as session:
            user = session.query(USER).filter_by(id=id).first()

            if user is not None:
                return user
            else:
                return None
        
    @staticmethod
    def get_byName(name):
        with Session() as session:
            user = session.query(USER).filter_by(name=name).first()

            if user:
                return user
            else:
                return None
        
    @staticmethod
    def delete(name):
        with Session() as session:
            user = USER.get_byName(name)

            if user:
                session.delete(user)
                session.commit()

                return "votre compte a bien été supprimé !"
            else:
                return None
