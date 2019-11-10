#import gevent.monkey
#gevent.monkey.patch_all()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO
from flask_redis import FlaskRedis
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
    app.config.from_object('config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .models import Game
        global ROOMS
        ROOMS += [Game()]

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

        return app

#if __name__ == '__main__':
#    socketio.run(app, debug=True, host='0.0.0.0')

