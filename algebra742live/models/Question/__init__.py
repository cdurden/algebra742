from datetime import datetime
from .. import db
import jinja2
import json
import os
from flask import url_for
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader)

class AnswerForm(Form):
    answer = StringField('answer')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)

    def render_html(self):
        form = AnswerForm()
        template = jinja_env.get_template("{:s}.html".format(self.__class__.__name__))
        return template.render(json.loads(self.params_json), form=form)

class PlotQuestion(Question):
    def scripts(self):
        #return({'canvasjs': "https://canvasjs.com/assets/script/canvasjs.min.js", 'plot': url_for('static',filename='js/plot.js')})
        return({'canvasjs': "https://canvasjs.com/assets/script/canvasjs.min.js", 'plot': '/static/js/plot.js'})

question_scores = db.Table('question_scores',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('score', db.Float),
    db.Column('answer', db.Text),
    db.Column('datetime', db.DateTime, nullable=False,
        default=datetime.utcnow)
)
