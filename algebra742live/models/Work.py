from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship

class Work(db.Model):
    __tablename__ = 'work'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)
    marked_correct = db.Column(db.Text)
    marked_incorrect = db.Column(db.Text)

    #user = relationship("User", back_populates="works")
    #task = relationship("Task", back_populates="works")

    def to_json(self):
        return({
            'id': self.id,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'submission_id': self.submission_id,
            'data': self.data,
            'datetime': self.datetime,
            })

def get_work_by_id(work_id):
    work = db.session.query(Work).get(work_id)
    return(work)

def get_works():
    works = db.session.query(Work).all()
    return(works)
