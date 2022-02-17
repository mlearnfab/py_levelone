import random
from collections import Counter


def tosses(n):
    rolls = []
    for i in range(n):
        roll = random.randint(1,6)
        rolls.append(roll)
    return rolls


tosslist = tosses(10)
print(tosslist)
print(Counter(tosslist))     


