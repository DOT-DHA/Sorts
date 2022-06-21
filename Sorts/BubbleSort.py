from Display import *
from graphics import *


def BubbleSort(*args):
    data, display, win = args[0], args[1], args[2]
    
    done = False
    while not done:
        done = True

        for i in range(len(data)-1):
            
            if data[i] > data[i+1]:
                display[i] = updateBar(display[i], data[i+1], max(data), win)
                display[i+1] = updateBar(display[i+1], data[i], max(data), win)
                flash([display[i], display[i+1]], "blue")

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                done = False