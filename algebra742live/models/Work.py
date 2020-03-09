from . import User
from .. import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    template = db.Column(db.Text)
    data = db.Column(db.Text)
    user = db.relationship("User")
