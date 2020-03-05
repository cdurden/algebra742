#import gevent.monkey
#gevent.monkey.patch_all()
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO
from flask_redis import FlaskRedis
from . import default_config
from . import config
from models import db
import json
from networkx.drawing.nx_pydot import read_dot
import os

from sqlalchemy_utils import create_database, database_exists

# initialize Flask
#VERSION = '0.0.1'
#app = Flask(__name__)
#app.config.from_object('config')
ROOMS = [] # dict to track active rooms
#DATA = {}
#ROOM = None
socketio = SocketIO()
#db = SQLAlchemy()
r = FlaskRedis()
#db = SQLAlchemy(app)
def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(default_config)
    app.config.from_object(config)
    app.config.from_envvar('ALGEBRA742LIVE_SETTINGS')
    app.logger.error(app.config["SQLALCHEMY_DATABASE_URI"])

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .models import QuestionDigraphGame, RevealJSPresentationGame, Node, SinglyLinkedList, get_or_create
        from .models.Question import QuestionOnePlusOne, MultiPartQuestion
        QuestionClasses = {
            'Question.MultiPartQuestion': MultiPartQuestion,
            'Question.QuestionOnePlusOne': QuestionOnePlusOne,
        }
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
        global ROOMS
        #questions = SinglyLinkedList()
        questions_digraph = read_dot(os.path.join(app.config["DOT_PATH"],'task1.dot'))
        print(questions_digraph.graph)
        for node,data in questions_digraph.nodes(data=True):
            for k,v in data.items():
                data[k.strip("\"")] = data.pop(k).strip("\"").replace("\\","")
            print(data)
            question = get_or_create(db.session, QuestionClasses[data['class']], params_json=data['params'])
            data['_question_obj'] = question
#        params = {'parts': [{'class': 'Question.QuestionOnePlusOne', 'params': {"question": "What is $1+1$?"}}, {'class': 'Question.QuestionOnePlusOne', 'params': {"question": "What is 2+1?"}},{'class': 'Question.PlotQuestion.PlotQuestion', 'params': {'question': 'test'}}, {'class': 'Question.Sort.Sort', 'params': 
#            {'background_style': "background-image: url(\"/static/deck12/bg.png\"); background-position:center; background-repeat:no-repeat; background-size: contain; width: 800px; height: 600px; position: relative;",
#             'layout_style': 'padding: 310px 0px 0px 0px',
#             'shuffle': [0 ,3 ,1 ,2],
#             'solutions': [0, 1, 2, 3],
#             'cards': [{'html': '<img src="/static/deck12/tile1.png"/>', 'blank_html': '', 'style': 'padding: 10px 50px 10px 75px; height: 80px; width: fit-content;'},
#                       {'html': '<img src="/static/deck12/tile2.png"/>', 'blank_html': '', 'style': 'padding: 10px 50px 10px 75px; height: 80px; width: fit-content;'},
#                       {'html': '<img src="/static/deck12/tile3.png"/>', 'blank_html': '', 'style': 'padding: 10px 50px 10px 75px; height: 80px; width: fit-content;'},
#                       {'html': '<img src="/static/deck12/tile4.png"/>', 'blank_html': '', 'style': 'padding: 10px 50px 10px 75px; height: 80px; width: fit-content;'}]
#                    },
#}]}
#        question = get_or_create(db.session, MultiPartQuestion, params_json=json.dumps(params))
#        questions.append(question)
        #ROOMS += [QuestionDigraphGame(questions_digraph)]
        ROOMS += [RevealJSPresentationGame()]

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')

