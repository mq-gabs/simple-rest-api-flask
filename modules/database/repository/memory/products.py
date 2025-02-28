from modules.database.repository.abstract.products import AbstractProductsRepository
from utils.response.error import AppError
from datetime import datetime
from modules.products.entity import Product
from utils.request.query import Query
from utils.response.list import ListResponse

class ProductsMemoryRepository(AbstractProductsRepository):
  products: list[Product] = []

  def save(self, product: Product) -> Product:
    self.products.append(product)
    return product

  def get_many(self, query: Query) -> ListResponse:
    return ListResponse(self.products, len(self.products))

  def get_one(self, id: str) -> Product:
    found_product = None
    for product in self.products:
      if product.id == id:
        found_product = product
    
    if not found_product:
      raise AppError(404, f'Product not found with id: {id}')
    
    return found_product

  def update(self, id: str, updated: Product) -> Product:
    updated_product = self.get_one(id)

    updated_product.name = updated.name
    updated_product.description = updated.description
    updated_product.status = updated.status
    updated_product.updated_at = str(datetime.now())

    new_products = []
    for product in self.products:
      if product.id == id:
        new_products.append(updated_product)
      else:
        new_products.append(product)
    
    self.products = new_products.copy()

    return updated_product

  def delete(self, id: str):
    self.get_one(id)

    new_products = []
    for product in self.products:
      if product.id == id:
        product.deleted_at = str(datetime.now())
      new_products.append(product)
    