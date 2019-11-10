#import gevent.monkey
#gevent.monkey.patch_all()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
from models import Player, Game, RequestDenied

# initialize Flask
from pylti.flask import lti
from models import db, User, error
VERSION = '0.0.1'
#app = Flask(__name__)
#app.config.from_object('config')
#ROOMS = {} # dict to track active rooms
#DATA = {}
ROOM = Game()
socketio = SocketIO()
db = SQLAlchemy()
r = FlaskRedis()
#db = SQLAlchemy(app)

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')

