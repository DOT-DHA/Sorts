from Display import *
from graphics import *


def CocktailSort(*args):
    data, display, win = args[0], args[1], args[2]

    done = False

    start = 0
    end = len(data) - 1

    while not done:

        done = True
        for i in range(start, end):
            
            if data[i] > data[i+1]:
                display[i] = updateShape(display[i], data[i+1], max(data), win)
                display[i+1] = updateShape(display[i+1], data[i], max(data), win)

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                done = False
            
        if done:
            break
        
        end -= 1 
        
        for i in range(end-1, start-1, -1):

            if data[i] > data[i+1]:
                display[i] = updateShape(display[i], data[i+1], max(data), win)
                display[i+1] = updateShape(display[i+1], data[i], max(data), win)

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                done = False

        start += 1

    for i in display:
        finish(i)
        
    return data