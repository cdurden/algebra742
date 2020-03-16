from flask import current_app as app
from datetime import datetime
from .. import db
import jinja2
import json
import os
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, TextAreaField, FieldList
from flask import url_for
from jinja2.exceptions import TemplateNotFound
from .. import SinglyLinkedList, get_or_create
from werkzeug.datastructures import MultiDict, ImmutableMultiDict
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates"))
jinja_env = jinja2.Environment(loader=loader)
from networkx.drawing.nx_pydot import read_dot
from ..util import params_hash_lookup, process_quotes_for_json

class Form(FlaskForm):
    jinja_env = None
    def render_html(self, **kwargs):
        import inspect
        for base_class in inspect.getmro(self.__class__):
            try:
                template = self.jinja_env.get_template("{:s}.html".format(base_class.__name__))
                html = template.render(form=self, url_for=url_for, **kwargs)
                return(html)
            except TemplateNotFound:
                next 

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


class MultiPartAnswerForm(FlaskForm):
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

    def render_html(self, **kwargs):
        import inspect
        print("Rendering question html")
        if self.form is None and self.form_class is not None:
            self.build_form()
        for base_class in inspect.getmro(self.__class__):
            print("Trying to render question using {:s} template".format(base_class.__name__))
            try:
                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
                html = template.render(self.params(), form=self.form, id=self.id, url_for=url_for, **kwargs)
                print(html)
                return html
            except TemplateNotFound:
                next 

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
            for i,entry in enumerate(self.df[column]):
                if re.match("^\[.+\]$",str(entry)):
                    print(str(entry))
                    self.missing_entries.append((column,i))

    def render_html(self, **kwargs):
        if self.df is None:
            self.load_csv()
        return Question.render_html(self, df=self.df, missing_entries=self.missing_entries, **kwargs)
    def build_form(self, formdata=None):
        if self.df is None:
            self.load_csv()
        Question.build_form(self, formdata)
        for (column,i) in self.missing_entries:
            if len(self.form.entries) < len(self.missing_entries):
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
        for (column,i) in self.missing_entries:
            answer = parse_expr(str(entry).strip("[]"),transformations=transformations)
            answer_input = parse_expr(self.form.entries.entries[self.missing_entries.index((column,i))].data, transformations=transformations)
            correct = bool(answer-answer_input==0)
            if correct:
                self.marked_correct.add(self.form.entries.entries[self.missing_entries.index((column,i))].name)
            else:
                self.marked_incorrect.add(self.form.entries.entries[self.missing_entries.index((column,i))].name)
        return len(self.marked_correct)==len(self.missing_entries)


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
#            missing_entries.append((column,i))
#            df[column][i] = self.form.entries.entries[missing_entries.index((column,i))]
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
    def render_html(self, **kwargs):
        params = self.params()
        return Question.render_html(self, background_image_url=params['background_image_url'], **kwargs)
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

    def scripts(self):
        params = self.params()
        #scripts = {}
        scripts = []
        class F(MultiPartAnswerForm):
            pass
        for i,part in enumerate(params['parts']):
            #scripts.update(part['question'].scripts())
            scripts += part['question'].scripts()
        return(scripts)


    def build_form(self, formdata=None):
        params = self.params()
        class F(MultiPartAnswerForm):
            pass
        for i,part in enumerate(params['parts']):
            setattr(F, 'part_{:d}'.format(i), FormField(part['question'].form_class))
            #setattr(F, 'part_{:d}'.format(i), FormField(part['question'].form_class,_name='part_{:d}'.format(i)))
            #setattr(getattr(F, 'part_{:d}'.format(i)),'name','part_{:d}'.format(i))
        #form = F(prefix='test')
        print("build_form formdata checkpoint")
        print(formdata)
        #self.form.process(MultiDict(formdata))
        #self.form = F()
        #self.form = F(MultiDict(formdata))
        self.form = F(data=MultiDict(formdata))
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
        return(self.form)

    def params(self):
        #params = json.loads(process_quotes_for_json(self.params_json))
        params = json.loads(self.params_json)
        import importlib
        for i,part in enumerate(params['parts']):
            module_class_string = part['class']
            module_name, class_name = module_class_string.rsplit(".", 1)
            module = importlib.import_module('..' + module_name, package=__name__)
            class_ = getattr(module, class_name)
            part['params_json'] = json.dumps(part['params'])
            question = get_or_create(db.session, class_, params_json=part['params_json'])
            part['question'] = question
        return(params)

    def render_html(self):
        import inspect
        params = self.params()
        if self.form is None:
            self.build_form()
        for i,part in enumerate(params['parts']):
            part['question'].form = getattr(self.form, 'part_{:d}'.format(i))
        for base_class in inspect.getmro(self.__class__):
            try:
                template = jinja_env.get_template("{:s}.html".format(base_class.__name__))
                return template.render(params, form=self.form)
            except TemplateNotFound:
                next 
    
    def check_answer(self):
        params = self.params()
        #return all([part['question'].check_answer(getattr(form,'part_'+str(i))) for i,part in enumerate(params['parts'])])
        print(self.form.data)
        self.marked_correct = set()
        self.marked_incorrect = set()
        for i,part in enumerate(params['parts']):
            part['question'].build_form(getattr(self.form,'part_{:d}'.format(i)).data)
            part['question'].check_answer()
            self.marked_correct = self.marked_correct.union(set(["part_{:d}-{:s}".format(i,field) for field in part['question'].marked_correct]))
            self.marked_incorrect = self.marked_incorrect.union(set(["part_{:d}-{:s}".format(i,field) for field in part['question'].marked_incorrect]))
        return all([part['question'].check_answer() for i,part in enumerate(params['parts'])])


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
            expr = parse_expr(params['statement']).subs(x,parse_expr(self.form.answer.data))
            correct = bool(expr)
        except:
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
