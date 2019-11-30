from datetime import datetime
from .. import db
import jinja2
import json
import os
from flask_wtf import Form
from wtforms import StringField, FormField
from flask import url_for
from jinja2.exceptions import TemplateNotFound
from .. import SinglyLinkedList, get_or_create
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader)

class AnswerForm(Form):
    answer = StringField('answer')

#    def __init__(self, **kwargs):
#        super().__init__(self, **kwargs)

#    def render_html(self):
#        import inspect
#        for base_class in inspect.getmro(self.__class__):
#            try:
#                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
#                return template.render(json.loads(self.params_json), form=form)
#            except TemplateNotFound:
#                next 

class MultiPartAnswerForm(Form):
    pass
#    def render_html(self):
#        import inspect
#        for base_class in inspect.getmro(self.__class__):
#            try:
#                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
#                return template.render(json.loads(self.params_json), form=form)
#            except TemplateNotFound:
#                next 


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)
    form_class = AnswerForm

    def scripts(self):
        return({'socket.io.wtforms': '/static/js/socket.io.wtforms.js'})

    def render_html(self, form=None):
        import inspect
        if form is None:
            form = self.form_class()
        for base_class in inspect.getmro(self.__class__):
            try:
                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
                return template.render(json.loads(self.params_json), form=form)
            except TemplateNotFound:
                next 

class MultiPartQuestion(Question):
    form_class = MultiPartAnswerForm

    def render_html(self, form=None):
        params = json.loads(self.params_json)
        import importlib
#        questions = SinglyLinkedList()
        class F(MultiPartAnswerForm):
            pass
        for i,part in enumerate(params['parts']):
            module_class_string = part['class']
            module_name, class_name = module_class_string.rsplit(".", 1)
            #module = importlib.import_module(module_name, package='algebra742.algebra742live.models')
            module = importlib.import_module('..' + module_name, package=__name__)
            class_ = getattr(module, class_name)
            question = get_or_create(db.session, class_, params_json=part['params_json'])
#            questions.append(question)
            #params['parts'][i]['question'] = question
            part['question'] = question
            setattr(F, 'part_{:d}'.format(i), FormField(question.form_class))
        setattr(F, 'n', len(params['parts']))
        form = F()
        import inspect
        for base_class in inspect.getmro(self.__class__):
            try:
                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
                return template.render(params, form=form)
            except TemplateNotFound:
                next 
    


class QuestionOnePlusOne(Question):
    def check_answer(self, formdata):
        return(formdata['answer']=='2')

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
