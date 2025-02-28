from enum import Enum

class EProductStatus(Enum):
  AVAILABLE = 1
  UNAVAILABLE = 2

  def list():
    return ['AVAILABLE', 'UNAVAILABLE']