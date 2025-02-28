from flask import Flask, request
from utils.request.query import Query
from .service import ProductsServices
from modules.database.repository.memory.products import ProductsMemoryRepository
from .dtos.product_dto import ProductDto
import uuid
from utils.response.response import Response
from utils.response.app_error import AppError
from json import dumps

repo = ProductsMemoryRepository()
service = ProductsServices(repo)

def set_products_routes(app: Flask):
  @app.post("/products")
  def create():
    data = request.get_json()
    dto = ProductDto()
    dto.name = data.get("name")
    dto.description = data.get("description")
    dto.price = data.get("price")

    result = service.create(dto)
    return dumps(result.toJSON())

  @app.get("/products")
  def get_many():
    query = Query()
    query.page = request.args.get("page")
    query.pageSize = request.args.get("pageSize")

    result = service.get_many(query)

    return dumps(result.toJSON())

  @app.get("/products/<uuid:id>")
  def get_one(id: uuid.UUID):
    result = service.get_one(str(id))

    return dumps(result.toJSON())
  
  @app.patch("/products/<uuid:id>")
  def update(id: uuid.UUID):
    data = request.get_json()
    dto = ProductDto()
    dto.name = data.get("name")
    dto.description = data.get("description")
    dto.price = data.get("price")
    dto.status = data.get("status")

    result = service.update(str(id), dto)
    return dumps(result.toJSON())

  @app.delete("/products/<uuid:id>")
  def delete(id: uuid.UUID):
    service.delete(str(id))
    return dumps(Response("Product deleted").toJSON())