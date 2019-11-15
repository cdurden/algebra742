#import gevent.monkey
#gevent.monkey.patch_all()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO
from flask_redis import FlaskRedis
from . import default_config
#from models import Game

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
    app.config.from_envvar('ALGEBRA742LIVE_SETTINGS')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .models import QuestionGame, Question
        global ROOMS
        try:
            question = Question.query.get(1)
        except:
            question = Question(question='What is 1+1?')
            db.session.add(question)
        ROOMS += [QuestionGame(question)]

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')

