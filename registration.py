import hashlib
import re

def valid_password(password):
    if len(password) < 12:
        return False
    upper_letter = 0
    lower_letter = 0
    num = 0
    symbol = 0
    for i in password:
        if ord('a') <= ord(i) <= ord('z'):
            lower_letter = 1
        if ord('A') <= ord(i) <= ord('Z'):
            upper_letter = 1
        if ord('0') <= ord(i) <= ord('9'):
            num = 1
        if (not i.isalpha() and not i.isdigit()):
            symbol = 1
    return lower_letter == upper_letter == num == symbol == 1

def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_obj = hashlib.sha256(password_bytes)
    return hash_obj.hexdigest()

def register():
    email = input("Enter email: ")
    user_name = input("Enter username: ")
    password = input("Enter password: ")

    f = open("password.txt")
    for line in f:
        l = line.split()
        if user_name == l[0]:
            f.close()
            print("\nThis user already exists!!!\nMaybe you want to login\n")
            return False
        if not valid_password(password):
            print("\nYou entered invalid password")
            print("\nPassword should contain at least 12 charaters, 1 Uppercase, 1 Lowercase, 1 numeric, 1 symbol\n")
            return False
        if not valid_email(email):
            print("\nYou entered invalid email\n")
            return False

    else:
        f.close()
        f = open("password.txt", "a")
        f.write(f"{user_name} {hash_password(password)} {email}\n")
        f.close()
        print("\nSuccessfully registered!!!\n")
        return True

def login():
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    f = open("password.txt")
    for line in f:
        l = line.split()
        if user_name == l[0] and hash_password(password) == l[1]:
            f.close()
            print("\nSuccessfully loged in!!!\n")
            return True
    else:
        f.close()
        print("\nSomething went worng\nMaybe you want to register?\n")
        return False


while(True):
    res = None
    call_func = input("If you want to register enter - r\nIf you want to login enter - l\nIf you want to exit enter - e\n")
    if call_func == "r":
        res = register()
    elif call_func == "l":
        res = login()
    elif call_func == "e":
        break
    if res == True:
        break