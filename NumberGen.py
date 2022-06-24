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
                data[i] = R.randrange(0, B)
        else:
            for i in range(N):
                data[i] = int(B * i / N)
    R.shuffle(data)
    
    for i in range(N):
        point = Circle(Point(winWidth * (( i +.5 ) / N ), winHeight * data[i] / max(data) ), 7)
        display[i] = point
    
    fun = display[:]


    while len(fun) > 0:
        choice = R.choice(fun)
        choice.draw(win)
        fun.remove(choice)
        Flash(choice,"Red")


    return data, display