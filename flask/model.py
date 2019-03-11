import sqlite3
from flask import current_app

class Database:

    def __init__(self, name):
        self.db = sqlite3.connect(name)

    @classmethod
    def createTable(cls, name, schema):
        db = sqlite3.connect(name)
        with open(schema, 'r') as f:
            db.executescript(f.read().decode('utf8'))
          
        db.close()

    def close(self):
        if self.db is not None:
            self.db.close()

    def userValidate(self, username, password):
        return "123456789"

    def wishlist(self, userID, start, count):
        return []

    def post(self, userID, title, content):
        return True
