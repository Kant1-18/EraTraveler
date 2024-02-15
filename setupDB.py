import mysql.connector as mysql

from src.hashpass import genSalt, encrypt
from src.objects.users import USER
from src.objects.salts import SALT
from src.objects.saves import SAVE
from src.objects.eras import ERA
from src.objects.levels import LEVEL

sqlFile = "EraTraveler/main.sql"
dbName = "main"

db_configRoot = {
    "host": "127.0.0.1",
    "port": "3306",
    "user": "root",
    "password": "password",
    "database": "mysql"
}

db_configRoot_Main = {
    "host": "127.0.0.1",
    "port": "3306",
    "user": "root",
    "password": "password",
    "database": "main"
}

users = [
    USER(id=None, name="quentin", password="coucou", creationDate=None),
    USER(id=None, name="matheo", password="coucou", creationDate=None),
    USER(id=None, name="daphne", password="coucou", creationDate=None),
    USER(id=None, name="sami", password="coucou", creationDate=None),
]

saves = [
    SAVE(id=None, idUser=1, coins=0, idLevel=1, items=0),
    SAVE(id=None, idUser=2, coins=0, idLevel=1, items=0),
    SAVE(id=None, idUser=3, coins=0, idLevel=1, items=0),
    SAVE(id=None, idUser=4, coins=0, idLevel=1, items=0),
]

eras = [
    ERA(id=None, name="tuto"),
    ERA(id=None, name="antiquity"),
    ERA(id=None, name="middleAges"),
    ERA(id=None, name="present"),
    ERA(id=None, name="future"),
]

levels = [
    LEVEL(id=None, idEra=1, num=3, difficulty=0),
    LEVEL(id=None, idEra=2, num=1, difficulty=1),
    LEVEL(id=None, idEra=2, num=2, difficulty=1),
    LEVEL(id=None, idEra=2, num=3, difficulty=2),
    LEVEL(id=None, idEra=3, num=1, difficulty=2),
    LEVEL(id=None, idEra=3, num=2, difficulty=2),
    LEVEL(id=None, idEra=3, num=3, difficulty=3),
    LEVEL(id=None, idEra=4, num=1, difficulty=3),
    LEVEL(id=None, idEra=4, num=2, difficulty=3),
    LEVEL(id=None, idEra=4, num=3, difficulty=4),
    LEVEL(id=None, idEra=5, num=1, difficulty=4),
    LEVEL(id=None, idEra=5, num=2, difficulty=4),
    LEVEL(id=None, idEra=5, num=3, difficulty=5),
]

def createDBs():
    conn = mysql.connect(**db_configRoot)
    cur = conn.cursor()

    cur.execute("CREATE DATABASE main")

    conn.commit()
    conn.close()

def createUser():
    conn = mysql.connect(**db_configRoot)
    cur = conn.cursor()

    cur.execute("CREATE USER 'gameMaster'@'%' identified by 'password'")
    cur.execute("GRANT ALL PRIVILEGES ON main.* TO 'gameMaster'@'%'")
    cur.execute("FLUSH PRIVILEGES")

    conn.commit()
    conn.close()

def tablesMain():
    try:
        conn = mysql.connect(**db_configRoot_Main)
        cursor = conn.cursor()
        
        with open(f"{sqlFile}", 'r') as f:
            sql_commands = f.read().split(';')

            for command in sql_commands:
                try:
                    cursor.execute(command)
                    print(" ")
                    print(f"La commande SQL a été exécutée avec succès : {command}")
                except mysql.Error as e:
                    print(f"Erreur lors de l'exécution de la commande SQL : {command}\nErreur : {str(e)}")

        conn.commit()
        print(" ")
        print("Base de données créée avec succès.")
    except mysql.Error as err:
        print(f"Erreur lors de la création de la base de données : {err}")
    finally:
        cursor.close()
        conn.close()

def drop():
    conn = mysql.connect(**db_configRoot_Main)
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {dbName}")

if __name__ == "__main__":
    while True:
        choice = int(input("[1::create db] - [2::drop db] - [3::exit] - [4::drop & create & exit]>>> "))
        if choice == 1:
    
            try:
                createDBs()
                print("CREATE DB [OK]")
            except Exception as e:
                print(str(e))

            try:
                createUser()
                print("createUser [OK]")
            except Exception as e:
                print(str(e))

            try:
                tablesMain()
                print("Tables in main [OK]")
            except Exception as e:
                print(f"ERROR::{str(e)}")

##########################################################################################################
##########################################################################################################
            try:
                for user in users:
                    salt = genSalt()
                    user.password = encrypt(user.password, salt)
                    user = USER.add(user)
                    print(user)
                    salt = SALT(None, user.id, salt)
                    SALT.add(salt)

                for era in eras:
                    ERA.add(era)

                for level in levels:
                    LEVEL.add(level)
                
                for save in saves:
                    SAVE.add(save)


                print(" ")
                print("Insert data [OK]")
                print(" ")
##########################################################################################################
##########################################################################################################

            except Exception as e:
                print(f"ERROR::{str(e)}")
    
        elif choice == 2:
            drop()

        elif choice == 3:
            exit()

        elif choice == 4:
            drop()

            try:
                createDBs()
                print("CREATE DB [OK]")
            except Exception as e:
                print(str(e))

            try:
                createUser()
                print("createUser [OK]")
            except Exception as e:
                print(str(e))

            try:
                tablesMain()
                print("Tables in main [OK]")
            except Exception as e:
                print(f"ERROR::{str(e)}")

##########################################################################################################
##########################################################################################################
            try:
                for user in users:
                    salt = genSalt()
                    user.password = encrypt(user.password, salt)
                    user = USER.add(user)
                    print(user)
                    salt = SALT(None, user.id, salt)
                    SALT.add(salt)

                for era in eras:
                    ERA.add(era)

                for level in levels:
                    LEVEL.add(level)
                
                for save in saves:
                    SAVE.add(save)


                print(" ")
                print("Insert data [OK]")
                print(" ")
##########################################################################################################
##########################################################################################################

            except Exception as e:
                print(f"ERROR::{str(e)}")

            finally:
                exit()

        else:
            print("non valide")