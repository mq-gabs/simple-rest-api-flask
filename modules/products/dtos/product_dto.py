from utils.enums.status import EProductStatus

class ProductDto:
  name: str = None
  description: str = None
  price: int = None
  status: EProductStatus = None