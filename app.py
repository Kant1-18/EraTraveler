from flask import Flask, render_template as template, request, session, redirect, url_for
from flask_cors import CORS
import secrets

from src.hashpass import genSalt, encrypt, checkPass
from src.objects.users import USER
from src.objects.salts import SALT
from src.objects.saves import SAVE
from src.objects.levels import LEVEL


app = Flask(__name__)
CORS(app)
app.secret_key = secrets.token_hex(16)

@app.route("/level")
def level():
    return template(session["levelTemplate"])

@app.route("/", methods=["POST", "GET"])
def account():
    if request.method == "POST":
        data = request.form
        name = data.get("name")
        password = data.get("password")

        user = USER.get_byName(name)
        
        if user is not None:
            salt = SALT.get_byUser(user.id)
            if checkPass(password, salt.salt, user.password) is True:
                save = SAVE.get_byUser(user.id)
                level = LEVEL.get_byID(save.idLevel)

                session["id"] = user.id
                session["name"] = user.name

                session["coins"] = save.coins
                session["idLevel"] = save.idLevel
                session["items"] = save.items
                
                session["era"] = level.idEra
                session["levelNum"] = level.num

                levelTemplate = f"level_{session['era']}-{session['levelNum']}.html"
                session["levelTemplate"] = levelTemplate

                return template(session["levelTemplate"])
        else:
            return template("account.html", messageError="Utilisateur ou mot de passe invalide !")

    return template("account.html")

@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":
        data = request.form
        name = data.get("name")
        password = data.get("password")

        salt = genSalt()
        password = encrypt(password, salt)

        try:
            newUser = USER(None, name, password, None)

            user = USER.add(newUser)
            if user:
                salt = SALT(None, user.id, salt)
                SALT.add(salt)

                firstSave = SAVE(id=None, idUser=user.id, coins=0, idLevel=1, items=0)
                SAVE.add(firstSave)

            result = True
        
        except:
            result = False

        if result is True:
            return template("account_created.html")
        else:
            return template("signin.html", messageError="Une erreur est survenue.")
        
    return template("signin.html")

@app.route("/account_created")
def account_created():
    return template("account_created.html")

@app.route("/logout")
def logout():
    session.pop("id")
    session.pop("name")
    return template("account.html")

@app.route("/settings")
def settings():
    return template("settings.html")

@app.route("/stats")
def stats():
    return template("stats.html")

@app.post("/save")
def save():
    data = request.get_json()
    coins = data["coins"]

    session["coins"] = int(session["coins"]) + int(coins)

    session["items"] = int(session["items"]) + 1
    if session["levelNum"] == 3:
        session["era"] += 1
        session["levelNum"] = 1
        session["idLevel"] += 1
    else:
        session["levelNum"] += 1
        session["idLevel"] += 1

    levelTemplate = f"level_{session['era']}-{session['levelNum']}.html"
    session["levelTemplate"] = levelTemplate

    SAVE.update(idUser=session["id"], coins=session["coins"], idLevel=session["idLevel"], items=session["items"])

    return {"level": url_for("level")}

@app.route("/reset")
def reset():
    session["coins"] = 0
    session["idLevel"] = 1
    session["items"] = 0

    level = LEVEL.get_byID(session["idLevel"])
    
    session["era"] = level.idEra
    session["levelNum"] = level.num

    levelTemplate = f"level_{session['era']}-{session['levelNum']}.html"
    session["levelTemplate"] = levelTemplate

    return redirect(url_for("level"))

@app.route("/game_end")
def game_end():
    return template("game_end.html")

if __name__ == "__main__":
    app.run(debug=False)
