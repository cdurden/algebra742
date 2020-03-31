from flask import current_app as app
from datetime import datetime
from .. import db
import jinja2
import json
import os
import sys
#from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, RadioField, HiddenField
from wtforms import FormField as FormField_
from wtforms import Form as Form_
from wtforms.utils import unset_value

from flask import url_for
from jinja2.exceptions import TemplateNotFound
from .. import SinglyLinkedList, get_or_create, get
from werkzeug.datastructures import MultiDict, ImmutableMultiDict
import inspect

from networkx.drawing.nx_pydot import read_dot
from ..util import params_hash_lookup, process_quotes_for_json

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader,extensions=['jinja2.ext.with_'])
class TemplateBased(object):
    def traverse_templates(self):
        self.template = None 
        self.macros_template = None 
        if isinstance(self, FormField):
            class_ = self.form_class
        else:
            class_ = self.__class__
        for base_class in inspect.getmro(class_):
            template = "{:s}.html".format(base_class.__name__)
            template_path = os.path.join(loader.searchpath[0], template)
            if os.path.exists(template_path):
                self.template = template 
                break
        for base_class in inspect.getmro(class_):
            macros_template = "{:s}_macros.html".format(base_class.__name__)
            macros_template_path = os.path.join(loader.searchpath[0], macros_template)
            if os.path.exists(macros_template_path):
                self.macros_template = macros_template
                break

class FormField(FormField_,TemplateBased):
    def process(self, formdata, data=unset_value):
        if data is unset_value:
            try:
                data = self.default()
            except TypeError:
                data = self.default
            self._obj = data
        self.object_data = data
        prefix = self.name + self.separator
        if isinstance(data, dict):
            self.form = self.form_class(formdata=formdata, prefix=prefix, csrf_enabled=False, **data)
        else:
            self.form = self.form_class(formdata=formdata, obj=data, prefix=prefix, csrf_enabled=False)
#    def traverse_templates(self):
#        for base_class in inspect.getmro(self.form_class):
#            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.template = "{:s}.html".format(base_class.__name__)
#                return(self.template)
#            else:
#                next
#        self.template = None 
#        return(self.template)
#    def traverse_macros_templates(self):
#        for base_class in inspect.getmro(self.form_class):
#            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
#                return(self.macros_template)
#            else:
#                next
#        self.macros_template = None 
#        return(self.macros_template)

class Form(Form_,TemplateBased):
    question_id = HiddenField('question_id')
    question_class = HiddenField('question_class')

    jinja_env = None
    def render_html(self, **kwargs):
        import inspect
        template = self.jinja_env.get_template(self.template)
        html = template.render(form=self, url_for=url_for, **kwargs)
        return(html)
#    def traverse_templates(self):
#        for base_class in inspect.getmro(self.__class__):
#            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.template = "{:s}.html".format(base_class.__name__)
#                return(self.template)
#            else:
#                next
#        self.template = None 
#        return(self.template)
#    def traverse_macros_templates(self):
#        for base_class in inspect.getmro(self.__class__):
#            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
#                return(self.macros_template)
#            else:
#                next
#        self.macros_template = None 
#        return(self.macros_template)

class AnswerForm(Form):
    answer = StringField('answer')

class MultipleChoiceAnswerForm(Form):
    answer = RadioField('answer')


class TableForm(Form):
    entries = FieldList(StringField('entry'))

class WrittenResponseForm(AnswerForm):
    answer = TextAreaField('answer')

class DrawingForm(Form):
    pass
class AlbusDrawingForm(Form):
    pass
#    background_image_url = None
#    def render_html(self, **kwargs):
#        return Form.render_html(self, background_image_url=self.background_image_url, **kwargs)


class MultiPartAnswerForm(Form):
    pass

def get_question(question_class, question_id):
    question = get(db.session, QuestionClasses[question_class], id=question_id)
    return(question)
#def get_question_from_digraph_node(graph, node):
#    questions_digraph = read_dot(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],graph+'.dot'))
#    node_data = questions_digraph.nodes[node]
#    for k,v in node_data.items():
#        old_val = node_data.pop(k)
#        new_val = process_quotes_for_json(old_val.strip("\"")).strip("\"")
#        node_data[k.strip("\"")] = new_val
#    question = get_or_create(db.session, QuestionClasses[node_data['class']], params_json=node_data['params'], source="question_digraph:{:s}:{:s}".format(graph,node))
#    return(question)
def get_question_from_digraph_node(graph, node):
    questions_digraph = read_dot(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],graph+'.dot'))
    node_data = questions_digraph.nodes[node]
    return get_snow_qm_task(node_data["collection"],node_data["task"])

