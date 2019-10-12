from algebra742 import db
connection = db.engine.raw_connection()
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS algebra742;")
db.create_all()
