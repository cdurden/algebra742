import os
import sys
import json
import re
from flask import Flask, url_for, redirect
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select, and_, desc
from flask_wtf import Form
from wtforms import TextField, IntegerField, BooleanField, FieldList, StringField, RadioField, IntegerField, FormField, TextAreaField, SelectField, SelectMultipleField, widgets
from wtforms.validators import NumberRange
import random
import markdown
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from markdown_include.include import MarkdownInclude

from pylti.flask import lti
from functools import wraps
from flask import request, render_template
from flask import Response, make_response, after_this_request
from functools import wraps
from Questions import *
from werkzeug.datastructures import MultiDict

import io
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse
VERSION = '0.0.1'
app = Flask(__name__)
app.config.from_object('config')
#logging.basicConfig(level=logging.INFO)
#root = logging.getLogger()
#logger = root
from wtforms_components import TimeField, read_only

handler = RotatingFileHandler(os.path.join(os.path.dirname(__file__),'info.log'), maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(Formatter('[%(levelname)s][%(asctime)s] %(message)s'))
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

#logging.basicConfig(stream=sys.stderr)
#logging.basicConfig(filename=os.path.join(os.path.dirname(__file__),'info.log'), level=logging.DEBUG)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

from datetime import datetime

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    params_json = db.Column(db.Text)
    assignment = db.Column(db.String(255))
    number = db.Column(db.Integer)
    variant_index = db.Column(db.Integer)

question_scores = db.Table('question_scores',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('score', db.Float),
    db.Column('answer', db.Text),
    db.Column('datetime', db.DateTime, nullable=False,
        default=datetime.utcnow)
)
# FIXME: Unique constraint?

#def AnswerChecker():

#class Assignment(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    description = db.Column(db.String(80), nullable=False)
#    body = db.Column(db.Text, nullable=False)
#    pub_date = db.Column(db.DateTime, nullable=False,
#        default=datetime.utcnow)
#
#    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
#        nullable=False)
#    category = db.relationship('Category',
#        backref=db.backref('posts', lazy=True))
#
#    def __repr__(self):
#        return '<Post %r>' % self.title
#


def returns_html(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        r = make_response(r)
        r.headers['Content-type'] = 'text/html; charset=utf-8'
        return r
    return decorated_function

def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

class SubmitForm(Form):

    """ Add data from Form

    :param Form:
    """
    feedback = TextAreaField('feedback')

class GenericForm(Form):
    """ Add data from Form

    :param Form:
    """
    #answer = IntegerField('answer')
    answer = StringField('answer')
    explanation = TextAreaField('explanation')

class TarsiaForm(Form):

    """ Add data from Form

    :param Form:
    """
    #answers = FieldList(SelectField('answers'))
    answers = StringField('answers')

class SortableForm(Form):

    """ Add data from Form

    :param Form:
    """
    #answers = FieldList(SelectField('answers'))
    answers = StringField('answers')


class FindValuesForm(Form):

    """ Add data from Form

    :param Form:
    """
    """ Add data from Form

    :param Form:
    """
    answers = FieldList(FormField(GenericForm))


class OpenResponseForm(Form):

    """ Add data from Form

    :param Form:
    """
    answer = TextAreaField('answer')

class MCForm(Form):
    """ Add data from Form

    :param Form:
    """
    options = RadioField('options')
    other = TextField('other')

class SumTermsProductFactorsForm(Form):
    """ Add data from Form

    :param Form:
    """
    options = RadioField('options')
    terms = TextField('terms')
    factors = TextField('factors')

def op(expr, operation, operand):
    if operation == '+':
        return(expr+operand)
    if operation == '-':
        return(expr-operand)
    if operation == '*':
        return(expr*operand)
    if operation == '/':
        return(expr/operand)

class SolveEquationStepForm(Form):
    """ Add data from Form

    :param Form:
    """
    operation = RadioField('operation', choices=[('+','Add'),('-','Subtract'),('*','Multiply by'),('/','Divide by'),('None','Simplify by distributing and combining like terms')])
    #operation = RadioField('operation', choices=[('+','$+$'),('-','$-$'),('*',r'$\times$'),('/',r'$\div$')])
    operand = StringField('operand')
    new_equation = StringField('new_equation')

class MatchingForm(Form):
    """ Add data from Form

    :param Form:
    """
    answers = FieldList(SelectField('answers'))

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SelectMultipleForm(Form):
    """ Add data from Form

    :param Form:
    """
    answers = MultiCheckboxField('answers')

class SolveEquationGuidedForm(Form):
    """ Add data from Form

    :param Form:
    """
    steps = FieldList(FormField(SolveEquationStepForm))

class CoordinatePairForm(Form):
    """ Add data from Form

    :param Form:
    """
    #object_ = SelectField('object', choices=[])
    #operation = RadioField('operation', choices=[('+','$+$'),('-','$-$'),('*',r'$\times$'),('/',r'$\div$')])
    x = StringField('x')
    y = StringField('y')

class SetOfCoordinatePairsForm(Form):
    """ Add data from Form

    :param Form:
    """
    #operation = RadioField('operation', choices=[('+','$+$'),('-','$-$'),('*',r'$\times$'),('/',r'$\div$')])
    set_of_coordinate_pairs = StringField('set_of_coordinate_pairs')

class SetOfCoordinatePairsAndPredictionForm(Form):
    """ Add data from Form

    :param Form:
    """
    set_of_coordinate_pairs = StringField('set_of_coordinate_pairs')
    answer = StringField('answer')
    explanation = TextAreaField('explanation')

class CoordinatePairsForm(Form):
    """ Add data from Form

    :param Form:
    """
    coordinate_pair_forms = FieldList(FormField(CoordinatePairForm))
    explanation = TextAreaField('explanation')

class InputOutputTableAndSetOfCoordinatePairsForm(Form):
    """ Add data from Form

    :param Form:
    """
    set_of_coordinate_pairs = StringField('set_of_coordinate_pairs')
    coordinate_pair_forms = FieldList(FormField(CoordinatePairForm))
    explanation = TextAreaField('explanation')

class NumericalForm(Form):
    """ Add data from Form

    :param Form:
    """
    #answer = IntegerField('answer')
    answer = StringField('answer')

class ExpressionForm(Form):
    """ Add data from Form

    :param Form:
    """
    #answer = IntegerField('answer')
    answer = StringField('answer')
    
class EquationForm(Form):
    """ Add data from Form

    :param Form:
    """
    variables = FieldList(StringField('variable'))
    quantities = FieldList(StringField('quantities'))
    lhs = TextField('lhs')
    rhs = TextField('rhs')
    
class SetUpAndSolveEquationGuidedForm(Form):
    """ Add data from Form

    :param Form:
    """
    equation_form = FormField(EquationForm)
    steps = FieldList(FormField(SolveEquationStepForm))

class UserInfoForm(Form):
    """ Add data from Form

    :param Form:
    """
    username = StringField('username')
    firstname = StringField('firstname')
    lastname = StringField('lastname')


def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')

def get_or_create(session, model, defaults=None, **kwargs):
    from sqlalchemy.sql.expression import ClauseElement
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance

def GetNextExamQuestionVariant(db, user, assignment, q, i):
        for j,QuestionData in enumerate(QuestionSets[assignment]['Questions']):
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==q, question_scores.c.score==1))
            correct = db.session.execute(statement).all()
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.number==j+1, question_scores.c.score==0))
            incorrect = db.session.execute(statement).all()
            if len(incorrect) < QuestionSets[assignment]['Questions'][j]['IncorrectLimit']:
                if len(correct)/(len(correct)+len(incorrect))> QuestionSets[assignment]['Questions'][j]['AdvanceLevel']:
                    statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.number==j+2, question_scores.c.score==0))
                    next_level_incorrect = db.session.execute(statement).all()
                    if length(next_level_incorrect) < QuestionSets[assignment]['Questions'][j+1]['IncorrectLimit']:
                        q0 = j+2
                    else:
                        q0 = j+1
                else:
                    q0 = j+1
            else:
                q0 = None

