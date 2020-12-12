from university import person
from university import course
from university import error
class professor:
  def __init__(self, firstName, lastName, dateOfBirth, phone, user_address, salary):
    super().__init__(self, firstName, lastName, dateOfBirth, phone, user_address)
    self.salary = salary
    self.courses = []
    self.gotRaise = False

  def checkForRaise(self):
    if len(self.courses) >= 4 and not self.gotRaise:
      self.salary += 20000
      self.gotRaise = True
  
  def addCourse(self, user_course):
    if not isinstance(user_course, course):
      error.error("invalid course.")
    self.courses.append(user_course)