from flask import current_app as app
from datetime import datetime
from .. import db
import jinja2
import json
import os
#from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList
from wtforms import FormField as FormField_
from wtforms import Form as Form_
from wtforms.utils import unset_value

from flask import url_for
from jinja2.exceptions import TemplateNotFound
from .. import SinglyLinkedList, get_or_create
from werkzeug.datastructures import MultiDict, ImmutableMultiDict
import inspect

from networkx.drawing.nx_pydot import read_dot
from ..util import params_hash_lookup, process_quotes_for_json

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader,extensions=['jinja2.ext.with_'])

class FormField(FormField_):
    def process(self, formdata, data=unset_value):
        if data is unset_value:
            try:
                data = self.default()
            except TypeError:
                data = self.default
            self._obj = data
        self.object_data = data
        prefix = self.name + self.separator
        print("prefix: {:s}".format(prefix))
        if isinstance(data, dict):
            self.form = self.form_class(formdata=formdata, prefix=prefix, csrf_enabled=False, **data)
        else:
            self.form = self.form_class(formdata=formdata, obj=data, prefix=prefix, csrf_enabled=False)
    def traverse_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
            if os.path.exists(path):
                self.template = "{:s}.html".format(base_class.__name__)
                return(self.template)
            else:
                next
        self.template = None 
        return(self.template)
    def traverse_macros_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
            if os.path.exists(path):
                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
                return(self.macros_template)
            else:
                next
        self.macros_template = None 
        return(self.macros_template)

class Form(Form_):
    jinja_env = None
    def render_html(self, **kwargs):
        import inspect
        template = self.jinja_env.get_template(self.traverse_templates())
        html = template.render(form=self, url_for=url_for, **kwargs)
        return(html)
    def traverse_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
            if os.path.exists(path):
                self.template = "{:s}.html".format(base_class.__name__)
                return(self.template)
            else:
                next
        self.template = None 
        return(self.template)
    def traverse_macros_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
            if os.path.exists(path):
                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
                return(self.macros_template)
            else:
                next
        self.macros_template = None 
        return(self.macros_template)

class AnswerForm(Form):
    answer = StringField('answer')
#    def __init__(self, **kwargs):
#        super().__init__(self, **kwargs)

class TableForm(Form):
    entries = FieldList(StringField('entry'))

class WrittenResponseForm(Form):
    answer = TextAreaField('answer')

class DrawingForm(Form):
    pass
#    background_image_url = None
#    def render_html(self, **kwargs):
#        return Form.render_html(self, background_image_url=self.background_image_url, **kwargs)


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

def get_question_from_digraph_node(graph, node):
    questions_digraph = read_dot(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],graph+'.dot'))
    node_data = questions_digraph.nodes[node]
    for k,v in node_data.items():
    #    node_data[k.strip("\"")] = node_data.pop(k).strip("\"").replace("\\","")
        old_val = node_data.pop(k)
        new_val = process_quotes_for_json(old_val.strip("\"")).strip("\"")
        node_data[k.strip("\"")] = new_val
    question = get_or_create(db.session, QuestionClasses[node_data['class']], params_json=node_data['params'], source="question_digraph:{:s}:{:s}".format(graph,node))
    return(question)

def questions_digraph_factory(graph):
    questions_digraph = read_dot(os.path.join(app.config["QUESTION_DIGRAPHS_DIR"],graph+'.dot'))
    for node,data in questions_digraph.nodes(data=True):
        for k,v in data.items():
        #    data[k.strip("\"")] = data.pop(k).strip("\"").replace("\\","")
            data[k.strip("\"")] = process_quotes_for_json(data.pop(k).strip("\"")).strip("\"")
        question = get_or_create(db.session, QuestionClasses[data['class']], params_json=data['params'], source="question_digraph:{:s}:{:s}".format(graph,node))
        data['_question_obj'] = question
    return(questions_digraph)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)
    form_class = AnswerForm
    form = None
    marked_correct = set() 
    marked_incorrect = set() 

