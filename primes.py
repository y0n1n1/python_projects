"""
prime number generator, checks primes until LEN variable size, and adds the primes to list x.
........
Complexity: O(no idea)
........
Cool: yes
........
"""

LEN = 10000

x = [2]
for i in range(LEN):
    y = i
    if y == 1:
        pass
    elif (y % 2) == 0:
        pass
    else:
        iss = True
        for a in x:
            if (y % a) == 0:
                iss = False
            else:
                pass
        if iss:
            x.append(y)
        else:
            pass
print(x)

#prime gen!
