from modules.products.controllers import set_products_routes
from flask import Flask

def set_routes(app: Flask):
  set_products_routes(app)