from Display import *
from graphics import *
import time


def CocktailSort(*args):
    data, display, win = args[0], args[1], args[2]

    high1 = highlight(win, None, "Create", "Blue", None)
    high2 = highlight(win, None, "Create", "Blue", None)

    done = False

    start = 0
    end = len(data) - 1

    while not done:

        done = True
        for i in range(start, end):
            
            if data[i] > data[i+1]:

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                display[i] = updateShape(display[i], data[i], max(data), win)
                highlight(win, display[i], "Move", None, high1)

                display[i+1] = updateShape(display[i+1], data[i+1], max(data), win)
                highlight(win, display[i+1], "Move", None, high2)

                done = False
                time.sleep(.05)
            
        if done:
            break
        
        end -= 1 
        
        for i in range(end-1, start-1, -1):

            if data[i] > data[i+1]:

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                display[i] = updateShape(display[i], data[i], max(data), win)
                highlight(win, display[i], "Move", None, high1)

                display[i+1] = updateShape(display[i+1], data[i+1], max(data), win)
                highlight(win, display[i+1], "Move", None, high2)

                done = False
                time.sleep(.05)

        start += 1

    highlight(win, None, "Change", "Green", high1)

    highlight(win, None, "Delete", None, high2)

    for i in display:
        highlight(win, i, "Move", "Green", high1)
        finish(i)
        time.sleep(.05)

    highlight(win, None, "Delete", None, high1)

    return data