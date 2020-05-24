from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship

class SubmissionBox(db.Model):
    __tablename__ = 'submissionbox'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Text)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    recipient = relationship("User", back_populates="inboxes")

def get_submissionbox_by_id(submissionbox_id):
    submissionbox = db.session.query(SubmissionBox).get(submissionbox_id)
    return(submissionbox)

def get_submissionboxes(**kwargs):
    submissionboxs = db.session.query(SubmissionBox).filter_by(**kwargs).all()
    return(submissionboxes)

db.SubmissionBox = SubmissionBox
