#import gevent.monkey
#gevent.monkey.patch_all()
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import json
from flask_restful import Resource, Api
import flask_restful
from flask_socketio import SocketIO
from flask_redis import FlaskRedis
from flask_bootstrap import Bootstrap
from . import default_config
try:
    from . import config
except ImportError:
    pass
from models import db
from models.Question import questions_digraph_factory
from models.Game import GameClasses
import json
from networkx.drawing.nx_pydot import read_dot
import os
import sys
#from flask.logging import default_handler
#import logging
#app.logger.addHandler(default_handler)
#logging.getLogger("chat")

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

#import flask.ext.restful.representations.json

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            print("running AlchemyEncoder on object "+obj+" of class "+obj.__class__)
            #if isinstance(obj.__class__, DeclarativeMeta):
            if isinstance(obj.__class__, db.Model):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder

class AlchemyEncoderMiddleWare(object):
    """Simple WSGI middleware"""
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        app.config['RESTFUL_JSON']["cls"] = new_alchemy_encoder() 
        return self.app(environ, start_response)

#def new_alchemy_encoder(revisit_self = False, fields_to_expand = []):
#    _visited_objs = []
#
#    class AlchemyEncoder(json.JSONEncoder):
#        def default(self, obj):
#            if isinstance(obj.__class__, DeclarativeMeta):
#                # don't re-visit self
#                if revisit_self:
#                    if obj in _visited_objs:
#                        return None
#                    _visited_objs.append(obj)
#
#                # go through each field in this SQLalchemy class
#                fields = {}
#                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                    val = obj.__getattribute__(field)
#
#                    # is this field another SQLalchemy object, or a list of SQLalchemy objects?
#                    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
#                        # unless we're expanding this field, stop here
#                        if field not in fields_to_expand:
#                            # not expanding this field: set it to None and continue
#                            fields[field] = None
#                            continue
#
#                    fields[field] = val
#                # a json-encodable dict
#                return fields
#
#            return json.JSONEncoder.default(self, obj)
#
#    return AlchemyEncoder

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(default_config)
    if 'config' in sys.modules:
        app.config.from_object(config)
    app.config.from_envvar('ALGEBRA742LIVE_SETTINGS')
    app.logger.error(app.config["SQLALCHEMY_DATABASE_URI"])
    app.config.update(
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_HTTPONLY=True,
            SESSION_COOKIE_SAMESITE=None,
    )
    Bootstrap(app)

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .models.Game import QuestionDigraphGame, RevealJSPresentationGame
        from .models.Question import QuestionClasses
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
        global ROOMS
        #questions = SinglyLinkedList()
        #questions_digraph = questions_digraph_factory("ch5")
#        questions_digraph = read_dot(os.path.join(app.config["DOT_PATH"],'task1.dot'))
#        print(questions_digraph.graph)
#        for node,data in questions_digraph.nodes(data=True):
#            for k,v in data.items():
#                data[k.strip("\"")] = data.pop(k).strip("\"").replace("\\","")
#            print(data)
#            question = get_or_create(db.session, QuestionClasses[data['class']], params_json=data['params'])
#            data['_question_obj'] = question
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

        #app.extensions['redis'].set('template',"reveal.html".encode('utf-8'))
        app.extensions['redis'].set('game',"RevealJSPresentationGame".encode('utf-8'))
        app.extensions['redis'].set('params','{"template": "sample.html"}'.encode('utf-8'))
        app.wsgi_app = AlchemyEncoderMiddleWare(app.wsgi_app)
        #template = app.extensions['redis'].get('template').decode('utf-8')
        game = GameClasses[app.extensions['redis'].get('game').decode('utf-8')]
        params = app.extensions['redis'].get('params').decode('utf-8')
        print(params)
        ROOMS += [game(**json.loads(params))]

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')
