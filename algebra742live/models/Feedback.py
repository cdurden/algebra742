from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    schoology_message_id = db.Column(db.Integer, default=0)
    data_json = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    creator = relationship("User", foreign_keys=[creator_id], back_populates="feedback_given")
    recipient = relationship("User", foreign_keys=[recipient_id], back_populates="feedback_received")
    board = relationship("Board", foreign_keys=[board_id], back_populates="feedback")
    submission = relationship("Submission", foreign_keys=[submission_id], back_populates="feedback")
    task = relationship("Task", foreign_keys=[task_id], back_populates="feedback")

    def get_data(self):
        if self.data_json is not None:
            return json.loads(self.data_json)
        else:
            return {}

def get_feedback(**kwargs):
    feedback = db.session.query(Feedback).filter_by(**kwargs).all()
    return(feedback)

def create_feedback(**kwargs):
    feedback = Feedback(**kwargs)
    db.session.add(feedback)
    db.session.commit()
    return(feedback)

db.Feedback = Feedback