def ReversedGetNextQuestionVariant(db, user, assignment, q, i):
    done = False
    try:
        q = int(q)
    except:
        for j,QuestionData in reversed(list(enumerate(QuestionSets[assignment]['Questions']))):
            for k in reversed(range(len(QuestionData['ParameterSetVariants']))):
                statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==j+1, Question.__table__.c.variant_index==k))
                results = db.session.execute(statement).first()
                if results:
                    if k!=len(QuestionData['ParameterSetVariants'])-1:
                        q = j+1
                        i = k+1
                    else:
                        q = j+2
                        i = 0 
                    done = True
                    break
            if done:
                break
        if not done:
            q = 1
            i = 0
    try:
        QuestionData = QuestionSets[assignment]['Questions'][q-1]
    except:
        return (None,None)
    try:
        i = int(i)
    except:
        for k in reversed(range(len(QuestionData['ParameterSetVariants']))):
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==q, Question.__table__.c.variant_index==k))
            results = db.session.execute(statement).first()
            if results:
                if k!=len(QuestionData['ParameterSetVariants'])-1:
                    i = k+1
                else:
                    i = k
                done = True
                break
        if not done:
            i = 0
    return((q,i))

def GetNextQuestionVariant(db, user, assignment, q, i):
    done = False
    try:
        q = int(q)
    except:
        for j,QuestionData in enumerate(QuestionSets[assignment]['Questions']):
            for k in range(len(QuestionData['ParameterSetVariants'])):
                statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==j+1, Question.__table__.c.variant_index==k))
                results = db.session.execute(statement).first()
                if not results:
                    q = j+1
                    i = k
                    done = True
                    break
            if done:
                break
    try:
        QuestionData = QuestionSets[assignment]['Questions'][q-1]
    except:
        return (None,None)
    try:
        i = int(i)
    except:
        for k in range(len(QuestionData['ParameterSetVariants'])):
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==q, Question.__table__.c.variant_index==k))
            results = db.session.execute(statement).first()
            if not results:
                i = k
                break
    return((q,i))

def GetNextNoncorrectlyAnsweredQuestionVariant(db, user, assignment, q, i):
    done = False
    try:
        q = int(q)
    except:
        for j,QuestionData in enumerate(QuestionSets[assignment]['Questions']):
            for k in range(len(QuestionData['ParameterSetVariants'])):
                statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==j+1, Question.__table__.c.variant_index==k, question_scores.c.score==1))
                results = db.session.execute(statement).first()
                if not results:
                    q = j+1
                    i = k
                    done = True
                    break
            if done:
                break
    try:
        QuestionData = QuestionSets[assignment]['Questions'][q-1]
    except:
        return (None,None)
    try:
        i = int(i)
    except:
        for k in range(len(QuestionData['ParameterSetVariants'])):
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment, Question.__table__.c.number==q, Question.__table__.c.variant_index==k, question_scores.c.score==1))
            results = db.session.execute(statement).first()
            if not results:
                i = k
                break
    return((q,i))

def random_points(N=5,seed=0,function=True):
    random.seed(int(seed))
    #x = [random.randint(-10,10) for i in range(N)]
    x = []
    if function:
        for i in range(N):
            x0 = random.randint(-10,10)
            while x0 in x:
                x0 = random.randint(-10,10)
            x.append(x0)
    else:
        x = [random.randint(-10,10) for i in range(N)]
        x[N] = x[1]
    
    y = [random.randint(-10,10) for i in range(N)]
    return(x,y)

def generate_mapping_diagram(x,y):
    """ renders the plot on the fly.
    """
    fig = Figure()
    app.logger.error(x)
    app.logger.error(y)
    inputs = list(set(x))
    outputs = list(set(y))
    inputs.sort(key=lambda elmt: float(elmt))
    outputs.sort(key=lambda elmt: float(elmt))
    n = max(len(inputs),len(outputs))
    axis = fig.add_subplot(1, 1, 1)
    ells = [Ellipse((0, -float(n-1)/2), n, 2, 90, edgecolor='black',facecolor='white'), Ellipse((3, -float(n-1)/2), n, 2, 90, edgecolor='black',facecolor='white')]
    for e in ells:
        axis.add_artist(e)
    axis.axis('off')
    axis.scatter([-1,4,4],[1,-len(inputs),-len(outputs)],marker=",",alpha=0)
    for i in range(len(inputs)):
        #axis.annotate(str(inputs[i]),(-i,0))
        axis.text(0,-i,str(inputs[i]),fontsize=18,color='black', horizontalalignment="right", verticalalignment="center")
    for j in range(len(outputs)):
        #axis.annotate(str(outputs[j]),(-j,3))
        axis.text(3,-j,str(outputs[j]),fontsize=18,color='black', horizontalalignment="left", verticalalignment="center")
    for x_,y_ in zip(x,y):
        i = inputs.index(x_)
        j = outputs.index(y_)
        axis.arrow(0.2,-i, 2.7, -(j-i), head_width=0.1, head_length=0.1, fc='k', ec='k')
    return(fig)

def generate_scatterplot(x,y):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.scatter(x, y)
    major_ticks = np.arange(-10, 10, 2)
    minor_ticks = np.arange(-10, 10, 1)
    minxy = min(x+y)
    maxxy = max(x+y)
    major_ticks = np.arange(minxy, maxxy, 2)
    minor_ticks = np.arange(minxy, maxxy, 1)
    axis.set_xticks(major_ticks)
    axis.set_xticks(minor_ticks, minor=True)
    axis.set_yticks(major_ticks)
    axis.set_yticks(minor_ticks, minor=True)
    axis.grid(which='minor', alpha=0.2)
    axis.grid(which='major', alpha=0.5)
    axis.set_aspect('equal')
    # set the x-spine (see below for more info on `set_position`)
    axis.spines['left'].set_position('zero')

    # turn off the right spine/ticks
    axis.spines['right'].set_color('none')
    axis.yaxis.tick_left()

    # set the y-spine
    axis.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    axis.spines['top'].set_color('none')
    axis.xaxis.tick_bottom()
    return(fig)

