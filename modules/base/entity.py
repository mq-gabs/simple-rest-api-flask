from datetime import datetime
import uuid

class Base:
  def __init__(self):
    self._id = uuid.uuid4().__str__()
    self._created_at: datetime = datetime.now().__str__()
    self._updated_at: datetime = datetime.now().__str__()
    self._deleted_at: datetime = None
    
    self.DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

  def toJSON(self) -> dict:
    return {
      "id": self._id,
      "created_at": self._created_at,
      "updated_at": self._updated_at,
      "deleted_at": self._deleted_at
    }
  
  def _is_valid_uuid(self, id: str) -> bool:
    try:
      uuid.UUID(id)
      return True
    except:
      return False
  
  @property
  def id(self):
    return self._id
  
  @id.setter
  def id(self, id: str):
    if not self._is_valid_uuid(id):
      raise TypeError(f'{id} is not valid UUID')

    self._id = id
  
  @property
  def created_at(self):
    return self._created_at

  @created_at.setter
  def created_at(self, created_at: datetime):
    self._created_at = created_at
  
  @property
  def updated_at(self):
    return self._updated_at

  @updated_at.setter
  def updated_at(self, updated_at: datetime):
    self._updated_at = updated_at
  
  @property
  def deleted_at(self):
    return self._deleted_at
  
  @deleted_at.setter
  def deleted_at(self, deleted_at: datetime):
    self._deleted_at = deleted_at