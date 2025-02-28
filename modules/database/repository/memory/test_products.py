import unittest
from .products import ProductsMemoryRepository
from modules.products.entity import Product
from utils.request.query import Query
from utils.response.list import ListResponse

class TestProductMemoryRepository(unittest.TestCase):
  repo: ProductsMemoryRepository = ProductsMemoryRepository()

  def setUp(self):
    self.repo.products = []

  def test_save(self):
    product = Product()

    self.repo.save(product)

    self.assertEqual(self.repo.products, [product])

  def test_get_many(self):
    product = Product()

    self.repo.save(product)

    query = Query()

    result = self.repo.get_many(query)

    self.assertEqual(result.list, [product])
    self.assertEqual(result.total, 1)

  def test_get_one(self):
    product = Product()

    self.repo.save(product)

    result = self.repo.get_one(product.id)

    self.assertEqual(result, product)

  def test_update(self):
    product = Product()

    self.repo.save(product)

    new_name = 'New Name'
    product.name = new_name

    self.repo.update(product.id, product)

    result = self.repo.get_one(product.id)

    self.assertEqual(result.name, new_name)

  def test_delete(self):
    product = Product()

    self.repo.save(product)

    self.repo.delete(product.id)

    self.assertEqual(self.repo.products, [product])
    self.assertNotEqual(self.repo.products[0].deleted_at, None)