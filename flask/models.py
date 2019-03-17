
class Question:
    id = 0
    owner_id = 0
    content = ""
    create_time = 0

    def serialize(self):
        return {
            'id': self.id, 
            'owner_id': self.owner_id,
            'content': self.content,
            'create_time': self.create_time
        }

class Answer:
    id = 0
    owner_id = 0
    question_id = 0
    content = ""
    create_time = 0

    def serialize(self):
        return {
            'id': self.id, 
            'owner_id': self.owner_id,
            'question_id': self.question_id,
            'content': self.content,
            'create_time': self.create_time
        }