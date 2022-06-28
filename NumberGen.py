import random as R
from graphics import *
from Display import *

def generateData(N = 10, Range = 10, random = False):

    data = [0] * N

    if len(data) > 0:
        if random:
            for i in range(N):
                data[i] = R.randint(1, Range - 1)
        else:
            for i in range(N):
                data[i] = int(Range * i / N)
    R.shuffle(data)

    return data