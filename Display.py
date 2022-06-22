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
    highlightFlash(win, newPoint, "Blue")

    return newPoint

def highlightFlash(win, objects, color = "Red"):
    flashStorage = []
    if type(objects) == type([]):
        GenFlash(objects)
        for i in objects:
            p1x = i.getCenter().getX() - i.getRadius()
            p2x = i.getCenter().getX() + i.getRadius()
            py = win.getHeight()
            flashStorage.append(Rectangle(Point(p1x,0),Point(p2x,py)))
        for i in flashStorage:
            i.setFill(color)
            i.setOutline(color)
            i.draw(win)
    else:
        GenFlash(objects)
        p1x = objects.getCenter().getX() - objects.getRadius()
        p2x = objects.getCenter().getX() + objects.getRadius()
        py = win.getHeight()

        rect = Rectangle(Point(p1x,0),Point(p2x,py))
        rect.setFill(color)
        rect.setOutline(color)
        rect.draw(win)

    #time.sleep(.01)
        
    if type(objects) == type([]):
        while flashStorage:
            current = flashStorage.pop(0)
            current.undraw()

            
    else:
        rect.undraw()

def GenFlash(objects, color = "Red"):
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