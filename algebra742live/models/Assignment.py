from flask import current_app as app
from datetime import datetime
from .. import db
import json
import re # for matching source patterns to assignment collections and assignments
import os # for reading assignment collection files
from sqlalchemy.orm import relationship
from . import get_or_create
from .Message import Message
from .Board import Board

class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    student = relationship("User", foreign_keys=[student_id], back_populates="assignments_received")
    director = relationship("User", foreign_keys=[director_id], back_populates="assignments_given")

def get_assignments():
    assignments = db.session.query(Assignment).all()
    return(assignments)

def get_assignment_by_id(assignment_id):
    assignment = db.session.query(Assignment).get(assignment_id)
    return(assignment)

db.Assignment = Assignment
