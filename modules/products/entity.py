from utils.enums.status import EProductStatus
from modules.base.entity import Base

class Product(Base):
  def __init__(self):
    super().__init__()
    self._name: str = None
    self._description: str = None
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
    if len(name) > self.MAX_NAME_LENGTH:
      raise ValueError(f'Name length cannot be greater than {self.MAX_NAME_LENGTH}')
    
    self._name = name

  @property
  def description(self):
    return self._description
  
  @description.setter
  def description(self, description: str):
    if len(description) > self.MAX_DESCRIPTION_LENGTH:
      raise ValueError(f'Description length cannot be greater than {self.MAX_DESCRIPTION_LENGTH}')
    
    self._description = description

  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, price: int):
    if price < 0:
      raise ValueError('Price must be greater than or equal to zero')

    self._price = price

  @property
  def status(self):
    return self._status
  
  @status.setter
  def status(self, status: str):
    if status not in EProductStatus.list():
      raise ValueError(f'Status must be in {EProductStatus.list()}, got {status}')

    self._status = EProductStatus[status]
