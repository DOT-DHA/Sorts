from graphics import *
import random as R
import time

def start(title, WINWIDTH, WINHEIGHT):
    win = GraphWin(title, WINWIDTH, WINHEIGHT)
    win.setCoords(0, 0, WINWIDTH, WINHEIGHT)
    return win

def updateBar(rect, newY, lMax, win):

    rect.undraw()
    point1 = rect.getP1()
    point2x = rect.getP2().getX()
    newRect = Rectangle(point1, Point(point2x, win.getHeight() * (newY/lMax)))
    newRect.draw(win)

    return newRect

def flash(objects, color = "Red"):
    if type(objects) == type([]):
        for i in objects:
            i.setFill(color)
            i.setOutline(color)
    else:
        objects.setFill(color)
        objects.setOutline(color)

    #time.sleep(.1)

    if type(objects) == type([]):
        for i in objects:
            i.setFill("Slate Gray")
            i.setOutline("Slate Gray")
    else:
        objects.setFill("Slate Gray")
        objects.setOutline("Slate Gray")

def boxify(object):
    return Rectangle(
                        Point(
                            object.getAnchor().getX()-50,
                            object.getAnchor().getY()-18),
                        Point(
                            object.getAnchor().getX()+50,
                            object.getAnchor().getY()+18)
                    )

def reset(display):
    while len(display) > 0:
        choice = R.choice(display)
        choice.undraw()
        display.remove(choice)


def finish(rect):
    rect.setFill("Forest Green")
    rect.setOutline("Forest Green")