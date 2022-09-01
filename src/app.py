from flask import Flask
from src.routes.routes import *


app = Flask(__name__)

app.config.from_mapping(SECRET_KEY='development')

app.add_url_rule(routes["index_route"], view_func = routes["index_controller"])