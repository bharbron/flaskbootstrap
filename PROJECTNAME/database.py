from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

from PROJECTNAME import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def get_one_or_create(session, model, **kwargs):
  try:
    return session.query(model).filter_by(**kwargs).one()
  except NoResultFound:
    return model(**kwargs)