def get_snow_qm_task(collection_id, task_id):
    print(collection_id)
    print(task_id)
    with open(os.path.join(app.config["SNOW_QM_COLLECTIONS_DIR"],collection_id+'.json')) as f:
        data = json.load(f)
    task_data = data[task_id]
    task_json = json.dumps(task_data)
    task = get_or_create(db.session, QuestionClasses[task_data['class']], params_json=task_json, source="snow-qm:{:s}:{:s}".format(collection_id,task_id))
    return(task)

def questions_digraph_factory(graph):
    questions_digraph = read_dot(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],graph+'.dot'))
    for node,data in questions_digraph.nodes(data=True):
        for k,v in data.items():
        #    data[k.strip("\"")] = data.pop(k).strip("\"").replace("\\","")
            data[k.strip("\"")] = process_quotes_for_json(data.pop(k).strip("\"")).strip("\"")
        question = get_or_create(db.session, QuestionClasses[data['class']], params_json=data['params'], source="question_digraph:{:s}:{:s}".format(graph,node))
        data['_question_obj'] = question
    return(questions_digraph)

class Question(db.Model, TemplateBased):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)
    form_class = AnswerForm
    form = None
    submitted = set() 
    marked_correct = set() 
    marked_incorrect = set() 
    scripts = []

#    def __init__(self, **kwargs):
#        self.params_json = json.dumps(kwargs['params'])
#        super().__init__(self, **kwargs)
    def build_form(self, formdata=None, data=None, prefix=''):
        #self.form = self.form_class(MultiDict(formdata),prefix=prefix)
        print(self.form_class)
        self.form = self.form_class(formdata=MultiDict(formdata),data=data,prefix=prefix)
        self.form.question_id.data = self.id
        self.form.question_class.data = self.__class__.__name__
        #self.form.traverse_templates()
        #self.form.traverse_macros_templates()
        self.form.traverse_templates()
        #self.form.question = self
        #self.form.jinja_env = jinja2.Environment(loader=loader)
        return(self.form)

    def params(self):
        #return(json.loads(process_quotes_for_json(self.params_json)))
        return(json.loads(self.params_json))

    def get_scripts(self):
        #return({'socket.io.wtforms': '/static/js/socket.io.wtforms.js'})
        return(self.scripts)
#    def traverse_templates(self):
#        for base_class in inspect.getmro(self.__class__):
#            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.template = "{:s}.html".format(base_class.__name__)
#                return(self.template)
#            else:
#                next
#        self.template = None 
#        return(self.template)
#    def traverse_macros_templates(self):
#        for base_class in inspect.getmro(self.__class__):
#            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
#            if os.path.exists(path):
#                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
#                return(self.macros_template)
#            else:
#                next
#        self.macros_template = None 
#        return(self.macros_template)

    def render_html(self, **kwargs):
        #print("Rendering question html")
        if self.form is None and self.form_class is not None:
            self.build_form()
        self.traverse_templates()
        #traverse_templates(self)
        #print("Question template: {:s}".format(self.template))
        #print("Form template: {:s}".format(self.form.template))
        #print("Form macros template: {:s}".format(self.form.macros_template))
        template = jinja_env.get_template(self.template)
        html = template.render(params=self.params(), question=self, form=self.form, url_for=url_for, **kwargs)
        return html

    def to_json(self):
        return({
            'scripts': self.get_scripts(),
            'submitted': list(self.submitted),
            'marked_correct': list(self.marked_correct),
            'marked_incorrect': list(self.marked_incorrect),
            'id': self.id,
            'class': self.__class__.__name__
            })

    def score_answer(self):
        return(int(self.check_answer()))

    def record_answer(self, user, score):
        statement = question_scores.insert().values(user_id=user.id, question_id=self.id, answer=json.dumps(self.form.data), score=score)
        db.session.execute(statement)
        db.session.commit()

class MultipleChoiceQuestion(Question):
    form_class = MultipleChoiceAnswerForm
    form = None
    def build_form(self, formdata=None, data=None, prefix=''):
        params = self.params()
        Question.build_form(self, formdata=formdata, data=data, prefix=prefix)
        #self.form.answer.choices = list(zip(range(len(params['choices'])),params['choices']))
        #print(self.form.answer)
        for i in range(len(params['choices'])):
            self.form.answer.choices.append_entry(i,params['choices'][i])
        return(self.form)

    def check_answer(self):
        self.marked_correct = set()
        self.marked_incorrect = set()
        params = self.params()
        if self.form.answer.data==str(params['answer']):
            self.marked_correct.add('answer')
            return True
        else:
            self.marked_incorrect.add('answer')
            return False