@app.route("/random_mapping_diagram-<int:N>-<int:seed>.svg")
def random_mapping_diagram(N=5, seed=0):
    x,y = random_points(N=N,seed=seed)
    fig = generate_mapping_diagram(x,y)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")

@app.route("/random_scatterplot-<int:N>-<int:seed>.svg")
def random_scatterplot(N=5, seed=0):
    x,y = random_points(N=N,seed=seed)
    fig = generate_scatterplot(x,y)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")

@app.route("/mapping_diagram")
def mapping_diagram():
    x = [int(elmt) for elmt in request.args.getlist('x')]
    y = [int(elmt) for elmt in request.args.getlist('y')]
    fig = generate_mapping_diagram(x,y)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")

@app.route("/scatterplot")
def scatterplot():
    #x = request.args.getlist('x')
    #y = request.args.getlist('y')
    x = [float(elmt) for elmt in request.args.getlist('x')]
    y = [float(elmt) for elmt in request.args.getlist('y')]
    fig = generate_scatterplot(x,y)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


@app.route('/Assignment/<assignment>/<q>/<i>', methods=['GET', 'POST'])
@app.route('/Assignment/<assignment>/<q>', methods=['GET', 'POST'])
@app.route('/Assignment/<assignment>', methods=['GET', 'POST'])
@templated('MarkdownQuestionGeneral.html')
@lti(request='session', error=error, app=app)
def Assignment(lti=lti, assignment=None,q=None,i=None):
#def Assignment(assignment=None,q=None,i=None):
    if q == 'submit':
        return render_template('thankyou.html')
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    app.logger.error(i)
    q,i = ReversedGetNextQuestionVariant(db, user, assignment, q, i)
    app.logger.error(i)
    #if q is None:
    #    q = len(QuestionSets[assignment]['Questions'])
    #    i = len(QuestionSets[assignment]['Questions'][q-1]['ParameterSetVariants'])-1
    #user = User(username="test user", lti_user_id="asdf")
    if q is None:
        QuestionData = { 'Type': 'SubmitAssignment',
                         'Template': 'SubmitAssignment.html',
                         'ParameterSetVariants': [{}]}
        Parameters = {}
        NextQuestion = None
        question_number = None 
    else:
        QuestionData = QuestionSets[assignment]['Questions'][q-1]
        app.logger.error(QuestionData['ParameterSetVariants'])
        Parameters = QuestionData['ParameterSetVariants'][i]
        if len(QuestionSets[assignment]['Questions']) > q or len(QuestionData['ParameterSetVariants']) > i+1:
            if len(QuestionData['ParameterSetVariants']) > i+1:
                NextQuestion = {'q': q, 'i': i+1}
            else:
                NextQuestion = {'q': q+1, 'i': 0}
        else:
            NextQuestion = None
    question_indices = []
    if not user:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)
    @after_this_request
    def add_header(response):
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    from sympy import sympify, simplify, symbols, latex
    from sympy.parsing.sympy_parser import parse_expr
    from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
    transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
    a,b = symbols("a b")
    correct = False
    answer = None
    message = ''
    formdata = {}

    if request.method != 'POST':
        try:
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment,Question.__table__.c.number==q, Question.__table__.c.variant_index==i)).order_by(desc('datetime'))
            results = db.session.execute(statement).first()
            formdata = json.loads(results.answer)
            app.logger.error(results.answer)
        except:
            formdata = {}
            pass
    app.logger.error(formdata)
    if user.id == 86:
        formdata = {}
    if QuestionData['Type'] == 'SubmitAssignment':
        form = SubmitForm()
    if QuestionData['Type'] == 'SortCards':
        try:
            form = SortableForm(data=formdata)
        except:
            form = SortableForm()
        app.logger.error(form.answers.data)
        try:
            shuffle = Parameters['shuffle']
            input_order = [shuffle[int(re.split("=",x)[1])] for x in re.split("&",form.answers.data)]
            Parameters['input_order'] = json.dumps(input_order)
            correct = input_order in Parameters['solutions']
            app.logger.error(input_order)
            app.logger.error(correct)
        except:
            correct = False
            #Parameters['shuffle0'] = Parameters['shuffle']
            #Parameters['cards'] = [Parameters['cards'][i] for i in Parameters['shuffle']]
        answer = json.dumps(form.data)
    if QuestionData['Type'] == 'Tarsia':
        try:
            form = TarsiaForm(data=formdata)
        except:
            form = TarsiaForm()
        app.logger.error(form.answers.data)
        try:
            input_order = [int(re.split("=",x)[1]) for x in re.split("&",form.answers.data)]
            correct = input_order==Parameters['shuffle']
            #cards = Parameters['cards'].copy()
            #cards = [cards[i] for i in Parameters['shuffle']]
            app.logger.error(input_order)
            #Parameters['cards'] = [Parameters['cards'][input_order[i]] for i in Parameters['shuffle']]
            app.logger.error(correct)
        except:
            correct = False
            Parameters['cards'] = [Parameters['cards'][i] for i in Parameters['shuffle']]
        answer = json.dumps(form.data)
    if QuestionData['Type'] == 'Simplify':
        #app.logger.error(form.data)
        #if form.data == None:
        #form = ExpressionForm(MultiDict(formdata))
        form = ExpressionForm(data=formdata)
        try:
            answer = sympify(parse_expr(form.answer.data, transformations=transformations, evaluate=False),evaluate=False)
            #expression = parse_expr(QuestionData['ParameterSetVariants'][i]['expression'], transformations=transformations)
        #except:
        #    answer = sympify(0)
        #try:
            expression = sympify(parse_expr(QuestionData['ParameterSetVariants'][i]['expression'], transformations=transformations, evaluate=False), evaluate=False)
            terms = expression.args
            correct = simplify(answer-expression) == 0 
            simplified = len(answer.args)<=len(simplify(expression).args)
            if correct and simplified:
                message = "Your answer {:s} is correct!".format(answer)
            else:
                if not correct:
                    message = "Your answer {:s} is not correct. Try again!".format(answer)
                if not simplified:
                    message = "Your answer {:s} is not simplified. Try again!".format(answer)
        except:
            pass
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['SelectMultiple']:
        try:
            form = SelectMultipleForm(data=formdata)
        except:
            form = SelectMultipleForm()
        choices = []
        for choice,value in Parameters['choices']:
            choices.append((choice,value))
        form.answers.choices = choices
        if Parameters['CorrectAnswer'] is None:
            correct = False
        else:
            correct = Parameters['CorrectAnswer'] == set(form.answers.data)
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['Matching']:
        try:
            form = MatchingForm(data=formdata)
        except:
            form = MatchingForm()
        choices = []
        for choice,value in Parameters['answers'].items():
            choices.append((choice,'{:s}. {:s}'.format(choice,value)))
        n = len(Parameters['prompts'])
        for it in range(n):
            if len(form.answers.entries) < it+1:
                form.answers.append_entry()
            form.answers[it].choices = choices
        correct = 0
        for it,answer in enumerate(form.answers.entries):
            if form.answers[it].data == Parameters['CorrectAnswers'][it]:
                correct += 1
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['GenericEquality']:
        try:
            form = GenericForm(data=formdata)
        except:
            form = GenericForm()
        try:
            input_expr = parse_expr(form.answer.data)
            correct = input_expr == parse_expr(Parameters['CorrectAnswer'])
            if not correct:
                message = "Your answer {:s} is not correct.".format(form.answer.data)
        except AttributeError:
            correct = False
        except ValueError:
            message = "Your answer {:s} is not correct.".format(form.answer.data)
            correct = False
        except SyntaxError:
            message = "Your answer {:s} is not correct.".format(form.answer.data)
            correct = False
        except TypeError:
            message = "Your answer {:s} is not correct.".format(form.answer.data)
            correct = False
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['SetOfCoordinatePairs']:
        form = SetOfCoordinatePairsForm(data=formdata)
        #form = CoordinatePairsForm()
        try:
            input_coordinate_pairs = re.split("\)\s*,\s*\(",form.set_of_coordinate_pairs.data)
            input_set_of_coordinate_pairs = set()
            for input_coordinate_pair_string in input_coordinate_pairs:
                input_coordinate_pair = tuple(float(x.strip("{()} ")) for x in input_coordinate_pair_string.split(","))
                input_set_of_coordinate_pairs.add(input_coordinate_pair)
            if len(input_set_of_coordinate_pairs) < int(json.loads(Parameters['N'])):
                correct = False
            app.logger.error(input_set_of_coordinate_pairs)
            app.logger.error(Parameters['set_of_coordinate_pairs'])
            correct = input_set_of_coordinate_pairs == Parameters['set_of_coordinate_pairs']
            if not correct:
                message = "Coordinate pairs {:s} are not correct.".format(Parameters['set_of_coordinate_pairs'] - input_set_of_coordinate_pairs)
        except ValueError:
            message = "Coordinate pairs could not be read. Make sure that you entered them correctly."
            correct = False
        except TypeError:
            message = "Coordinate pairs could not be read. Make sure that you entered them correctly."
            correct = False
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['MCMappingDiagram', 'MCGraph']:
        form = MCForm(data=formdata)
        #form = CoordinatePairsForm()
        app.logger.error(Parameters)
        input_coordinates = set()
        choices = []
        #seed = Parameters['seed']
        for it,k in enumerate(['a','b','c','d']):
            if QuestionData['Type'] == 'MCMappingDiagram':
                if 'x' in Parameters['Choices'][it][1] and 'y' in Parameters['Choices'][it][1]:
                    choices.append((k,"<img src={:s} />".format(url_for('mapping_diagram', x=Parameters['Choices'][it][1]['x'],y=Parameters['Choices'][it][1]['y']))))
                else:
                    choices.append((k,"<img src={:s} />".format(url_for('random_mapping_diagram', seed=Parameters['Choices'][it][1]['seed'],N=Parameters['Choices'][it][1]['n']))))
            if QuestionData['Type'] == 'MCGraph':
                if 'x' in Parameters['Choices'][it][1] and 'y' in Parameters['Choices'][it][1]:
                    choices.append((k,"<img src={:s} />".format(url_for('scatterplot', x=Parameters['Choices'][it][1]['x'],y=Parameters['Choices'][it][1]['y']))))
                else:
                    choices.append((k,"<img src={:s} />".format(url_for('random_scatterplot', seed=Parameters['Choices'][it][1]['seed'],N=Parameters['Choices'][it][1]['n']))))
        try:
            choice = form.options.data
            CorrectAnswer = QuestionData['ParameterSetVariants'][i]['CorrectAnswer']
            app.logger.error(choice)
            app.logger.error(CorrectAnswer)
            if choice == CorrectAnswer:
                correct = True
            else:
                correct = False
        except:
            pass
        form.options.choices = choices
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['FindValues']:
        form = FindValuesForm(data=formdata)
        #form = CoordinatePairsForm()
        n = len(Parameters['variables'])
        variables = Parameters['variables']
        if request.method == 'POST':
            correct = True
        for it,answer_form in enumerate(form.answers.entries):
            try:
                if simplify(parse_expr(answer_form.answer.data)-parse_expr(variables[it][1])) != 0:
                    correct = False
                    break
            except:
                message = "Coordinate pairs could not be read.".format(it+1)
                correct = False
                break
        for it in range(n):
            if len(form.answers.entries) < it+1:
                form.answers.append_entry()
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['InputOutputTableEquation']:
        form = CoordinatePairsForm(data=formdata)
        #form = CoordinatePairsForm()
        variables = Parameters['variables']
        if 'n' in Parameters:
            n = Parameters['n']
        else:
            n = len(Parameters[variables[0]])
        input_coordinates = set()
        lhs,rhs = Parameters['equation'].split("=")
        if request.method == 'POST':
            correct = True
        for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
            if variables[0] in Parameters and len(Parameters[variables[0]])>it and Parameters[variables[0]][it] is not None:
                read_only(form.coordinate_pair_forms.entries[it].x)
            if variables[0] in Parameters and len(Parameters[variables[1]])>it and Parameters[variables[1]][it] is not None:
                read_only(form.coordinate_pair_forms.entries[it].y)
        for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
            try:
                variables = Parameters['variables']
                lhs0 = lhs.replace(variables[0], "({:s})".format(str(coordinate_pair_form.x.data)))
                rhs0 = rhs.replace(variables[0], "({:s})".format(str(coordinate_pair_form.x.data)))
                lhs0 = lhs0.replace(variables[1], "({:s})".format(str(coordinate_pair_form.y.data)))
                rhs0 = rhs0.replace(variables[1], "({:s})".format(str(coordinate_pair_form.y.data)))
                app.logger.error(lhs0)
                app.logger.error(rhs0)

                if simplify(parse_expr(lhs0, transformations=transformations)-parse_expr(rhs0, transformations=transformations))!=0:
                    correct = False
            except:
                message = "Coordinate pairs could not be read.".format(it+1)
                correct = False
                break
        for it in range(n):
            if len(form.coordinate_pair_forms.entries) < it+1:
                try:
                    form.coordinate_pair_forms.append_entry({'x': Parameters[variables[0]][it], 'y': Parameters[variables[1]][it]})
                except:
                    form.coordinate_pair_forms.append_entry()
                if variables[0] in Parameters and len(Parameters[variables[0]])>it and Parameters[variables[0]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].x)
                if variables[0] in Parameters and len(Parameters[variables[1]])>it and Parameters[variables[1]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].y)
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['InputOutputTableAndSetOfCoordinatePairsEquation']:
        form = InputOutputTableAndSetOfCoordinatePairsForm(data=formdata)
        #form = CoordinatePairsForm()
        variables = Parameters['variables']
        if 'n' in Parameters:
            n = Parameters['n']
        else:
            n = len(Parameters[variables[0]])
        input_coordinates = set()
        lhs,rhs = Parameters['equation'].split("=")
        if request.method == 'POST':
            correct = True
            try:
                input_coordinate_pairs = re.split("\)\s*,\s*\(",form.set_of_coordinate_pairs.data)
                input_set_of_coordinate_pairs = set()
                for input_coordinate_pair_string in input_coordinate_pairs:
                    input_coordinate_pair = tuple(float(x.strip("{()} ")) for x in input_coordinate_pair_string.split(","))
                    input_set_of_coordinate_pairs.add(input_coordinate_pair)
                    x = input_coordinate_pair[0]
                    y = input_coordinate_pair[1]
                    lhs0 = lhs.replace(variables[0], "({:s})".format(str(x)))
                    rhs0 = rhs.replace(variables[0], "({:s})".format(str(x)))
                    lhs0 = lhs0.replace(variables[1], "({:s})".format(str(y)))
                    rhs0 = rhs0.replace(variables[1], "({:s})".format(str(y)))
                    app.logger.error(lhs0)
                    app.logger.error(rhs0)
    
                    if simplify(parse_expr(lhs0, transformations=transformations)-parse_expr(rhs0, transformations=transformations))!=0:
                        correct = False
                        message = "The points on your graph are not solutions to the equation."
            except:
                message = "The points on your graph could not be read."
                correct = False
            for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
                if variables[0] in Parameters and len(Parameters[variables[0]])>it and Parameters[variables[0]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].x)
                if variables[0] in Parameters and len(Parameters[variables[1]])>it and Parameters[variables[1]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].y)
            try:
                if len(input_set_of_coordinate_pairs) < int(json.loads(Parameters['N'])):
                    correct = False
                for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
                    lhs0 = lhs.replace(variables[0], "({:s})".format(str(coordinate_pair_form.x.data)))
                    rhs0 = rhs.replace(variables[0], "({:s})".format(str(coordinate_pair_form.x.data)))
                    lhs0 = lhs0.replace(variables[1], "({:s})".format(str(coordinate_pair_form.y.data)))
                    rhs0 = rhs0.replace(variables[1], "({:s})".format(str(coordinate_pair_form.y.data)))
                    app.logger.error(lhs0)
                    app.logger.error(rhs0)
    
                    if simplify(parse_expr(lhs0, transformations=transformations)-parse_expr(rhs0, transformations=transformations))!=0:
                        correct = False
            except:
                message = "Coordinate pairs could not be read."
                correct = False
        for it in range(n):
            if len(form.coordinate_pair_forms.entries) < it+1:
                try:
                    form.coordinate_pair_forms.append_entry({'x': Parameters[variables[0]][it], 'y': Parameters[variables[1]][it]})
                except:
                    form.coordinate_pair_forms.append_entry()
                if variables[0] in Parameters and len(Parameters[variables[0]])>it and Parameters[variables[0]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].x)
                if variables[0] in Parameters and len(Parameters[variables[1]])>it and Parameters[variables[1]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].y)
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['SetOfCoordinatePairsEquation', 'SetOfCoordinatePairsEquationAndPrediction']:
        try:
            form = SetOfCoordinatePairsAndPredictionForm(data=formdata)
        except:
            form = SetOfCoordinatePairsAndPredictionForm()
        #form = CoordinatePairsForm()
        input_coordinates = set()
        lhs,rhs = Parameters['equation'].split("=")
        if request.method == 'POST':
            correct = True
        try:
            input_coordinate_pairs = re.split("\)\s*,\s*\(",form.set_of_coordinate_pairs.data)
            input_set_of_coordinate_pairs = set()
            for input_coordinate_pair_string in input_coordinate_pairs:
                input_coordinate_pair = tuple(float(x.strip("{()} ")) for x in input_coordinate_pair_string.split(","))
                input_set_of_coordinate_pairs.add(input_coordinate_pair)
                x = input_coordinate_pair[0]
                y = input_coordinate_pair[1]
                variables = Parameters['variables']
                lhs0 = lhs.replace(variables[0], "({:s})".format(str(x)))
                rhs0 = rhs.replace(variables[0], "({:s})".format(str(x)))
                lhs0 = lhs0.replace(variables[1], "({:s})".format(str(y)))
                rhs0 = rhs0.replace(variables[1], "({:s})".format(str(y)))
                app.logger.error(lhs0)
                app.logger.error(rhs0)

                if simplify(parse_expr(lhs0, transformations=transformations)-parse_expr(rhs0, transformations=transformations))!=0:
                    correct = False
                    message = "The points you entered are not on the line."
            if len(input_set_of_coordinate_pairs) < int(json.loads(Parameters['N'])):
                correct = False
            if QuestionData['Type'] in ['SetOfCoordinatePairsEquationAndPrediction']:
                x0 = Parameters['x0']
                y0 = form.answer.data
                lhs0 = lhs.replace(variables[0], "({:s})".format(str(x0)))
                rhs0 = rhs.replace(variables[0], "({:s})".format(str(x0)))
                lhs0 = lhs0.replace(variables[1], "({:s})".format(str(y0)))
                rhs0 = rhs0.replace(variables[1], "({:s})".format(str(y0)))
                app.logger.error(lhs0)
                app.logger.error(rhs0)
                if simplify(parse_expr(lhs0, transformations=transformations)-parse_expr(rhs0, transformations=transformations))!=0:
                    correct = False
                    message += "Your prediction is incorrect."
        except:
            message = "Coordinate pairs could not be read."
            correct = False
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['InputOutputTable']:
        form = CoordinatePairsForm(data=formdata)
        #form = CoordinatePairsForm()
        variables = Parameters['variables']
        if 'n' in Parameters:
            n = Parameters['n']
        else:
            n = len(Parameters['x'])
        input_coordinates = set()
        for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
            try:
                input_coordinates.add(tuple([int(coordinate_pair_form.x.data),int(coordinate_pair_form.y.data)]))
            except:
                message = "Coordinate pairs could not be read.".format(it+1)
                correct = False
                break
        try:
            if 'seed' in Parameters:
                random.seed(Parameters['seed'])
                x = [random.randint(-10,10) for i in range(n)]
                y = [random.randint(-10,10) for i in range(n)]
            else:
                x = Parameters['x']
                y = Parameters['y']
            coordinates = set(zip(x,y))
            correct = input_coordinates == coordinates
            app.logger.error(input_coordinates)
            app.logger.error(coordinates)
        except:
            message = "Coordinate pairs could not be read."
            correct = False

        for it in range(n):
            if len(form.coordinate_pair_forms.entries) < it+1:
                try:
                    form.coordinate_pair_forms.append_entry({'x': Parameters[variables[0]][it], 'y': Parameters[variables[1]][it]})
                except:
                    form.coordinate_pair_forms.append_entry()
                if variables[0] in Parameters and len(Parameters[variables[0]])>it and Parameters[variables[0]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].x)
                if variables[0] in Parameters and len(Parameters[variables[1]])>it and Parameters[variables[1]][it] is not None:
                    read_only(form.coordinate_pair_forms.entries[it].y)
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['CoordinatePairs']:
        form = CoordinatePairsForm(data=formdata)
        #form = CoordinatePairsForm()
        n = Parameters['n']
        choices = []
        for object_,_ in Parameters['objects'].items():
            choices.append((object_,object_))
        app.logger.error(choices)
        app.logger.error(len(form.coordinate_pair_forms.entries))
        for it,coordinate_pair_form in enumerate(form.coordinate_pair_forms.entries):
            try:
                object_ = coordinate_pair_form.object_.data
                app.logger.error(object_)
                app.logger.error(Parameters['objects'])
                coordinates = tuple(int(x.strip("() ")) for x in coordinate_pair_form.coordinate_pair.data.split(","))
                correct = (coordinates[0] == Parameters['objects'][object_][0] and coordinates[1] == Parameters['objects'][object_][1])
                if not correct:
                    message = "Coordinate pair number {:d} is incorrect.".format(it+1)
                    break
            except ValueError:
                message = "Coordinate pair number {:d} is incorrect.".format(it+1)
                correct = False
                break
        for it in range(n):
            if len(form.coordinate_pair_forms.entries) < it+1:
                form.coordinate_pair_forms.append_entry()
            form.coordinate_pair_forms[it].object_.choices = choices
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['SolveEquationGuided', 'SetUpAndSolveEquationGuided']:
        if QuestionData['Type'] == 'SetUpAndSolveEquationGuided':
            written = False
            #form = SetUpAndSolveEquationGuidedForm(MultiDict(formdata))
            #form = SetUpAndSolveEquationGuidedForm()
            form = SetUpAndSolveEquationGuidedForm(data=formdata)
            #form = EquationForm()
            n = len(Parameters['variables'])
            for it in range(n):
                form.equation_form.variables.append_entry()
                form.equation_form.quantities.append_entry()
            # Check answers
            # Answers array
            try:
                lhs_input = parse_expr(form.equation_form.lhs.data, transformations=transformations)
                rhs_input = parse_expr(form.equation_form.rhs.data, transformations=transformations)
                lhs,rhs = QuestionData['ParameterSetVariants'][i]['equation'].split("=")
                #lhs = BalanceQuestionData[q-1]['LHS']
                #rhs = BalanceQuestionData[q-1]['RHS']
                variables = []
                for it,variable in enumerate(Parameters['variables']):
                    if len(str(form.equation_form.variables[it].data)) > 1:
                        message = "Variables and units must be a single letter or the number 1"
                        raise Exception
                    variables.append(form.equation_form.variables[it].data)
                    lhs = lhs.replace(variable, "({:s})".format(form.equation_form.variables[it].data))
                    rhs = rhs.replace(variable, "({:s})".format(form.equation_form.variables[it].data))
                if len(variables) != len(set(variables)):
                    message = "Each variable or unit can be used only once."
                    raise Exception
                    
                lhs = parse_expr(lhs, transformations=transformations)
                rhs = parse_expr(rhs, transformations=transformations)
                correct = simplify(lhs-lhs_input) == 0 and simplify(rhs-rhs_input) == 0
                if not correct:
                    message = "Your equation does not represent this problem in one of the two forms listed above."
            except:
                lhs = form.equation_form.lhs.data
                rhs = form.equation_form.rhs.data
                correct = False
            if correct and (simplify(lhs-parse_expr(form.equation_form.variables[0].data, transformations=transformations))==0 or simplify(rhs-parse_expr(form.equation_form.variables[0].data, transformations=transformations))==0):
                message = "Your answer is correct"
                pass 
            else:
                if correct:
                    written = True
                    correct = False 
                else:
                    for entry in range(len(form.steps.entries)):
                        form.steps.pop_entry()
        else:
            #form = SolveEquationGuidedForm()
            #form = SolveEquationGuidedForm(MultiDict(formdata))
            form = SolveEquationGuidedForm(data=formdata)
            if len(form.steps.entries)==0:
                form.steps.append_entry()
            correct = True
        app.logger.error("test")
