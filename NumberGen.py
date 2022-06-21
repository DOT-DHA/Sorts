from graphics import *
import random as R
from Display import flash

def generateData(win, N=10, B=10, random = False):
    
    WINHEIGHT = win.getHeight()
    WINWIDTH = win.getWidth()
    
    data = [0] * N
    display = [Rectangle(Point(0,0), Point(0,0))] * N

    if len(data) > 0:
        if random:
            for i in range(N):
                data[i] = R.randrange(B)
        else:
            for i in range(N):
                data[i] = int(B * i / N)
    R.shuffle(data)

    for i in range(N):
        dataPoint = data[i]

        rect = Rectangle(
            Point(
                WINWIDTH*(i/N),
                0
            ),
            Point(
                WINWIDTH*((i+1)/N),
                WINHEIGHT*(dataPoint/max(data))
            )
        )
        display[i].undraw()
        display[i] = rect
        rect.draw(win)
        
        flash(display[i], "Red")

    return data, display