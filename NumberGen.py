import random as R
from graphics import *
from Display import *

#Functions for generating data
def generateData(N, Range, random):

    #initializing data list
    data = [0] * N

    if len(data) > 0:

        #generating random data
        if random:
            for i in range(N):
                data[i] = int(R.triangular(1, Range - 1))

        #generating linear data
        else:
            for i in range(N):
                data[i] = int(Range * i / N)

    #shuffling data to make certain
    R.shuffle(data)

    return data