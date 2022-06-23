from Display import *
from graphics import *

def InsertionSort(*args):
    data, display, win = args[0], args[1], args[2]

    
    high1 = highlight(win, target = display[0], mode = "Create", color = "Blue")
    high2 = highlight(win, target = display[1], mode = "Create", color = "Green")


    for i in range(1, len(data)):
        inPlace = False
        pos = i
        highlight(win, display[i], "Move", highlighter = high1)
        while not inPlace:
            if pos == 0:
                break

            inPlace = True
            if data[pos] < data[pos-1]:
                temp = data[pos]
                data[pos] = data[pos-1]
                data[pos-1] = temp


                display[pos] = updateShape(display[pos], data[pos], max(data), win)
                display[pos-1] = updateShape(display[pos-1], data[pos-1], max(data), win)

                highlight(win, display[pos-1], "Move", highlighter = high2)
                inPlace = False
                pos -= 1

            finish([display[pos+1],display[pos]])

    highlight(win, mode = "Delete", highlighter = high1)
    highlight(win, mode = "Delete", highlighter = high2)

    return data