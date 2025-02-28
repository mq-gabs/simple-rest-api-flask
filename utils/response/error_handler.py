from flask import Flask
from werkzeug.exceptions import HTTPException
from json import dumps
from utils.response.app_error import AppError

def set_error_handler(app: Flask):
  @app.errorhandler(AppError)
  def error_handler(e: AppError):
    response = HTTPException().get_response()
    response.content_type = "application/json"
    response.status_code = e.status_code
    response.data = dumps(e.toJSON())
    return response

  @app.errorhandler(HTTPException)
  def general_error_handler(e: HTTPException):
    response = e.get_response()
    response.content_type = "application/json"
    response.data = dumps({
      "status_code": 500,
      "message": "Internal Server Error",
      "details": e.description
    })
    return response 
