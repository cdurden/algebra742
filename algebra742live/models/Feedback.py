from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    submission = relationship("Submission", back_populates="feedback")
    user = relationship("User", back_populates="feedback")
    task = relationship("Task", back_populates="feedback")
    board = relationship("Board", back_populates="feedback")

def get_feedback(**kwargs):
    feedback = db.session.query(Feedback).filter_by(**kwargs).all()
    return(feedback)

def create_feedback(**kwargs):
    feedback = Feedback(**kwargs)
    db.session.add(feedback)
    db.session.commit()
    return(feedback)

