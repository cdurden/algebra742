from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship


class Assessment(db.Model):
    __tablename__ = 'assessment'
    id = db.Column(db.Integer, primary_key=True)
    objective_id = db.Column(db.Integer, db.ForeignKey('objective.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #assessor_id = db.Column(db.Integer, db.ForeignKey('assessor.id'))
    achievement_data_json = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False,
                    default=datetime.utcnow)

    def get_data(self):
        if self.achievment_data_json is not None:
            return json.loads(self.achievement_data_json)
        else:
            return {}

def get_assessments(objective_ids, **kwargs):
    if objective_ids is not None:
        assessment = db.session.query(Assessment).filter(Assessment.objective_id.in_(objective_ids)).filter_by(**kwargs).all()
    else:
        assessment = db.session.query(Assessment).filter_by(**kwargs).all()
    return(assessment)

def get_assessment_by_id(assessment_id):
    assessment = db.session.query(Assessment).get(assessment_id)
    return(assessment)

def create_assessment(**kwargs):
    assessment = Assessment(**kwargs)
    db.session.add(assessment)
    db.session.commit()
    return(assessment)

db.Assessment = Assessment
