from flask import current_app as app
from datetime import datetime
from .. import db
import json

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    data = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    def to_json(self):
        return({
            'id': self.id,
            'submission_id': self.submission_id,
            'data': self.data,
            'datetime': self.datetime.isoformat(),
            })
