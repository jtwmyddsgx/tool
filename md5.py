import hashlib
import requests


def encryption():
    m = hashlib.md5()
    password = input("想要加密的字符串：")
    m.update(password.encode())
    pwd = m.hexdigest()
    print("加密后:", pwd)


def get_many():
    password = "cca9cc444e64c8116a30la00559c042b4"
    passwords = []
    for i in range(len(password)):
        passwords.append(password[:i]+password[i+1:])
    passwords = list(set(passwords))
    for i in passwords:
        print(i)


if __name__ == "__main__":
    get_many()