class CompleteTableQuestion(Question):
    form_class = TableForm
    form = None
    df = None
    def load_csv(self):
        import pandas as pd
        from io import StringIO
        import re
        params = self.params()
        s = StringIO(params['csv'])
        self.df = pd.read_csv(s)
        self.missing_entries = []
        for column in self.df.columns:
            for row,entry in enumerate(self.df[column]):
                if re.match("^\[.+\]$",str(entry)):
                    #print(str(entry))
                    self.missing_entries.append((row,column))

    def render_html(self, **kwargs):
        if self.df is None:
            self.load_csv()
        params = self.params()
        transpose_display = 'transpose_display' in params and params['transpose_display'] in ["true","True",True]
        #print(params['transpose_display'])
        return Question.render_html(self, missing_entries=self.missing_entries, transpose_display=transpose_display, **kwargs)
    def build_form(self, formdata=None, data=None):
        if self.df is None:
            self.load_csv()
        Question.build_form(self, formdata=formdata, data=data)
        while len(self.form.entries) < len(self.missing_entries):
            self.form.entries.append_entry()
        return(self.form)
    def check_answer(self):
        from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
        from sympy import symbols
        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
        if self.df is None:
            self.load_csv()
        self.marked_correct = set()
        self.marked_incorrect = set()
        #print("checking answers")
        #print(self.form.data)
        for (row,column) in self.missing_entries:
            try:
                answer = parse_expr(str(self.df.loc[row,column]).strip("[]"),transformations=transformations)
                answer_input = parse_expr(self.form.entries.entries[self.missing_entries.index((row,column))].data, transformations=transformations)
                correct = bool(answer-answer_input==0)
            except:
                correct = False
            if correct:
                self.marked_correct.add(self.form.entries.entries[self.missing_entries.index((row,column))].name)
            else:
                self.marked_incorrect.add(self.form.entries.entries[self.missing_entries.index((row,column))].name)
        return len(self.marked_correct)==len(self.missing_entries)

class CompleteTableDraggableQuestion(CompleteTableQuestion):
    scripts = ["/static/teaching_assets/slides/js/jquery-ui-1.12.1/jquery-ui.min.js"]
    #scripts = ["https://cdn.jsdelivr.net/npm/@shopify/draggable@1.0.0-beta.8/lib/draggable.bundle.js"]

class DrawingQuestion(Question):
    form_class = DrawingForm
    form = None
    def build_form(self, formdata=None, data=None):
        Question.build_form(self, formdata=formdata, data=data)
        return(self.form)

class AlbusDrawingQuestion(Question):
    form_class = AlbusDrawingForm
    form = None
    def build_form(self, formdata=None, data=None):
        Question.build_form(self, formdata=formdata, data=data)
        return(self.form)

class GraphicsQuestion(Question):
    form_class = AnswerForm
    form = None

    def render_html(self, **kwargs):
        params = self.params()
        params_hash = params_hash_lookup(self.params_json)
        return Question.render_html(self, template=params['template'], params_hash=params_hash, **kwargs)

class AsyGraphicsQuestion(GraphicsQuestion):
    def render_html(self, **kwargs):
        return GraphicsQuestion.render_html(self, engine="asy")

class AsyGraphicsDrawingQuestion(DrawingQuestion):
    def render_html(self, **kwargs):
        params = self.params()
        params_hash = params_hash_lookup(self.params_json)
        return Question.render_html(self, template=params['template'], params_hash=params_hash, **kwargs)

class DotGraphicsQuestion(GraphicsQuestion):
    def render_html(self, **kwargs):
        return GraphicsQuestion.render_html(self, engine="dot")


