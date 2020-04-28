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
    board_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)
    graded = db.Column(db.Boolean, default=False)
    score = db.Column(db.Float)
    marked_correct = db.Column(db.Text, default="[]")
    marked_incorrect = db.Column(db.Text, default="[]")

    user = relationship("User", back_populates="submissions")
    task = relationship("Task", back_populates="submissions")
    feedback = relationship("Feedback", back_populates="submission")
    board = relationship("Board", back_populates="submissions")

    def check():
        pass

    def to_json(self):
        return({
            'id': self.id,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'data': self.data,
            'datetime': self.datetime.isoformat(),
            'graded': self.graded,
            'score': self.score,
            'marked_correct': json.loads(self.marked_correct),
            'marked_incorrect': json.loads(self.marked_incorrect),
            'user': self.user.to_json(),
            'task': self.task.to_json(),
            'feedback': [feedback.to_json() for feedback in self.feedback],
            })

def get_submission_by_id(submission_id):
    submission = db.session.query(Submission).get(submission_id)
    return(submission)

def get_submissions(**kwargs):
    submissions = db.session.query(Submission).filter_by(**kwargs).all()
    #submissions = db.session.query(Submission).all()
    return(submissions)

db.Submission = Submission
