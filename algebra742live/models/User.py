from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship
from .Submission import Submission
from .Feedback import Feedback
from .Board import Board
from .Assignment import Assignment

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(80), unique=True, nullable=False)
    schoology_message_thread_id = db.Column(db.BigInteger)
    role = db.Column(db.String(80), default="student")
    assignment = db.Column(db.String(80))
    section = db.Column(db.String(80))

    inboxes = relationship("SubmissionBox", back_populates="recipient")
    boards = relationship("Board", back_populates="user")
    submissions = relationship("Submission", back_populates="user")
    messages = relationship("Message", back_populates="user")
    assignments_given = relationship("Assignment", foreign_keys=[Assignment.director_id], back_populates="director")
    assignments_received = relationship("Assignment", foreign_keys=[Assignment.student_id], back_populates="student")
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
    def save_board(self, shapeStorage_json, boardId, task=None, background_image=None):
        print("Saving board {:s} with shapeStorage:".format(boardId));
        print(shapeStorage_json)
        board = self.get_board_by_boardId(boardId)
        if board is not None:
            #board.shapeStorage_json = json.dumps(data)
            board.shapeStorage_json = shapeStorage_json
            if background_image is not None:
                board.background_image = background_image
        else:
            if task is None:
                board = db.Board(user_id=self.id, boardId=boardId, shapeStorage_json=shapeStorage_json, background_image=background_image)
                #board = db.Board(user_id=self.id, boardId=boardId, data_json=json.dumps(data), background_image=background_image)
            else: 
                board = db.Board(user_id=self.id, boardId=boardId, task_id=task.id, shapeStorage_json=shapeStorage_json, background_image=background_image)
                #board = db.Board(user_id=self.id, boardId=boardId, task_id=task_id, data_json=json.dumps(data), background_image=background_image)
            db.session.add(board)
        db.session.commit()
        return(board)
    def create_feedback(self, submission, board, data_json):
        db.session.add(board)
        db.session.commit()
        feedback = db.Feedback(submission_id=submission.id, board_id=board.id, recipient_id=submission.user.id, creator_id=self.id, task_id = submission.task_id, data_json=data_json)
        db.session.add(feedback)
        db.session.commit()
        return(feedback)
    def get_board_by_boardId(self, boardId):
        board = db.session.query(Board).filter_by(user_id=self.id, boardId=boardId).first()
        return(board)

    def get_latest_board_by_task_id(self, task_id):
        board = db.session.query(Board).filter_by(user_id=self.id, task_id=task_id).order_by(desc(Board.datetime)).first()
        return(board)
    def get_feedback_received(self, board_ids):
        if board_ids is not None:
            feedback_list = db.session.query(Feedback).filter(Feedback.board_id.in_(board_ids)).filter_by(user_id=self.id).all()
        else:
            feedback_list = db.session.query(Feedback).filter_by(user_id=self.id).all()
        return(feedback_list)


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
