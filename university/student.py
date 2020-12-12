from university import person
from university import enrol
from university import error
class student(person):
  def __init__(self, firstName, lastName, dateOfBirth, phone, user_address, international=False):
    super().__init__(self, firstName, lastName, dateOfBirth, phone, user_address)
    self.international = international
    self.enroled = []

  def addEnrolment(self, user_enrol):
    if not isinstance(user_enrol, enrol):
      error.error("invalid enrol.")
    self.enroled.append(user_enrol)

  def isOnProbation(self):
    return

  def isPartTime(self):
    return  len(self.enroled) <= 3