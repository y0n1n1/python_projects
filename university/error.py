class error:
  def __init__(self, error):
    self.error = error

  def error(self):
    Exception(str(self.error))