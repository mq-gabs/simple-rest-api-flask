class ListResponse:
  def __init__(self, _list, total: int):
    self.list = _list
    self.total = total

  def toJSON(self):
    return {
      "total": self.count,
      "list": [item.toJSON() for item in self.list]
    }