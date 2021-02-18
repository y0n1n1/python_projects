import time
import random
from os import system
from threading import Thread

boggle = [[],[],[],[],[],[],[]]
probability_distribution = ['e','e','e','e','e','e','e','e','e','e','e','t','t','t','t','t','t','t','t','t','o','o','o','o','o','o','o','s','s','s','s','s','s','a','a','a','a','a','a','i','i','i','i','i','i','n','n','n','n','n','n','r','r','r','r','r','h','h','h','h','h','l','l','l','l','w','w','w','u','u','u','d','d','d','y','y','y','b','b','c','c','f','f','g','g','m','m','p','p','v','v','j','k','q','x','z']

def setb(b):
  for i in b:
    for a in range(7):
      i.append(random.choice(probability_distribution))

def display(b):
  for i in b:
    s = "|"
    for a in i:
      s = s+" "
      s = s+a
      s = s+" "
    s = s + "|"
    print(s)

def clb():
  b = [[],[],[],[],[],[],[]]
  return b

over = False

def timer():
  for i in range(60):
    time.sleep(1)
  print(oevr)
  over = True

def corpus(b):
  words = []
  t = True
  while t:
    x = input("word")
    words.append(x)
    system("cls")
    display(b)
    if over:
      t = False

def main(b):
  for i in range(10):
    setb(b)
    display(b)
    time.sleep(0.4)
    system("cls")
    b = clb()
  setb(b)
  display(b)
  t1 = Thread(target=timer)
  t2 = Thread(target=corpus(b))
  t1.start()
  t2.start()
  system("cls")
  print("over")
  time.sleep(1.7)
  print("words:")
  for i in words:
    print(i)


main(boggle)
