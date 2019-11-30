#import gevent.monkey
#gevent.monkey.patch_all()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO
from flask_redis import FlaskRedis
from . import default_config
from . import config
import json

from sqlalchemy_utils import create_database, database_exists

# initialize Flask
#VERSION = '0.0.1'
#app = Flask(__name__)
#app.config.from_object('config')
ROOMS = [] # dict to track active rooms
#DATA = {}
#ROOM = None
socketio = SocketIO()
db = SQLAlchemy()
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
        from .models import QuestionGame, Node, SinglyLinkedList, get_or_create
        from .models.Question import PlotQuestion, QuestionOnePlusOne, MultiPartQuestion
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()
        global ROOMS
        questions = SinglyLinkedList()
        #for json_data in ['{"question": "What is $1+1$?"}', '{"question": "What is 2+1?"}']:
        #    question = get_or_create(db.session, QuestionOnePlusOne, params_json=json_data)
        #    questions.append(question)
        params = {'parts': [{'class': 'Question.QuestionOnePlusOne', 'params': {"question": "What is $1+1$?"}}, {'class': 'Question.QuestionOnePlusOne', 'params': {"question": "What is 2+1?"}},{'class': 'Question.PlotQuestion', 'params': {'question': 'test'}}]}
        question = get_or_create(db.session, MultiPartQuestion, params_json=json.dumps(params))
        questions.append(question)
        ROOMS += [QuestionGame(questions)]
        print(ROOMS[0].active_question)

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')

