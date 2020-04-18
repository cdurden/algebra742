from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship
from sqlalchemy import desc

class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    title = db.Column(db.Text)
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)
    marked_correct = db.Column(db.Text)
    marked_incorrect = db.Column(db.Text)

    #user = relationship("User", back_populates="boards")
    #task = relationship("Task", back_populates="boards")

    def to_json(self):
        return({
            'id': self.id,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'submission_id': self.submission_id,
            'data': self.data,
            'datetime': self.datetime.isoformat(),
            })

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
