from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship
from .Submission import Submission
from .Feedback import Feedback
#from .Board import get_board_by_boardId

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), default="student")
    assignment = db.Column(db.String(80))
    section = db.Column(db.String(80))

    boards = relationship("Board", back_populates="user")
    submissions = relationship("Submission", back_populates="user")
    messages = relationship("Message", back_populates="user")
    feedback_given = relationship("Feedback", foreign_keys=[Feedback.creator_id], back_populates="creator")
    feedback_received = relationship("Feedback", foreign_keys=[Feedback.recipient_id], back_populates="recipient")

    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return({ 'id': self.id,
                 'username': self.username,
                 'firstname': self.firstname,
                 'lastname': self.lastname,
                 'lti_user_id': self.lti_user_id })
    def submit(self, task, data, board_id=None):
        submission = Submission(user_id=self.id, task_id=task.id, data=json.dumps(data), board_id=board_id)
        db.session.add(submission)
        db.session.commit()
        return(submission)
    def save_board(self, data, boardId, task_id=None, background_image=None):
        print(type(data))
        print(data.keys())
        board = self.get_board_by_boardId(boardId)
        if board is not None:
            board.data_json = json.dumps(data)
            board.task_id = task_id
            board.background_image = background_image
        else:
            if task_id is None:
                board = db.Board(user_id=self.id, boardId=boardId, data_json=json.dumps(data), background_image=background_image)
            else: 
                board = db.Board(user_id=self.id, boardId=boardId, task_id=task_id, data_json=json.dumps(data), background_image=background_image)
            db.session.add(board)
        db.session.commit()
        return(board)
    def create_feedback(self, board, recipient, task):
        db.session.add(board)
        db.session.commit()
        feedback = db.Feedback(board_id=board.id, recipient_id=recipient.id, creator_id=self.id, task_id=task.id)
        db.session.add(feedback)
        db.session.commit()
        return(feedback)
    def get_board_by_boardId(boardId):
        board = db.session.query(Board).filter_by(user_id=self.id, boardId=boardId).first()
        return(board)

    def get_latest_board_by_task_id(self, task_id):
        board = db.session.query(Board).filter_by(user_id=self.id, task_id=task_id).order_by(desc(Board.datetime)).first()
        return(board)

def get_users():
    users = db.session.query(User).all()
    return users

def get_user_by_id(user_id):
    instance = db.session.query(User).get(user_id) # TODO: ensure unique
    return instance

def get_user_by_lti_user_id(lti_user_id):
    instance = db.session.query(User).filter_by(lti_user_id=lti_user_id).first() # TODO: ensure unique
    return instance

db.User = User
