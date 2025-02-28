import unittest
from .entity import Product
from utils.enums.status import EProductStatus

class TestProductEntity(unittest.TestCase):
  product: Product = None

  def setUp(self):
    self.product = Product()

  def test_toJSON(self):
    result = self.product.toJSON()
    expected = {
      "id": self.product.id,
      "created_at": self.product.created_at,
      "updated_at": self.product.updated_at,
      "deleted_at": self.product.deleted_at,
      "name": self.product.name,
      "description": self.product.description,
      "price": self.product.price,
      "status": self.product.status.name,
    }
  
    self.assertEqual(result, expected)

  def test_props(self):
    self.assertEqual(self.product.price, 0)
    self.assertEqual(self.product.status, EProductStatus.AVAILABLE)
  
  def test_update(self):
    new_name = 'Name'
    new_description = 'Description'
    new_price = 1200
    new_status = EProductStatus.UNAVAILABLE

    self.product.name = new_name
    self.product.description = new_description
    self.product.price = new_price
    self.product.status = new_status.name

    self.assertEqual(new_name, self.product.name)
    self.assertEqual(new_description, self.product.description)
    self.assertEqual(new_price, self.product.price)
    self.assertEqual(new_status, self.product.status)


  def test_update_error(self):
    error = False

    try:
      self.product.name = (self.product.MAX_NAME_LENGTH + 1)*'a'
    except:
      error = True

    self.assertTrue(error, 'name validation has failed')

    error = False

    try:
      self.product.description = (self.product.MAX_DESCRIPTION_LENGTH + 1)*'a'
    except:
      error = True
    
    self.assertTrue(error, 'description validation has failed')

    error = False

    try:
      self.product.price = -1
    except:
      error = True

    self.assertTrue(error, 'price validation has failed')

    error = False

    try:
      self.product.status = 'WRONG_STATUS'
    except:
      error = True

    self.assertTrue(error, 'status validation has failed')