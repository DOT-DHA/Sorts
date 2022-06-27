from graphics import *

class dis:
    win = None
    winWidth = None
    winHeight = None

    dSize = None
    dMax = None

    display = None
    highlight1 = None
    highlight2 = None

    def __init__(self, title, winWidth, winHeight):
        self.win = GraphWin(title, winWidth, winHeight)
        self.win.setCoords(0, 0, winWidth, winHeight)
        self.winWidth = winWidth
        self.winHeight = winHeight

    def setDisplay(self, data):
        self.dSize = len(data)
        self.dMax = max(data)
        self.display = [Point(0,0)] * self.dSize
    
        for i in range(self.dSize):
            bar = Rectangle(
                    Point(
                        self.winWidth * i / self.dSize , 
                        0
                    ), 
                    Point(
                        self.winWidth * (i+1) / self.dSize,
                        self.winHeight * data[i] / self.dMax)
                        )
            self.display[i] = bar
            self.display[i].draw(self.win)
            self.setColor(i)
        

    def updateShape(self, newData, index):

        oldX1 = self.display[index].getP1().getX()
        oldX2 = self.display[index].getP2().getX()

        bar = Rectangle(Point(oldX1, 0), Point(oldX2, self.winHeight * newData / self.dMax))

        self.setColor(bar)
        self.display[index].undraw()
        self.display[index] = bar
        self.display[index].draw(self.win)

    def setColor(self, index, color = "Slate Gray"):
        if type(index) == type(0):
            if type(index) == type([]):
                for i in index:
                    self.display[i].setFill(color)
                    self.display[i].setOutline(color)
            else:
                self.display[index].setFill(color)
                self.display[index].setOutline(color)

        else:
            if type(index) == type([]):
                for i in index:
                    i.setFill(color)
                    i.setOutline(color)
            else:
                index.setFill(color)
                index.setOutline(color)

    def boxify(self, object):
        return Rectangle(
                            Point(
                                object.getAnchor().getX()-50,
                                object.getAnchor().getY()-18),
                            Point(
                                object.getAnchor().getX()+50,
                                object.getAnchor().getY()+18)
                        )


    def finish(self, index):
        self.display[index].setFill("Forest Green")
        self.display[index].setOutline("Forest Green")
    
    def reset(self):
        for i in self.display:
            i.undraw()