import random as R
from graphics import *
from Display import flash

def generateData(win, N=10, B=10, random = False):
    
    WINHEIGHT = win.getHeight()
    WINWIDTH = win.getWidth()
    
    data = [0] * N
    display = [Rectangle(Point(0,0), Point(0,0))] * N

    if len(data) > 0:
        if random:
            for i in range(N):
                data[i] = int(R.triangular(0, B, B/10))
        else:
            for i in range(N):
                data[i] = int(B * i / N)
    R.shuffle(data)
    
    for i in range(N):
        rect = Rectangle(
            Point(
                WINWIDTH*(i/N),
                0
            ),
            Point(
                WINWIDTH*((i+1)/N),
                WINHEIGHT*(data[i]/max(data))
            )
        )
        display[i] = rect
    
    fun = display[:]

    while len(fun) > 0:
        choice = R.choice(fun)
        choice.draw(win)
        fun.remove(choice)
        flash(choice,"red")

    return data, display