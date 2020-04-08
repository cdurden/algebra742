from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship

class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)
    graded = db.Column(db.Boolean, default=False)
    score = db.Column(db.Float)
    marked_correct = db.Column(db.Text)
    marked_incorrect = db.Column(db.Text)

    #user = relationship("User", back_populates="submissions")
    task = relationship("Task", back_populates="submissions")

    def check():
        pass

    def to_json(self):
        return({
            'id': self.id,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'data': self.data,
            'datetime': self.datetime,
            })

def get_task_by_id(task_id):
    task = db.session.query(Task).get(task_id)
    return(task)

def get_submissions():
    submissions = db.session.query(Submissions).all()
    return(submissions)
