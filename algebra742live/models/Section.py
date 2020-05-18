from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schoology_id = db.Column(db.Integer)
    description = db.Column(db.String(80))

    def __repr__(self):
        return '<Section %r>' % self.description

def get_sections():
    sections = db.session.query(Section).all()
    return sections

def get_section_by_id(section_id):
    instance = db.session.query(Section).get(section_id) # TODO: ensure unique
    return instance


db.Section = Section


