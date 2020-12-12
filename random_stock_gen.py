alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","K","R","S","T","U","V","W","X","Y","Z"]
stocks = []
import random
for i in range(200):
    size = random.randint(2,5)
    string = ""
    for a in range(size):
        letter = random.choice(alphabet)
        string = string + letter
    stocks.append(string)
print(stocks)

"""
a fast project to create 200 random stock-like quotes between 2-5 digits.
"""
