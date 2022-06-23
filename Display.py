from graphics import *
import random as R
import time

def start(title, WINWIDTH, WINHEIGHT):
    win = GraphWin(title, WINWIDTH, WINHEIGHT)
    win.setCoords(0, 0, WINWIDTH, WINHEIGHT)
    return win

def updateShape(point, newY, SMAX, win):

    point.undraw()
    pointX = point.getCenter().getX()
    newPoint = Circle(Point(pointX, win.getHeight() * newY/SMAX), 3)
    newPoint.draw(win)
    Flash(newPoint)

    return newPoint

def highlight(win, target, mode, color, highlighter):
    if target == None:
        target = Circle(Point(0,0),3)
    if mode == None:
        mode = "Create"
    if color == None:
        color = "Red"
    if highlighter == None:
        highlighter = Rectangle(Point(0,0),Point(0,0))

    if mode == "Create":
        hX = target.getCenter().getX() - target.getRadius()
        hY = win.getHeight()
        highlighter = Rectangle(Point(hX, 0),Point(hX + target.getRadius() * 2, hY))
        highlighter.setOutline(color)
        highlighter.setFill(color)
        highlighter.draw(win)

    elif mode == "Move":
        tX = target.getCenter().getX() - target.getRadius()
        hX = highlighter.getP1().getX()
        highlighter.move(tX - hX, 0)
        
    elif mode == "Change":
        highlighter.setOutline(color)
        highlighter.setFill(color)

    elif mode == "Delete":
        highlighter.undraw()

    return highlighter

def Flash(objects, color = "Red"):
    if type(objects) == type([]):
        for i in objects:
            i.setFill(color)
            i.setOutline(color)
    else:
        objects.setFill(color)
        objects.setOutline(color)

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


def finish(point):
    point.setFill("Forest Green")
    point.setOutline("Forest Green")