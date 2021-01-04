"""
recursive programs !
"""

# FACTORIAL
def factorial(value):
  if value == 0:
    return 1
  elif value < 0:
    fact = abs(value)*factorial(abs(value - 1))
    return fact
  else:
    return value * factorial(value - 1)

# TEST
print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120


# FIBONACCI
def fibonacci(value):
  if value <= 1:
    return 1
  else:
    return fibonacci(value - 1) + fibonacci(value - 2)

print(fibonacci(1)) # 1
print(fibonacci(2)) # 2
print(fibonacci(3)) # 3
print(fibonacci(4)) # 5
print(fibonacci(5)) # 8
