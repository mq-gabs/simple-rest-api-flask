class AppError:
  def __init__(self, code: int, message: str, details: any = None):
    self.statusCode = code
    self.message = message
    self.details = details
  
  def toJSON(self) -> dict:
    return {
      "statusCode": self.code,
      "message": self.message,
      "details": self.details
    }