#        operations = []
#        operands = []
#        equations = []
        app.logger.error("form.steps.entries has length {:d}".format(len(form.steps.entries)))
        #stepform = form.steps.entries[0]
        #lhs,rhs = QuestionData['ParameterSetVariants'][i]['equation'].split("=")
        lhs,rhs = Parameters['equation'].split("=")
        if QuestionData['Type'] == 'SetUpAndSolveEquationGuided':
            try:
                for it,variable in enumerate(Parameters['variables']):
                    lhs = lhs.replace(variable, "({:s})".format(form.equation_form.variables[it].data))
                    rhs = rhs.replace(variable, "({:s})".format(form.equation_form.variables[it].data))
                    #lhs = lhs.replace(variable, form.equation_form.variables[it].data)
                    #rhs = rhs.replace(variable, form.equation_form.variables[it].data)
            except:
                pass
        #QuestionData['ParameterSetVariants'][i]['equation_latex'] = "{:s}={:s}".format(latex(parse_expr(lhs, transformations=transformations)),latex(parse_expr(rhs, transformations=transformations)))
        if 'equation_latex' not in Parameters.keys():
            Parameters['equation_latex'] = "{:s}={:s}".format(latex(parse_expr(lhs, transformations=transformations, evaluate=False)),latex(parse_expr(rhs, transformations=transformations, evaluate=False)))
        it = 0
        for it,stepform in enumerate(form.steps.entries):
        #while correct:
            try:
                operation = stepform.operation.data
                operand = stepform.operand.data
                if operation == 'None':
                    noop = True
                    operation = '+';
                    operand = '0';
                else:
                    noop = False
                new_lhs, new_rhs = stepform.new_equation.data.split("=")
            except:
                message = "Choose an operation (or choose simplify), decide what you want to add, subtract, multiply, or divide, and write a new equation."
