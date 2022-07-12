import math as M
from graphics import *
from Display import *
from Sorts.CountingSort import CountingSort

#radix sort does a counting sort one digit at a time.
def RadixSort(data, D):
    
    #setting base, and max digit position
    base = 10
    dMax = M.floor(M.log(max(data), base)) + 1

    for i in range(dMax):
        #counting sort each digit in order
        data = CountingSort(data, D, base, divisor = M.floor(M.pow(base, i)))
    return data