class MultiPartQuestion(Question):
    form_class = MultiPartAnswerForm
    form = None
    parts = None

    def build_parts(self):
        self.parts = []
        import importlib
        params = self.params()
        for i,part in enumerate(params['parts']):
            #module_class_string = part['class']
            #module_name, class_name = module_class_string.rsplit(".", 1)
            class_name = part['class']
            module = importlib.import_module('..Question', package=__name__)
            question_class = getattr(module, class_name)
            part['params_json'] = json.dumps(part)
            question = get_or_create(db.session, question_class, params_json=part['params_json'])
            self.parts.append(question)
        for i,part in enumerate(self.parts):
            part.traverse_templates()
            #part.macros_template = part.traverse_macros_templates()
            #print("Part macros template: {:s}".format(part.macros_template))

    def get_scripts(self):
        params = self.params()
        scripts = []
        for i,part in enumerate(params['parts']):
            scripts += getattr(sys.modules[__name__], part['class']).scripts
        return(scripts)

    def build_form(self, formdata=None, data=None):
        self.build_parts()
        class DynamicMultiPartAnswerForm(MultiPartAnswerForm):
            pass
        self.form_class = DynamicMultiPartAnswerForm
        for i,part in enumerate(self.parts):
            setattr(self.form_class, 'part_{:d}'.format(i), FormField(part.form_class))
        #print("build_form formdata checkpoint")
        #print(formdata)
        Question.build_form(self, formdata=formdata, data=data)
        #self.form = self.form_class(formdata=formdata)
        self.form.traverse_templates()
        self.form.question = self
        # FIXME: this throws an error when created before submission
        #self.form.validate()
        for i,part in enumerate(self.parts):
            part.build_form(formdata=formdata, data=data, prefix='part_{:d}'.format(i))
            #part.form = getattr(self.form, 'part_{:d}'.format(i))
            # thought about doing some updating of the big form based on subforms
            #destination.__dict__.update(source.__dict__)
            #for (attr in part.form.__dict__) {
            #    if(isinstance(part.form.__dict__[attr],Field)) {
            #        self.form.__dict__[attr] = 
            #    }
            #}
            #part.form.traverse_templates()
            #print(part.form.data)
        return(self.form)

    def render_html(self, **kwargs):
        if self.form is None:
            self.build_form()
        #for part in self.parts:
            #print(part.__class__.__name__)
        return Question.render_html(self, parts=self.parts, **kwargs)
    
    def check_answer(self):
        #print(self.form.data)
        self.marked_correct = set()
        self.marked_incorrect = set()
        for i,part in enumerate(self.parts):
            part.check_answer()
            self.marked_correct = self.marked_correct.union(set(["part_{:d}-{:s}".format(i,field) for field in part.marked_correct]))
            self.marked_incorrect = self.marked_incorrect.union(set(["part_{:d}-{:s}".format(i,field) for field in part.marked_incorrect]))
            self.submitted = self.submitted.union(set(["part_{:d}-{:s}".format(i,field) for field in part.submitted]))
        return all([part.check_answer() for i,part in enumerate(self.parts)])


class QuestionOnePlusOne(Question):
    form_class = AnswerForm
    form = None

    def build_form(self, formdata=None, data=None):
        self.form = self.form_class(formdata=MultiDict(formdata),data=data)
        #print('building QuestionOnePlusOne form')
        #print(self.form.data)
        return(self.form)

    def check_answer(self):
        #print(self.form.answer.data)
        self.marked_correct = set()
        self.marked_incorrect = set()
        if self.form.answer.data=='2':
            self.marked_correct.add('answer')
            return True
        else:
            self.marked_incorrect.add('answer')
            return False

class SolutionQuestion(Question):
    def render_html(self, **kwargs):
        params = self.params()
        return Question.render_html(self, Question="${:s}$".format(params['statement']), **kwargs)
    def check_answer(self):
        from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
        from sympy import symbols
        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
        x = symbols("x")
        params = self.params()
        try:
            #print(self.form.data)
            expr = parse_expr(params['statement'],transformations=transformations).subs(x,parse_expr(self.form.answer.data))
            #print(expr)
            correct = bool(expr)
        except SyntaxError:
            correct = False
        self.marked_correct = set()
        self.marked_incorrect = set()
        if correct:
            self.marked_correct.add('answer')
        else:
            self.marked_incorrect.add('answer')
        return(correct)

class NonSolutionQuestion(Question):
    def render_html(self, **kwargs):
        params = self.params()
        return Question.render_html(self, Question="${:s}$".format(params['statement']), **kwargs)
    def check_answer(self):
        from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
        from sympy import symbols
        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
        x = symbols("x")
        params = self.params()
        try:
            expr = parse_expr(params['statement']).subs(x,parse_expr(self.form.answer.data))
            correct = not bool(expr)
        except:
            correct = False
        self.marked_correct = set()
        self.marked_incorrect = set()
        if correct:
            self.marked_correct.add('answer')
        else:
            self.marked_incorrect.add('answer')
        return(correct)

class OpenEndedQuestion(Question):
    form_class = WrittenResponseForm
    form = None

    def check_answer(self):
        self.submitted = set(['answer'])
        return(True)

QuestionClasses = {
    'CompleteTableQuestion': CompleteTableQuestion,
    'CompleteTableDraggableQuestion': CompleteTableDraggableQuestion,
    'OpenEndedQuestion': OpenEndedQuestion,
    'MultipleChoiceQuestion': MultipleChoiceQuestion,
    'SolutionQuestion': SolutionQuestion,
    'NonSolutionQuestion': NonSolutionQuestion,
    'MultiPartQuestion': MultiPartQuestion,
    'QuestionOnePlusOne': QuestionOnePlusOne,
    'DrawingQuestion': DrawingQuestion,
    'AsyGraphicsQuestion': AsyGraphicsQuestion,
    'DotGraphicsQuestion': DotGraphicsQuestion,
    'AsyGraphicsDrawingQuestion': AsyGraphicsDrawingQuestion,
}

question_scores = db.Table('question_scores',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('score', db.Float),
    db.Column('answer', db.Text),
    db.Column('datetime', db.DateTime, nullable=False,
        default=datetime.utcnow)
)
