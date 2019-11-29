from datetime import datetime
from .. import db
import jinja2
import json
import os
from flask_wtf import Form
from wtforms import StringField
from flask import url_for
from jinja2.exceptions import TemplateNotFound
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader)

class AnswerForm(Form):
    answer = StringField('answer')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)

    def scripts(self):
        return({'socket.io.wtforms': '/static/js/socket.io.wtforms.js'})

    def render_html(self):
        form = AnswerForm()
        import inspect
        for base_class in inspect.getmro(self):
            try:
                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
            except TemplateNotFound:
                next 
            return template.render(json.loads(self.params_json), form=form)


class QuestionOnePlusOne(Question):
    def check_answer(self, formdata):
        return(formdata.answer==2)

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
