from datetime import datetime
from ..models import db
import jinja2
import json
import os
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)

    def render_html(self):
        template = jinja_env.get_template(self.__class__.__name__)
        return template.render(json.loads(self.params_json))

question_scores = db.Table('question_scores',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('score', db.Float),
    db.Column('answer', db.Text),
    db.Column('datetime', db.DateTime, nullable=False,
        default=datetime.utcnow)
)