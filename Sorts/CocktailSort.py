from Display import *
from graphics import *


def CocktailSort(*args):
    data, display, win = args[0], args[1], args[2]

    high1 = highlight(win, target = display[0], mode = "Create", color = "Blue")
    high2 = highlight(win, target = display[1], mode = "Create", color = "Blue")

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
                highlight(win, display[i], "Move", highlighter = high1)

                display[i+ 1] = updateShape(display[i+1], data[i+1], max(data), win)
                highlight(win, display[i+1], "Move", highlighter = high2)

                done = False
            
        if done:
            break
        
        end -= 1 
        
        for i in range(end-1, start-1, -1):

            if data[i] > data[i+1]:

                datatemp = data[i]
                data[i] = data[i+1]
                data[i+1] = datatemp

                display[i] = updateShape(display[i], data[i], max(data), win)
                highlight(win, display[i], "Move", highlighter = high1)

                display[i+ 1] = updateShape(display[i+1], data[i+1], max(data), win)
                highlight(win, display[i+1], "Move", highlighter = high2)

                done = False

        start += 1

    highlight(win, mode = "Delete", highlighter = high2)

    highlight(win, mode = "Change", color = "Green", highlighter = high1)

    for i in display:
        highlight(win, i, "Move", "Green", high1)
        finish(i)

    highlight(win, mode = "Delete", highlighter = high1)