#    def __init__(self, **kwargs):
#        self.params_json = json.dumps(kwargs['params'])
#        super().__init__(self, **kwargs)
    def build_form(self, formdata=None):
        print(formdata)
        self.form = self.form_class(MultiDict(formdata))
        self.form.traverse_templates()
        self.form.traverse_macros_templates()
        self.form.question = self
        #self.form.jinja_env = jinja2.Environment(loader=loader)
        print('building Question form')
        print(self.form.data)
        return(self.form)

    def params(self):
        print(self.params_json)
        #return(json.loads(process_quotes_for_json(self.params_json)))
        return(json.loads(self.params_json))

    def scripts(self):
        #return({'socket.io.wtforms': '/static/js/socket.io.wtforms.js'})
        return(['/static/js/socket.io.wtforms.js'])
    def traverse_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}.html".format(base_class.__name__))
            if os.path.exists(path):
                self.template = "{:s}.html".format(base_class.__name__)
                return(self.template)
            else:
                next
        self.template = None 
        return(self.template)
    def traverse_macros_templates(self):
        for base_class in inspect.getmro(self.__class__):
            path = os.path.join(loader.searchpath[0], "{:s}_macros.html".format(base_class.__name__))
            if os.path.exists(path):
                self.macros_template = "{:s}_macros.html".format(base_class.__name__)
                return(self.macros_template)
            else:
                next
        self.macros_template = None 
        return(self.macros_template)

    def render_html(self, **kwargs):
        print("Rendering question html")
        if self.form is None and self.form_class is not None:
            self.build_form()
        self.traverse_templates()
        print("Question template: {:s}".format(self.template))
        print("Form template: {:s}".format(self.form.template))
        print("Form macros template: {:s}".format(self.form.macros_template))
        template = jinja_env.get_template(self.template)
        html = template.render(params=self.params(), question=self, form=self.form, url_for=url_for, **kwargs)
        return html

    def to_json(self):
        return({
            'marked_correct': list(self.marked_correct),
            'marked_incorrect': list(self.marked_incorrect),
            })

    def score_answer(self):
        return(int(self.check_answer()))

    def record_answer(self, user, score):
        statement = question_scores.insert().values(user_id=user.id, question_id=self.id, answer=json.dumps(self.form.data), score=score)
        db.session.execute(statement)
        db.session.commit()

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
                    print(str(entry))
                    self.missing_entries.append((row,column))

    def render_html(self, **kwargs):
        if self.df is None:
            self.load_csv()
        params = self.params()
        transpose_display = 'transpose_display' in params and params['transpose_display'] in ["true","True",True]
        print(params['transpose_display'])
        return Question.render_html(self, missing_entries=self.missing_entries, transpose_display=transpose_display, **kwargs)
    def build_form(self, formdata=None):
        if self.df is None:
            self.load_csv()
        Question.build_form(self, formdata)
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
        print("checking answers")
        print(self.form.data)
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
    pass
#    def render_html(self, **kwargs):
#        params = self.params()
#        return CompleteTableQuestion.render_html(self, blocks=params['blocks'], **kwargs)


#import pandas as pd
#from io import StringIO
#import re
#s = StringIO("a,b,c\n1,[2],3\n4,[5],6\n")
#df = pd.read_csv(s)
#missing_entries = []
#df = df.transpose()
#for column in df.columns:
#    for i,entry in enumerate(df[column]):
#        if re.match("^\[.+\]$",str(entry)):
#            missing_entries.append((row,column))
#            df[column][i] = self.form.entries.entries[missing_entries.index((row,column))]
#        
#for label, content in df.items():
#    for entry in content:
#        if re.match("^\[.+\]$",str(entry)):
#            missing_entries.append(entry)
#        Question.build_form(self, formdata)
#        return(self.form)

class DrawingQuestion(Question):
    form_class = DrawingForm
    form = None
#    def render_html(self, **kwargs):
#        params = self.params()
#        return Question.render_html(self, background_image_url=params['background_image_url'], **kwargs)
    def build_form(self, formdata=None):
        Question.build_form(self, formdata)
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
            module_class_string = part['class']
            module_name, class_name = module_class_string.rsplit(".", 1)
            module = importlib.import_module('..' + module_name, package=__name__)
            question_class = getattr(module, class_name)
            part['params_json'] = json.dumps(part['params'])
            question = get_or_create(db.session, question_class, params_json=part['params_json'])
            self.parts.append(question)
        for i,part in enumerate(self.parts):
            part.macros_template = part.traverse_macros_templates()
            print("Part macros template: {:s}".format(part.macros_template))

    def scripts(self):
        params = self.params()
        #scripts = {}
        scripts = []
        for i,part in enumerate(params['parts']):
            #scripts.update(part['question'].scripts())
            scripts += part['question'].scripts()
        return(scripts)

    def build_form(self, formdata=None):
        self.build_parts()
        class DynamicMultiPartAnswerForm(MultiPartAnswerForm):
            pass
        self.form_class = DynamicMultiPartAnswerForm
        for i,part in enumerate(self.parts):
            setattr(self.form_class, 'part_{:d}'.format(i), FormField(part.form_class))
            #setattr(F, 'part_{:d}'.format(i), FormField(part['question'].form_class,_name='part_{:d}'.format(i)))
            #setattr(getattr(F, 'part_{:d}'.format(i)),'name','part_{:d}'.format(i))
        #form = F(prefix='test')
        print("build_form formdata checkpoint")
        print(formdata)
        #self.form.process(MultiDict(formdata))
        #self.form = F()
        #self.form = F(MultiDict(formdata))
        #self.form = DynamicMultiPartAnswerForm(data=MultiDict(formdata))
        self.form = self.form_class(formdata=formdata)
        #Question.build_form(self)
        self.form.traverse_templates()
        self.form.traverse_macros_templates()
        self.form.question = self
        #self.form.jinja_env = jinja2.Environment(loader=loader)
        print(self.form.data)
        self.form.validate()
        print(self.form.errors)