#                if len(form.steps.entries)==it+1:
#                    form.steps.pop_entry()
                correct = False
                break
            try:
                app.logger.error(new_lhs)
                app.logger.error(new_rhs)
                app.logger.error(operation)
                app.logger.error(operand)
                app.logger.error(lhs)
                app.logger.error(rhs)
                if it==0:
                    app.logger.error(parse_expr("({:s}){:s}({:s})".format(lhs,operation,operand), transformations=transformations))
                    app.logger.error(parse_expr(new_lhs, transformations=transformations))
                    app.logger.error(parse_expr("({:s}){:s}({:s})".format(rhs,operation,operand), transformations=transformations))
                    app.logger.error(parse_expr(new_rhs, transformations=transformations))
                    correct = simplify(parse_expr("({:s}){:s}({:s})".format(lhs,operation,operand), transformations=transformations)-parse_expr(new_lhs, transformations=transformations))==0 and simplify(parse_expr("({:s}){:s}({:s})".format(rhs,operation,operand), transformations=transformations)-parse_expr(new_rhs, transformations=transformations))==0
                    if not correct:
                        message = "Your equation in step {:d} is incorrect.".format(it+1)
                    if noop:
                        simplified = len(sympify(parse_expr(new_lhs,evaluate=False, transformations=transformations),evaluate=False).args) <= len(simplify(parse_expr(lhs,transformations=transformations)).args) and len(sympify(parse_expr(new_rhs,evaluate=False, transformations=transformations),evaluate=False).args) <= len(simplify(parse_expr(rhs,transformations=transformations)).args)
                        correct = correct and simplified
                        if not simplified:
                            message = message+" Your equation in step {:d} is not simplified".format(it+1)
                else:
                    correct = simplify(parse_expr("({:s}){:s}({:s})".format(previous_lhs,operation,operand), transformations=transformations)-parse_expr(new_lhs, transformations=transformations))==0 and simplify(parse_expr("({:s}){:s}({:s})".format(previous_rhs,operation,operand), transformations=transformations)-parse_expr(new_rhs, transformations=transformations))==0
                    if not correct:
                        message = "Your equation in step {:d} is incorrect.".format(it+1)
                    if noop:
                        simplified = len(sympify(parse_expr(new_lhs,evaluate=False, transformations=transformations),evaluate=False).args) <= len(simplify(parse_expr(previous_lhs,transformations=transformations)).args) and len(sympify(parse_expr(new_rhs,evaluate=False, transformations=transformations),evaluate=False).args) <= len(simplify(parse_expr(previous_rhs,transformations=transformations)).args)
                        correct = correct and simplified
                        if not simplified:
                            message = message+" Your equation in step {:d} is not simplified".format(it+1)
                if correct:
                    previous_lhs,previous_rhs = new_lhs,new_rhs
