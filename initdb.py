from algebra742 import db,app
from sqlalchemy_utils import create_database, database_exists
url = app.config['SQLALCHEMY_DATABASE_URI']
if not database_exists():
    create_database(url)
db.create_all()
