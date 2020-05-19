from flask import current_app as app
from datetime import datetime
from .. import db
import json
from sqlalchemy.orm import relationship


class Objective(db.Model):
    __tablename__ = 'objective'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(65000))
    #standard_id = db.Column(db.Integer, db.ForeignKey('standard.id'))

    def get_data(self):
        if self.achievment_data_json is not None:
            return json.loads(self.achievement_data_json)
        else:
            return {}

def get_objectives(standard_ids, **kwargs):
    if standard_ids is not None:
        objectives = db.session.query(Objective).filter(Objective.standard_id.in_(standard_ids)).filter_by(**kwargs).all()
    else:
        objectives = db.session.query(Objective).filter_by(**kwargs).all()
    return(objectives)

def get_objective_by_id(objective_id):
    objective = db.session.query(Objective).get(objective_id)
    return(objective)

def create_objective(**kwargs):
    objective = Objective(**kwargs)
    db.session.add(objective)
    db.session.commit()
    return(objective)

db.Objective = Objective
