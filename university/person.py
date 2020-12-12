from university import address
from university import error
class person:
  def __init__(self, firstName, lastName, dateOfBirth, phone, user_address):
    self.firstName = firstName
    self.lastName = lastName
    self.dateOfBirth = dateOfBirth
    self.phone = phone
    self.addresses = []
    if isinstance(user_address, address):
      self.addresses.append(user_address)
    elif isinstance(user_address, list):
      for entry in user_address:
        if not isinstance(entry, address):
          error.error("invalid address.")
      self.addresses = user_address
    else:
      error.error("invalid address.")

  def addAddress(self, user_address):
    if not isinstance(user_address, address):
      error.error("invalid address.")
    self.addresses.append(user_address)


