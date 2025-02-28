import unittest
from .entity import Base
from datetime import datetime
import uuid

class TestBaseEntity(unittest.TestCase):
  base: Base = None

  def setUp(self):
    self.base = Base()

  def test_toJSON(self):
    result = self.base.toJSON()
    expected = {
      "id": self.base.id,
      "created_at": self.base.created_at,
      "updated_at": self.base.updated_at,
      "deleted_at": self.base.deleted_at
    }

    self.assertEqual(result, expected)
  
  def test_uuid(self):
    error = False
    try:
      uuid.UUID(self.base.id)
    except:
      error = True
    
    self.assertFalse(error, f'{self.base.id} is invalid UUID')
  
  def test_dates(self):
    error = False

    try:
      datetime_created_at = datetime.strptime(self.base.created_at, self.base.DATE_FORMAT)
      datetime_updated_at = datetime.strptime(self.base.updated_at, self.base.DATE_FORMAT)
    except:
      error = True
    
    self.assertFalse(error, f'error while converting dates from string to datetime: created_at = {self.base.created_at}, updated_at: {self.base.updated_at}')
    self.assertEqual(self.base.deleted_at, None)
  
  def test_update(self):
    new_id = str(uuid.uuid4())
    new_date = str(datetime.now())

    self.base.id = new_id
    self.base.created_at = new_date
    self.base.updated_at = new_date
    self.base.deleted_at = new_date

    self.assertEqual(new_id, self.base.id)
    self.assertEqual(new_date, self.base.created_at)
    self.assertEqual(new_date, self.base.updated_at)
    self.assertEqual(new_date, self.base.deleted_at)

  def test_update_error(self):
    error = False

    try:
      self.base.id = 'not-uuid'
    except:
      error = True
    
    self.assertTrue(error, 'uuid validation has failed')
