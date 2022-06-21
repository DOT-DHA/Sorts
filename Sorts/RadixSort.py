from graphics import *
from Display import *
from Sorts.CountingSort import CountingSort

def RadixSort(*args):
    data, display, win = args[0], args[1], args[2]
    
    divisor = 1
    while max(data)/divisor > 1:
        data = CountingSort(data, display, win, 10, divisor)
        divisor *= 10
        
    return data