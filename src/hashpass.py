import bcrypt

def genSalt():
    return bcrypt.gensalt()

def encrypt(password, salt):
    try:
        password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, salt)

    except:
        hashed_password = bcrypt.hashpw(password, salt)
        
    finally:
        return hashed_password

def checkPass(password, salt, hashedPass):
    password = encrypt(password, salt)
    if password == hashedPass:
        return True
    else:
        return False
