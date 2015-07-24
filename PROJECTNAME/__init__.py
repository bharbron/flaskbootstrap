import os
import json

from flask import Flask

import logging
import logging.config

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "PROJECTNAME.config.DevelopmentConfig")
app.config.from_object(config_path)

with open(app.config["LOGCONFIG_PATH"], 'r') as f:
	logconfig = json.load(f)
logging.config.dictConfig(logconfig)

app.logger.info("Running with CONFIG_PATH: {}".format(config_path))

from . import views
from . import filters
from . import login

from database import Base, engine
app.logger.debug("Creating all metadata for Base")
Base.metadata.create_all(engine)