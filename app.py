from flask import Flask
from modules.index import set_routes
from utils.response.error_handler import set_error_handler

app = Flask('MyApp')

set_routes(app)
set_error_handler(app)
