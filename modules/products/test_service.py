import unittest
from modules.database.repository.memory.products import ProductsMemoryRepository
from .service import ProductsServices
from .dtos.product_dto import ProductDto
from .entity import Product
from utils.request.query import Query

class TestProductsServices(unittest.TestCase):
  repo = ProductsMemoryRepository()
  service = ProductsServices(repo)

  def setUp(self):
    self.repo.products = []

  def test_create(self):
    dto = ProductDto()
    dto.name = 'Name'
    dto.description = 'Description'

    result = self.service.create(dto)

    self.assertTrue(type(result) == Product)
    self.assertEqual(dto.name, result.name)
    self.assertEqual(dto.description, result.description)

  def test_get_many(self):
    dto = ProductDto()
    dto.name = 'Name'
    dto.description = 'Description'

    product = self.service.create(dto)

    query = Query()
    result = self.service.get_many(query)

    self.assertEqual(result.list, [product])
    self.assertEqual(result.total, 1)
  
  def test_get_one(self):
    dto = ProductDto()
    dto.name = 'Name'
    dto.description = 'Description'

    product = self.service.create(dto)

    result = self.service.get_one(product.id)

    self.assertEqual(result, product)

  def test_update(self):
    dto = ProductDto()
    dto.name = 'Name'
    dto.description = 'Description'

    product = self.service.create(dto)

    other_dto = ProductDto()
    other_dto.name = 'New name'
    other_dto.description = 'New description'

    result = self.service.update(product.id, other_dto)

    self.assertEqual(result.name, other_dto.name)
    self.assertEqual(result.description, other_dto.description)
  
  def test_delete(self):
    dto = ProductDto()
    dto.name = 'Name'
    dto.description = 'Description'

    product = self.service.create(dto)

    self.service.delete(product.id)

    result = self.service.get_one(product.id)

    self.assertEqual(result, None)


