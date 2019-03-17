import mysql.connector
from models import Question, Answer
from flask import current_app

class Database:

    def __init__(self, name):
        self.db = mysql.connector.connect(user='root', database=name)

    def close(self):
        if self.db is not None:
            self.db.close()

    def login(self, open_id):
        query = ("SELECT id, name FROM users WHERE open_id = %s;")
        cursor = self.db.cursor()

        cursor.execute(query, (open_id))
        ret = cursor.fetchone()
        cursor.close()
        return ret

    def insertQuestion(self, uid, text):
        insert = ("INSERT INTO questions (owner_id, content) VALUES (%s, %s);")
        cursor = self.db.cursor()

        cursor.execute(insert, (uid, text))
        cursor.commit()
        cursor.close()

    def fetchQuestions(self, start, count):
        query = ("SELECT id, owner_id, content, c_time FROM questions ORDER BY c_time DESC OFFSET %s LIMIT %s;")
        cursor = self.db.cursor()

        ret = []
        cursor.execute(query, (start, count))
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
        insert = ("INSERT INTO answers (q_id, owner_id, content) VALUES (%s, %s, %s);")
        cursor = self.db.cursor()
        
        cursor.execute(insert, (q_id, uid, text))
        cursor.commit()
        cursor.close()

    def fetchAnswer(self, q_id, start, count):
        query = ("SELECT id, owner_id, content, c_time FROM answers WHERE q_id = %s ORDER BY c_time DESC OFFSET %s LIMIT %s;")
        cursor = self.db.cursor()

        ret = []
        cursor.execute(query, (q_id, start, count))
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