from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


db_config = {
"host": "127.0.0.1",
"port": "3306",
"user": "gameMaster",
"password": "password",
"database": "main"
}

engine = create_engine(f'mysql+mysqlconnector://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}',)
Session = sessionmaker(bind=engine)

Session = scoped_session(Session)
