import math as M
from graphics import *
from Display import *
from Sorts.CountingSort import CountingSort

def RadixSort(*args):
    data, display, D = args[0], args[1], args[2]

    base = 2
    dMax = M.floor(M.log(max(data), base))+1

    for i in range(dMax):
        data = CountingSort(data, display, D, base, divisor = M.floor(M.pow(base, i)))
    return data