from sqlalchemy import Column, Integer, BLOB
from sqlalchemy.ext.declarative import declarative_base

from src.db_config import Session

Base = declarative_base()

class SALT(Base):
    __tablename__ = "salts"

    id = Column(Integer, autoincrement=True, primary_key=True)
    idUser = Column(Integer)
    salt = Column(BLOB)

    def __init__(self, id: None, idUser, salt) -> None:
        self.id = id
        self.idUser = idUser
        self.salt = salt

    def __str__(self) -> str:
        return f"SALT ==> id: {self.id}, idUser: {self.idUser}, salt: {self.salt}"
    
    @staticmethod
    def add(salt):
        with Session() as session:
            session.add(salt)
            session.commit()
            print(salt)
        return salt

    @staticmethod
    def get_byID(idSalt):
        with Session() as session:
            salt = session.query(SALT).filter_by(id=idSalt).first()

            if salt:
                return salt
            else:
                return None
        
    @staticmethod
    def get_byUser(idUser):
        with Session() as session:
            salt = session.query(SALT).filter_by(idUser=idUser).first()

            if salt:
                return salt
            else:
                return None
        
    @staticmethod
    def delete(idUser):
        with Session() as session:
            salt = SALT.get_byUser(idUser)

            if salt:
                session.delete(salt)
                session.commit()
