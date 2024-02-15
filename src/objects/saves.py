from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from src.db_config import Session

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

Base = declarative_base()

class SAVE(Base):
    __tablename__ = "saves"

    id = Column(Integer, autoincrement=True, primary_key=True)
    idUser = Column(Integer)
    coins = Column(Integer)
    idLevel = Column(Integer)
    items = Column(Integer)


    def __init__(self, id: None, idUser, coins, idLevel, items) -> None:
        self.id = id
        self.idUser = idUser
        self.coins = coins
        self.idLevel = idLevel
        self.items = items

    def __str__(self) -> str:
        return f"SAVE ==> id: {self.id}, idUser: {self.idUser}, coins: {self.coins}, level: {self.idLevel}, items: {self.items}"
    
    @staticmethod
    def add(save):
        with Session() as session:
            session.add(save)
            session.commit()
            print(save)
        return save

    @staticmethod
    def get_byID(id):
        with Session() as session:
            save = session.query(SAVE).filter_by(id=id).first()

            if save:
                return save
            else:
                return None
        
    @staticmethod
    def get_byUser(idUser):
        with Session() as session:
            save = session.query(SAVE).filter_by(idUser=idUser).first()

            if save:
                return save
            else:
                return None
            
    @staticmethod
    def update(idUser, coins, idLevel, items):
        try:
            #save = SAVE.get_byUser(idUser)
            with Session() as session:
                save = session.query(SAVE).filter_by(idUser=idUser).first()
                print({
                    "idUser": idUser,
                    "coins": coins,
                    "idLevel": idLevel,
                    "items": items
                })
                save.coins = coins
                save.idLevel = idLevel
                save.items = items

                
                session.commit()

                # print(save)
            return save
        except Exception as e:
            print(e)

    @staticmethod
    def delete(idSave):
        with Session() as session:
            save = SAVE.session.query(SAVE).filter_by(id=idSave).first()

            if save:
                session.delete(save)
                session.commit()

                return "Votre sauvegarde a bien été supprimé !"
            else:
                return None
