import math
import os
import time
 
class calculator:
  def sum(i, I):
    return i + I
  def sub(i, I):
    return i - I
  def mul(i, I):
    return i * I
  def div(i, I):
    return i / I
  def per(i, I):
    return (i / I) * 100
  def pow(i, I):
    return i**I
  def sin(i):
    return math.sin(i)
  def cos(i):
    return math.cos(i)
  def tan(i):
    return math.tan(i)
 
class screen:
  def __init__(self):
    self.s = []
 
  def prepare(self):
    self.s = ["enter: command(input1, input2)",
      "command:input->output", 
      "sum: i+I -> E", 
      "sub: i-I -> E",
      "mul: i*I -> E",
      "div: i/I -> E",
      "per: i*100/I -> E",
      "pow: i^I -> E",
      "sin: i -> E",
      "cos: i -> E",
      "tan: i -> E", 
      "quit:QQQ"]
 
  def comp(self, command, value1, value2):
    os.system("cls")
    if command == "QQQ":
      self.Q = False
    elif command == "sin":
      result = calculator.sin(int(value1))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "cos":
      result = calculator.cos(int(value1))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "tan":
      result = calculator.tan(int(value1))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "sum":
      result = calculator.sum(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "sub":
      result = calculator.sub(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "mul":
      result = calculator.mul(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "div":
      result = calculator.div(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "per":
      result = calculator.per(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    elif command == "pow":
      result = calculator.pow(int(value1), int(value2))
      self.s = ["\/ result \/", str(result), "quit: QQQ"]
    else:
      print("wrong commands/inputs")
    screen.display(self)
    time.sleep(5)
    os.system("cls")
    screen.prepare(self)
 
 
    
 
  def display(self):
    self.Q = True
    while self.Q:
      os.system("cls")
      print("____________________________________________________")
      for i in self.s:
        e = ""
        e += "| "
        e += i
        q = 50 -len(i)
        for i in range(q):
          e += " "
        e += " |"
        print(e)
        
      print("____________________________________________________")
      print("**press enter if a value is supposed to be empty**")
      screen.prepare(self)
      command = input("command:")
      value1 = input("value 1:")
      value2 = input("value 2:")
      screen.comp(self, command, value1, value2)
 
x = screen()
x.prepare()
x.display()
 
 
 
 
