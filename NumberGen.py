import random as R
import math as M
from graphics import *
from Display import *

def generateData(win, N=10, B=10, random = False):
    
    winHeight = win.getHeight()
    winWidth = win.getWidth()
    
    data = [0] * N
    display = [Point(0,0)] * N

    if len(data) > 0:
        if random:
            for i in range(N):
                data[i] = R.randint(0, B)
        else:
            for i in range(N):
                data[i] = int(B * i / N)
    R.shuffle(data)
    
    for i in range(N):
        point = Circle(Point(winWidth * (( i +.5 ) / N ), winHeight * data[i] / max(data) ), 3)
        display[i] = point
    
    fun = display[:]

    high = highlight(win, None, "Create", None, None)

    while len(fun) > 0:
        choice = R.choice(fun)
        choice.draw(win)
        fun.remove(choice)
        highlight(win, choice, "Move", "Red", high)
        Flash(choice,"Red")

    highlight(win, None, "Delete", None, high)

    return data, display