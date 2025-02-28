from abc import ABC, abstractmethod
from modules.products.entity import Product
from utils.request.query import Query
from utils.response.list import ListResponse

class AbstractProductsRepository(ABC):
  @abstractmethod
  def save(product: Product) -> Product:
    pass

  @abstractmethod
  def get_many(query: Query) -> ListResponse:
    pass

  @abstractmethod
  def get_one(id: str) -> Product:
    pass

  @abstractmethod
  def update(id: str, updated: Product) -> Product:
    pass

  @abstractmethod
  def delete(id: str):
    pass