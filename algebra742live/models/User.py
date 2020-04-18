from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship
from .Submission import Submission

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(255), unique=True, nullable=False)

    submissions = relationship("Submission", back_populates="user")
    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return({ 'id': self.id,
                 'username': self.username,
                 'firstname': self.firstname,
                 'lastname': self.lastname,
                 'lti_user_id': self.lti_user_id })
    def submit(self, task, data):
        submission = Submission(user_id=self.id, task_id=task.id, data=json.dumps(data))
        db.session.add(submission)
        db.session.commit()
        return(submission)
    def save_board(self, data, task_id=None):
        if task_id is None:
            board = db.Board(user_id=self.id, data=json.dumps(data))
        else: 
            board = db.Board(user_id=self.id, task_id=task_id, data=json.dumps(data))
        db.session.add(board)
        db.session.commit()
        return(board)
    def get_latest_board_by_task_id(self, task_id):
        board = db.session.query(Board).filter_by(user_id=self.id, task_id=task_id).order_by(desc(Board.datetime)).first()
        return(board)


def get_user_by_lti_user_id(lti_user_id):
    instance = db.session.query(User).filter_by(lti_user_id=lti_user_id).first() # TODO: ensure unique
    return instance

db.User = User
