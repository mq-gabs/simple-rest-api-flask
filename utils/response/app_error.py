class AppError(Exception):
  def __init__(self, status_code: int, message: str, details: any = None):
    super().__init__()
    self.status_code = status_code
    self.message = message
    self.details = details
  
  def toJSON(self) -> dict:
    return {
      "status_code": self.status_code,
      "message": self.message,
      "details": self.details
    }