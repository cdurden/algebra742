"""
Configuration file for flask sample application
"""
import os

# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "you-will-never-guess")
AUTH_TOKEN = os.environ.get("FLASK_AUTH_TOKEN", "another-secret")

# Sample client certificate example for 12 factor app
# You would want to store your entire pem in an environment variable
# with something like:
# ```
# export CONSUMER_KEY_CERT=$(cat <<EOF
# < paste cert here>
# EOF
# )
# ```

SQLALCHEMY_DATABASE_URI = 'mysql://www-data:password@localhost/algebra742live'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{:s}'.format(os.path.abspath(os.path.join(os.path.dirname(__file__),'algebra742.db')))
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

CONSUMER_KEY_PEM_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),'consumer_key.pem'))
with open(CONSUMER_KEY_PEM_FILE, 'w') as wfile:
    wfile.write(os.environ.get('CONSUMER_KEY_CERT', ''))

PYLTI_CONFIG = {
    "consumers": {
        "__consumer_key__": {
            "secret": os.environ.get("CONSUMER_KEY_SECRET", "__lti_secret__"),
            "cert": CONSUMER_KEY_PEM_FILE
        }
    }
}

# Remap URL to fix edX's misrepresentation of https protocol.
# You can add another dict entry if you have trouble with the
# PyLti URL.
PYLTI_URL_FIX = {
    "https://localhost:8000/": {
        "https://localhost:8000/": "http://localhost:8000/"
    },
    "https://localhost/": {
        "https://localhost/": "http://192.168.33.10/"
    }
}

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')
MARKDOWN_INCLUDE_PATH = os.path.join(os.path.dirname(__file__), 'resources', 'include')
PRIVATE_DATA_PATH = os.path.join(os.path.dirname(__file__), 'private')
QUESTION_DIGRAPHS_DIR = os.path.join(os.path.dirname(__file__), 'content', 'question_digraphs')
GRAPHICS_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'content','graphics','templates')
GRAPHICS_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'content','graphics','output')
