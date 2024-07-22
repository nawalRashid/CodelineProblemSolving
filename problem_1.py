
import re

def validate_name(name):
    return 0 < len(name) <= 50

def validate_passwd(pw):
    return (
        len(pw) >= 8 and
        re.search("[A-Z]", pw) and
        re.search("[a-z]", pw) and
        re.search("[0-9]", pw) and
        re.search("[!@#$%^&*]", pw)
    )

def validate_mail(mail):
    if "@" not in mail:
        return False
    user, dom = mail.split("@")
    return re.match(r"^[a-zA-Z0-9]+", user) and re.match(r"[a-zA-Z]+\.[a-zA-Z]+$", dom)

name = input("Username: ")
passwd = input("Password: ")
mail = input("Email: ")

name_valid = "valid" if validate_name(name) else "invalid"
passwd_valid = "valid" if validate_passwd(passwd) else "invalid"
mail_valid = "valid" if validate_mail(mail) else
