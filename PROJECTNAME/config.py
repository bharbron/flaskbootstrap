import os

class DevelopmentConfig(object):
  SQLALCHEMY_DATABASE_URI = "postgresql://vagrant@localhost:5432/PROJECTNAME"
  DEBUG = True
  SECRET_KEY = os.environ.get("PROJECTNAME_SECRET_KEY", "foobar")
  LOGCONFIG_PATH = "grubhubbub/logconfig.dev.json"