#                    it = it+1
#                    form.steps.append_entry()
                    stepform = form.steps.entries[it]
                else:
                    break
                    #operations.append(operation)
                    #operands.append(operand)
                    #equations.append(stepform.new_equation.data)
            except IOError:
                message = "Your equation in step {:d} is incorrect".format(it+1)
                correct = False
                break
        for it0 in range(it+1,len(form.steps.entries)):
            form.steps.pop_entry()
        if QuestionData['Type'] == 'SetUpAndSolveEquationGuided':
            if written:
                if len(form.steps.entries)==0:
                    form.steps.append_entry()
        if QuestionData['Type'] == 'SolveEquationGuided':
            if len(form.steps.entries)==0:
                form.steps.append_entry()
        try:
            #if correct and simplify(parse_expr(new_lhs, transformations=transformations)-parse_expr("x", transformations=transformations))!=0:
            if QuestionData['Type'] == 'SolveEquationGuided':
                if correct and (simplify(parse_expr(new_lhs, transformations=transformations)-parse_expr(Parameters['variables'][0], transformations=transformations))!=0 and simplify(parse_expr(new_rhs, transformations=transformations)-parse_expr(Parameters['variables'][0], transformations=transformations))!=0):
                    form.steps.append_entry()
                    message = "Nice work! Keep going until you find the value of the variable!"
                    correct = False
                elif correct:
                    message = "Your answer {:s} is correct".format(stepform.new_equation.data)
                    #answer = stepform.new_equation.data
            if QuestionData['Type'] == 'SetUpAndSolveEquationGuided':
                if correct and (simplify(parse_expr(new_lhs, transformations=transformations)-parse_expr(form.equation_form.variables[0].data, transformations=transformations))!=0 and simplify(parse_expr(new_rhs, transformations=transformations)-parse_expr(form.equation_form.variables[0].data, transformations=transformations))!=0):
                    form.steps.append_entry()
                    message = "Nice work! Keep going until you find the value of the variable!"
                    correct = False
                elif correct:
                    try:
                    #answer = stepform.new_equation.data
                        message = "Your answer {:s} is correct".format(stepform.new_equation.data)
                    except:
                        message = "Your answer is correct"
        except:
            correct = False
        answer = json.dumps(form.data)
        app.logger.error(message)

        #if len(form.steps.entries)==0 or len(form.steps.entries)==i+1:
        #    form.steps.append_entry()
    if QuestionData['Type'] == 'OpenResponse':
        try:
            form = OpenResponseForm(data=formdata)
        except:
            form = OpenResponseForm()
        if request.method == 'POST':
            correct = True
        else:
            correct = False
        answer = json.dumps(form.data)
    if QuestionData['Type'] in ['MC','RubricScore']:
        try:
            form = MCForm(data=formdata)
        except:
            form = MCForm()
        choices = []
        markdown_include = MarkdownInclude(
                               configs={'base_path':app.config['MARKDOWN_INCLUDE_PATH']}
                               )
        md = markdown.Markdown(extensions=['mdx_math','attr_list','markdown.extensions.extra','markdown.extensions.meta',markdown_include])
        if 'Choices' in QuestionData['ParameterSetVariants'][i]:
            for k,choice in QuestionData['ParameterSetVariants'][i]['Choices']:
                choices.append((k,md.convert(choice)))
        else:
            for k,choice in QuestionData['Choices']:
                choices.append((k,md.convert(choice)))
        form.options.choices = choices
        try:
            choice = form.options.data
            app.logger.error(choice)
