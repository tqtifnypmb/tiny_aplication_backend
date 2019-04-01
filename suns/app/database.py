import mysql.connector

class Database:

    def __init__(self, name):
        self.db = mysql.connector.connect(user='suns', password='1816400', host='db', database=name)

    def upload_image(self, name):
        insert = ("INSERT INTO images (name) VALUES (%s);")
        cursor = self.db.cursor()
        cursor.execute(insert, name)

    def close(self):
        if self.db is None:
            return

        self.db.close()