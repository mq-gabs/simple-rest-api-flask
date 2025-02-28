from .dtos.product_dto import ProductDto
from utils.request.query import Query
from utils.response.list import ListResponse
from modules.database.repository.abstract.products import AbstractProductsRepository
from modules.products.entity import Product

class ProductsServices:
  def __init__(self, repo: AbstractProductsRepository):
    self.repo = repo
  
  def create(self, dto: ProductDto) -> Product:
    product = Product()
    product.name = dto.name
    product.description = dto.description

    result = self.repo.save(product)

    return result

  def get_many(self, query: Query) -> ListResponse:
    result = self.repo.get_many(query)

    return result

  def get_one(self, id: str) -> Product:
    result = self.repo.get_one(id)
    return result
  
  def update(self, id: str, dto: ProductDto) -> Product:
    product = self.repo.get_one(id)

    if dto.name:
      product.name = dto.name
    if dto.description:
      product.description = dto.description
    if dto.status:
      product.status = dto.status

    result = self.repo.update(id, product)

    return result
  
  def delete(self, id: str):
    self.repo.delete(id)
