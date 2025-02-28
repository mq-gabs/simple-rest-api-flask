from utils.enums.status import EProductStatus
from modules.base.entity import Base
from utils.response.app_error import AppError

class Product(Base):
  def __init__(self):
    super().__init__()
    self._name: str = ''
    self._description: str = ''
    self._price: int = 0 
    self._status: EProductStatus = EProductStatus.AVAILABLE

    self.MAX_NAME_LENGTH = 64
    self.MAX_DESCRIPTION_LENGTH = 1500

  def toJSON(self) -> dict:
    mydict = super().toJSON()
    task = {
      "name": self._name,
      "description": self._description,
      "price": self._price,
      "status": self._status.name
    }

    mydict.update(task)
    return mydict

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name: str):
    if not name:
      raise AppError(400, "'name' cannot be None")
    if len(name) > self.MAX_NAME_LENGTH:
      raise AppError(400, f"'name' length cannot be greater than {self.MAX_NAME_LENGTH}")
    
    self._name = name

  @property
  def description(self):
    return self._description
  
  @description.setter
  def description(self, description: str):
    if not description:
      raise AppError(400, "'description' cannot be None")
    if len(description) > self.MAX_DESCRIPTION_LENGTH:
      raise AppError(400, f"'description' length cannot be greater than {self.MAX_DESCRIPTION_LENGTH}")
    
    self._description = description

  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, price: int):
    if not price:
      raise AppError(400, "'price' cannot be None")
    if price < 0:
      raise AppError(400, "'price' must be greater than or equal to zero")

    self._price = price

  @property
  def status(self):
    return self._status
  
  @status.setter
  def status(self, status: str | EProductStatus):
    if not status:
      raise AppError(400, "'status' cannot be None")
    if type(status) == str:
      if status not in EProductStatus.list():
        raise AppError(400, f"'status' must be in {EProductStatus.list()}, got {status}")

      self._status = EProductStatus[status]
      return
    
    self._status = status