#            if form.other.data:
#                answer = form.other.data
#            else:
#                answer = choice
            if QuestionData['Type'] in ['RubricScore']:
                correct = form.options.data
            else:
                if choice == QuestionData['ParameterSetVariants'][i]['CorrectAnswer']:
                    correct = True
                else:
                    correct = False
        except ValueError:
            correct = False
        app.logger.error(choice)
    if QuestionData['Type'] == 'Numerical':
        form = NumericalForm()
        answer = form.answer.data
        CorrectAnswer = QuestionData['ParameterSetVariants'][i]['CorrectAnswer']
        if answer is not None:
            try:
                correct = int(answer)-CorrectAnswer == 0
            except:
                correct = False
        # Check answers
        # Answers array
    if QuestionData['Type'] == 'Expression':
        form = ExpressionForm()
        try:
            answer = parse_expr(form.answer.data, transformations=transformations)
            CorrectAnswer = parse_expr(QuestionData['ParameterSetVariants'][i]['CorrectAnswer'], transformations=transformations)
            correct = simplify(answer-CorrectAnswer) == 0
        except:
            pass
        # Check answers
        # Answers array
    content = render_template(QuestionData['Template'], form=form, **Parameters)
    if request.method == 'POST':
        question = get_or_create(db.session, Question, assignment=assignment, number=q, variant_index=i)
        db.session.commit()
        if QuestionData['Type'] in ['Matching', 'RubricScore']:
            statement = question_scores.insert().values(user_id=user.id, question_id=question.id, answer=answer, score=correct)
        else:
            statement = question_scores.insert().values(user_id=user.id, question_id=question.id, answer=answer, score=bool(correct))
        db.session.execute(statement)
        db.session.commit()
        if not QuestionSets[assignment]['ProvideImmediateFeedback']:
            print("test")
            return(redirect(url_for('Assignment', assignment=assignment)))
    if 'Test' in QuestionSets[assignment] and QuestionSets[assignment]['Test']:
        test = True
    else:
        test = False
    scores = []
    for j,question in enumerate(QuestionSets[assignment]['Questions']):
        for k in range(len(question['ParameterSetVariants'])):
            question_indices.append((j+1,k))
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment==assignment,Question.__table__.c.number==j+1, Question.__table__.c.variant_index==k)).order_by(desc('datetime'))
            results = db.session.execute(statement).first()
            if not results:
                scores.append("NA")
            else:
                scores.append(results.score)
            if (q,i)==(j+1,k):
                question_number = len(question_indices)
            
    try:
        title = QuestionSets[assignment]['Title']
    except:
        title = None
    return dict(title=title, content=content, assignment=assignment, answer=answer, form=form, q=q, i=i, NextQuestion=NextQuestion, correct=correct, QuestionData=QuestionData, question_indices=question_indices, question_number=question_number, message=message,Parameters=Parameters, scores=scores, test=test)


