from university import course
from university import student
from university import error
from datetime import datetime
class enrol:
  def __init__(self, user_student, user_course):
    if not isinstance(user_student, student):
      error.error("invalid student")
    if not isinstance(user_course, course):
      error.error("invalid course")

    self.student = user_student
    self.course = user_course
    self.grade = None
    self.date = datetime.now()

  def setGrade(self, grade):
    self.grade = grade

  