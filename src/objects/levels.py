from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from src.db_config import Session


Base = declarative_base()

class LEVEL(Base):
    __tablename__ = "levels"

    id = Column(Integer, autoincrement=True, primary_key=True)
    idEra = Column(Integer)
    num = Column(Integer)
    difficulty = Column(Integer)

    def __init__(self, id: None, idEra, num, difficulty) -> None:
        self.id = id
        self.idEra = idEra
        self.num = num
        self.difficulty = difficulty

    def __str__(self) -> str:
        return f"LEVEL ==> id: {self.id}, idEra: {self.idEra}, num: {self.num}, difficulty: {self.difficulty}"
    
    @staticmethod
    def add(level):
        with Session() as session:
            session.add(level)
            session.commit()
            print(level)
        return level
    
    @staticmethod
    def get_byID(idLevel):
        with Session() as session:
            level = session.query(LEVEL).filter_by(id=idLevel).first()

            if level:
                return level
            else:
                return None
        
    @staticmethod
    def getALL_byEra(idEra):
        with Session() as session:
            levels = session.query(LEVEL).filter_by(idEra=idEra).all()

            if len(levels) != 0:
                return levels
            else:
                return None

    @staticmethod
    def getALL_byNum(num):
        with Session() as session:
            levels = session.query(LEVEL).filter_by(num=num).all()

            if len(levels) != 0:
                return levels
            else:
                return None

    @staticmethod
    def getALL_byDifficulty(difficulty):
        with Session() as session:
            levels = session.query(LEVEL).filter_by(difficulty=difficulty).all()

            if len(levels) != 0:
                return levels
            else:
                return None
        
    @staticmethod
    def set_era(idLevel, newValue):
        with Session() as session:
            level = LEVEL.get_byID(idLevel)

            if level:
                level.idEra = newValue
                session.commit()

    @staticmethod
    def set_num(idLevel, newValue):
        with Session() as session:
            level = LEVEL.get_byID(idLevel)

            if level:
                level.num = newValue
                session.commit()

    @staticmethod
    def set_difficulty(idLevel, newValue):
        with Session() as session:
            level = LEVEL.get_byID(idLevel)

            if level:
                level.difficulty = newValue
                session.commit()
    
    @staticmethod
    def delete(idLevel):
        with Session() as session:
            level = LEVEL.get_byID(idLevel)

            if level:
                session.delete(level)
                session.commit()