#        for i,part in enumerate(params['parts']):
#            #subform = part['question'].form_class(MultiDict(formdata['part_{:d}'.format(i)]))
#            #subform(MultiDict(formdata['part_{:d}'.format(i)]))
#            self.form['part_{:d}'.format(i)].object_data = formdata['part_{:d}'.format(i)]
#            #getattr(self.form, 'part_{:d}'.format(i)).bind(self.form, 'part_{:d}'.format(i))
#            #print(formdata['part_{:d}'.format(i)])
#            #getattr(self.form, 'part_{:d}'.format(i)).process(MultiDict(formdata['part_{:d}'.format(i)]))
#            #subform_field = getattr(F, 'part_{:d}'.format(i)).bind(self.form, 'part_{:d}'.format(i))
#            #subform_field.process_formdata(MultiDict(formdata['part_{:d}'.format(i)]))
#            #print(MultiDict(formdata['part_{:d}'.format(i)]))
#            #print(subform_field.data)
#            #self.form['part_{:d}'.format(i)].process(formdata=MultiDict(formdata['part_{:d}'.format(i)]))
#        #self.form = F(MultiDict(formdata))
#        #self.form.process(MultiDict(formdata))
        print(formdata)
        print('building MultiPartQuestion form')
        print(self.form.data)
        for i,part in enumerate(self.parts):
            part.form = getattr(self.form, 'part_{:d}'.format(i))
            print(part.form)
        return(self.form)

    def render_html(self, **kwargs):
        if self.form is None:
            self.build_form()
        for part in self.parts:
            print(part.__class__.__name__)
        return Question.render_html(self, parts=self.parts, **kwargs)
#        for base_class in inspect.getmro(self.__class__):
#            try:
#                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
#                return template.render(params, form=self.form)
#            except TemplateNotFound:
#                next 
    
    def check_answer(self):
        #params = self.params()
        self.build_parts()
        #return all([part['question'].check_answer(getattr(form,'part_'+str(i))) for i,part in enumerate(params['parts'])])
        print(self.form.data)
        self.marked_correct = set()
        self.marked_incorrect = set()
        for i,part in enumerate(self.parts):
            part.check_answer()
            self.marked_correct = self.marked_correct.union(set(["part_{:d}-{:s}".format(i,field) for field in part.marked_correct]))
            self.marked_incorrect = self.marked_incorrect.union(set(["part_{:d}-{:s}".format(i,field) for field in part.marked_incorrect]))
        return all([part.check_answer() for i,part in enumerate(self.parts)])


class QuestionOnePlusOne(Question):
    form_class = AnswerForm
    form = None

    def build_form(self, formdata=None):
        self.form = self.form_class(MultiDict(formdata))
        print('building QuestionOnePlusOne form')
        print(self.form.data)
        return(self.form)

    def check_answer(self):
        print(self.form.answer.data)
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
            print(self.form.data)
            expr = parse_expr(params['statement'],transformations=transformations).subs(x,parse_expr(self.form.answer.data))
            print(expr)
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
        self.marked_correct = set('answer')
        return(True)

QuestionClasses = {
    'Question.CompleteTableQuestion': CompleteTableQuestion,
    'Question.CompleteTableDraggableQuestion': CompleteTableDraggableQuestion,
    'Question.OpenEndedQuestion': OpenEndedQuestion,
    'Question.SolutionQuestion': SolutionQuestion,
    'Question.NonSolutionQuestion': NonSolutionQuestion,
    'Question.MultiPartQuestion': MultiPartQuestion,
    'Question.QuestionOnePlusOne': QuestionOnePlusOne,
    'Question.DrawingQuestion': DrawingQuestion,
    'Question.AsyGraphicsQuestion': AsyGraphicsQuestion,
    'Question.DotGraphicsQuestion': DotGraphicsQuestion,
    'Question.AsyGraphicsDrawingQuestion': AsyGraphicsDrawingQuestion,
}

question_scores = db.Table('question_scores',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('score', db.Float),
    db.Column('answer', db.Text),
    db.Column('datetime', db.DateTime, nullable=False,
        default=datetime.utcnow)
)
