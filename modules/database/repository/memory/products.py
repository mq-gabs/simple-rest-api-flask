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
      if product.id == id and not product.deleted_at:
        found_product = product

    return found_product

  def update(self, id: str, updated: Product) -> Product:
    new_products = []
    for product in self.products:
      if product.id == id:
        new_products.append(updated)
      else:
        new_products.append(product)
    
    self.products = new_products.copy()

    return updated

  def delete(self, id: str):
    new_products = []
    for product in self.products:
      if product.id == id:
        product.deleted_at = str(datetime.now())
      new_products.append(product)

    self.products = new_products.copy()
    