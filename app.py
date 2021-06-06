import sys, base64
from requests import get

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Finder:
    def __init__(self):
        super().__init__()

        self.service = 'https://api.ipify.org'

        password = None
        with open('.password', 'r') as file:
            password = bytes(file.readline().strip(), encoding='utf8')

        salt = None
        with open('.salt', 'r') as file:
            salt = bytes(file.readline().strip(), encoding='utf8')

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))
        self.fernet = Fernet(key)

    def decrypt(self, encrypted):
        ip = self.fernet.decrypt(encrypted).decode("utf-8")
        print(ip)
        sys.exit()

    def get(self):
        ip = bytes(get(self.service).text, 'utf-8')

        encrypted = self.fernet.encrypt(ip)

        return encrypted

from flask import Flask
FinderApp = Flask(__name__)

@FinderApp.route('/')
def main():
    finder = Finder()
    response = finder.get()
    return response

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'decrypt':
            finder = Finder()
            ecrypted_ip = bytes(sys.argv[2], encoding='utf8')
            finder.decrypt(ecrypted_ip)
        else:
            print('Something was wrong')
    else:
        FinderApp.run()
  
