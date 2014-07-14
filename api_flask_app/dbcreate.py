# Go ahead, make my day....tabase.
# creates the databasebased on the models we've defined in models.py

from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all()