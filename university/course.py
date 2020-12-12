from university import professor
from university import error
from university import enrol 

class course:
  def __init__(self, name, code, max_, min_, user_professor):
    self.name = name
    self.code = code
    self.max = max_
    self.min = min_
    self.professors = []
    self.enrolments = []

    if isinstance(user_professor, professor):
      self.professors.append(user_professor)
    elif isinstance(user_professor, list):
      for entry in user_professor:
        if not isinstance(entry, professor):
          error.error("invalid professor.")
      self.professors = user_professor
    else:
      error.error("invalid address.")

  def addProfessor(self, user_professor):
    if not isinstance(user_professor, professor):
      error.error("invalid professor.")
    self.professors.append(user_professor)

  def addEnrolment(self, user_enrol):
    if not isinstance(user_enrol, enrol):
      error.error("invalid enrolment.")
    
    if len(enrolments) == self.max:
      error.error("course is full.")
    self.enrolments.append(user_enrol)

  def isCancelled(self):
    return len(self.enrolments) < self.min
