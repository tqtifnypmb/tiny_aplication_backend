import mysql.connector
import time
from models import Question, Answer
from flask import current_app

class Database:

    def __init__(self, name):
        self.db = mysql.connector.connect(user='wishlist', password='1816400', host='db', database=name)

    def _timestamp(self):
        return int(time.time())

    def close(self):
        if self.db is not None:
            self.db.close()

    def login(self, open_id):
        query = ("SELECT id, name FROM users WHERE open_id = %s;")
        cursor = self.db.cursor()

        cursor.execute(query, (open_id,))
        ret = cursor.fetchone()
        cursor.close()
        return ret

    def signup(self, username, open_id):
        insert = ("INSERT INTO users (name, open_id, c_time) VALUES (%s, %s, %s);")
        ts = self._timestamp()
        cursor = self.db.cursor()

        cursor.execute(insert, (username, open_id, ts))
        self.db.commit()
        cursor.close()
        return True

    def insertQuestion(self, uid, title, text):
        insert = ("INSERT INTO questions (owner_id, title, content, c_time) VALUES (%s, %s, %s, %s);")
        cursor = self.db.cursor()

        ts = self._timestamp()
        cursor.execute(insert, (uid, title, text, ts))
        self.db.commit()
        cursor.close()

    def fetchQuestions(self, start, count):
        query = ("SELECT id, owner_id, content, c_time FROM questions ORDER BY c_time DESC LIMIT %s OFFSET %s;")
        cursor = self.db.cursor()

        ret = []
        cursor.execute(query, (int(count), int(start)))
        for (id, owner_id, content, c_time) in cursor:
            question = Question()
            question.id = id
            question.owner_id = owner_id
            question.content = content
            question.create_time = c_time
            ret.append(question)
        cursor.close()
        return ret

    def insertAnswer(self, uid, q_id, text):
        insert = ("INSERT INTO answers (q_id, owner_id, content, c_time) VALUES (%s, %s, %s, %s);")
        cursor = self.db.cursor()
        
        ts = self._timestamp()
        cursor.execute(insert, (q_id, uid, text, ts))
        self.db.commit()
        cursor.close()

    def fetchAnswers(self, q_id, start, count):
        query = ("SELECT id, owner_id, content, c_time FROM answers WHERE q_id = %s ORDER BY c_time DESC LIMIT %s OFFSET %s ;")
        cursor = self.db.cursor()

        ret = []
        cursor.execute(query, (q_id, int(count), int(start)))
        for (id, owner_id, content, c_time) in cursor:
            answer = Answer()
            answer.id = id
            answer.question_id = q_id
            answer.owner_id = owner_id
            answer.content = content
            answer.create_time = c_time
            ret.append(answer)

        cursor.close()
        return ret

    def fetchMyAnswers(self, uid, start, count):
        query = ("SELECT id, owner_id, q_id, content, c_time FROM answers WHERE owner_id = %s ORDER BY c_time DESC LIMIT %s OFFSET %s ;")
        cursor = self.db.cursor()

        ret = []
        cursor.execute(query, (uid, int(count), int(start)))
        for (id, owner_id, q_id, content, c_time) in cursor:
            answer = Answer()
            answer.id = id
            answer.question_id = q_id
            answer.owner_id = owner_id
            answer.content = content
            answer.create_time = c_time
            ret.append(answer)

        cursor.close()
        return ret