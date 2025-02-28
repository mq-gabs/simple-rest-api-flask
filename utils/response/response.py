class Response:
  def __init__(self, message: str):
    self.success = True
    self.message = message
  
  def toJSON(self):
    return {
      "success": self.success,
      "message": self.message
    }