@app.route('/RepresentBalances/<q>', methods=['GET', 'POST'])
@app.route('/RepresentBalances/', methods=['GET', 'POST'])
@templated('MarkdownQuestion.html')
@lti(request='session', error=error, app=app)
def RepresentBalances(lti=lti, q=None):
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if q is None:
        for i in range(len(BalanceQuestionData)):
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.number==i+1, question_scores.c.score==1))
            results = db.session.execute(statement).first()
            if not results:
                q = i+1
                break
    if not user:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)
    if q == 'submit':
        lti.post_grade(1)
        return render_template('grade.html', form=form)
    q = int(q)
    @after_this_request
    def add_header(response):
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    from sympy import simplify, symbols
    from sympy.parsing.sympy_parser import parse_expr
    from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
    transformations = (standard_transformations + (implicit_multiplication_application,))
    assignment = 'RepresentBalances'
    a,b = symbols("a b")
#    markdown_include = MarkdownInclude(
#                           configs={'base_path':app.config['MARKDOWN_INCLUDE_PATH']}
#                           )
#    md = markdown.Markdown(extensions=['mdx_math','attr_list','markdown.extensions.extra','markdown.extensions.meta',markdown_include])
#    with open(os.path.join(app.config['RESOURCES_DIR'],'RepresentBalances', 'Question{:d}.md'.format(q)), 'rb') as f:
#        source = f.read()
#    result = md.convert(source.decode('utf-8'))
#    try:
#        title = md.Meta['title'][0]
#    except:
#        title = 'untitled'
    form = EquationForm()
    n = len(BalanceQuestionData[q-1]['Variables'])
    for i in range(n):
        form.variables.append_entry()
    # Check answers
    # Answers array
    try:
        lhs_input = parse_expr(form.lhs.data, transformations=transformations)
        rhs_input = parse_expr(form.rhs.data, transformations=transformations)
        lhs = BalanceQuestionData[q-1]['LHS']
        rhs = BalanceQuestionData[q-1]['RHS']
        for i,variable in enumerate(BalanceQuestionData[q-1]['Variables']):
            lhs = lhs.replace(variable, form.variables[i].data)
            rhs = rhs.replace(variable, form.variables[i].data)
        lhs = parse_expr(lhs, transformations=transformations)
        rhs = parse_expr(rhs, transformations=transformations)
        correct = simplify(lhs-lhs_input) == 0 and simplify(rhs-rhs_input) == 0
    except:
        lhs = form.lhs.data
        rhs = form.rhs.data
        correct = False
    if request.method == 'POST':
        question = get_or_create(db.session, Question, assignment=assignment, number=q)
        db.session.commit()
        statement = question_scores.insert().values(user_id=user.id, question_id=question.id, score=bool(correct))
        db.session.execute(statement)
        db.session.commit()
    if len(BalanceQuestionData) > q+1:
        NextQuestion = q+1
    else:
        NextQuestion = None
    return dict(title='Representing balance scales', content='', form=form, q=q, NextQuestion=NextQuestion, lhs=lhs, rhs=rhs, correct=correct, QuestionData=BalanceQuestionData[q-1])

@app.route('/markdown/<filename>')
@templated('markdown.html')
def markdown_view(lti=lti, filename=None):
    @after_this_request
    def add_header(response):
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    markdown_include = MarkdownInclude(
                           configs={'base_path':app.config['MARKDOWN_INCLUDE_PATH']}
                           )
    md = markdown.Markdown(extensions=['mdx_math','attr_list','markdown.extensions.extra','markdown.extensions.meta',markdown_include])
    with open(os.path.join(app.config['RESOURCES_DIR'],filename), 'rb') as f:
        source = f.read()
    result = md.convert(source.decode('utf-8'))
    try:
        title = md.Meta['title'][0]
    except:
        title = 'untitled'
    return dict(title=title, content=result)

@app.route('/is_up', methods=['GET'])
def hello_world(lti=lti):
    """ Indicate the app is working. Provided for debugging purposes.

    :param lti: the `lti` object from `pylti`
    :return: simple page that indicates the request was processed by the lti
        provider
    """
    return render_template('up.html', lti=lti)

@app.route('/rubric/<username>/<assignment>', methods=['GET', 'POST'])
@lti(request='session', error=error, app=app)
def rubric(lti=lti, assignment=None, username=None):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    app.logger.error(user.username)
    if user:
        app.logger.error(os.path.join(app.config['PRIVATE_DATA_PATH'], user.username), "{:s}.pdf".format(assignment))
        return send_from_directory(
            os.path.join(app.config['PRIVATE_DATA_PATH'], user.username),
            "{:s}.pdf".format(assignment)
        )
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET'])
@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    #app.logger.error(user.username)
    if user:
        try:
            statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.assignment=='SolvingEquationsTest', Question.__table__.c.number==11, Question.__table__.c.variant_index==0)).order_by(desc('datetime'))
            results = db.session.execute(statement).first()
            focus_areas = json.loads(results.answer)['answers']
        except:
            focus_areas = []
        return render_template('index.html', user=user, lti=lti, focus_areas=focus_areas)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@app.route('/assignments', methods=['GET', 'POST'])
@lti(request='session', error=error, app=app)
def assignments(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)


@app.route('/userinfo', methods=['GET','POST'])
@lti(request='session', error=error, app=app)
def SetUserInfo(lti=lti):
    from sqlalchemy.sql.expression import ClauseElement
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        user.username = form.username.data
    else:
        form = UserInfoForm()
        user = User(lti_user_id=lti.name, username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data)
        db.session.add(user)
    db.session.commit()
    return render_template('index.html', user=user)


@app.route('/index_staff', methods=['GET', 'POST'])
@lti(request='session', error=error, role='staff', app=app)
def index_staff(lti=lti):
    """ render the contents of the staff.html template

    :param lti: the `lti` object from `pylti`
    :return: the staff.html template rendered
    """
    return render_template('staff.html', lti=lti)

def set_debugging():
    """ enable debug logging

    """
    import logging
    import sys

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

#set_debugging()

if __name__ == '__main__':
    """
    For if you want to run the flask development server
    directly
    """
    port = int(os.environ.get("FLASK_LTI_PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", "localhost")
    app.run(debug=True, host=host, port=port)
