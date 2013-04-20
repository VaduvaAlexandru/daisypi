'''Model the entities.'''

import flask

import daisy

DB = flask.ext.sqlalchemy.SQLAlchemy(daisy.app)
