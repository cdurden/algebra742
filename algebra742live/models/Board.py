from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship
from sqlalchemy import desc

class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    boardId = db.Column(db.String(6))
    background_image = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    #submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    title = db.Column(db.Text)
    shapeStorage_json = db.Column(db.String(16777215))
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    user = relationship("User", back_populates="boards")
    task = relationship("Task")
    feedback = relationship("Feedback", back_populates="board")
    submissions = relationship("Submission", back_populates="board")

    def get_shapeStorage(self):
        return json.loads(self.shapeStorage_json)

def get_boards():
    boards = db.session.query(Board).all()
    return(boards)

def get_boards_by_task_id(task_id):
    boards = db.session.query(Board).filter_by(task_id=task_id).order_by(desc(Board.datetime)).all()
    return(boards)

def get_latest_board_by_task_id(task_id):
    board = db.session.query(Board).filter_by(task_id=task_id).order_by(desc(Board.datetime)).first()
    return(board)

def get_board_by_id(board_id):
    board = db.session.query(Board).get(board_id)
    return(board)

def get_latest_board(**kwargs):
    board = db.session.query(Board).filter_by(**kwargs).order_by(desc(Board.datetime)).first()
    return(board)

db.Board = Board
