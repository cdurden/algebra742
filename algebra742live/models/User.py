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


def get_user_by_lti_user_id(lti_user_id):
    instance = db.session.query(User).filter_by(lti_user_id=lti_user_id).first() # TODO: ensure unique
    return instance

db.User = User
