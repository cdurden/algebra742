from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    user = relationship("User", back_populates="messages")
    task = relationship("Task", back_populates="messages")

    def check():
        pass

    def to_json(self):
        return({
            'id': self.id,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'data': self.data,
            'datetime': self.datetime.isoformat(),
            'user': self.user.to_json(),
            'task': self.task.to_json(),
            })

def get_message_by_id(message_id):
    message = db.session.query(Message).get(message_id)
    return(message)

def get_messages(**kwargs):
    messages = db.session.query(Message).filter_by(**kwargs).all()
    return(messages)
