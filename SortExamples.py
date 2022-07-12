from Display import *
from graphics import *
from NumberGen import generateData
from Sorts.CocktailSort import CocktailSort
from Sorts.ShellSort import ShellSort
from Sorts.MergeSort import MergeSort
from Sorts.CountingSort import CountingSort
from Sorts.RadixSort import RadixSort
from Sorts.HeapSort import HeapSort
#(Just about) every sort from the files 

#main driving code
if __name__ == "__main__":

    #starting variables
    WINHEIGHT = 9 * 90
    WINWIDTH = 9 * 160
    amountOfNumbers = 1024
    numberRange = amountOfNumbers * 2
    random = True
    done = False

    #setting up my display class and window object
    D = dis("Sorting Examples", WINWIDTH, WINHEIGHT)
    win = D.win
    win.setBackground("Black")

    #main user loop
    while not done:

        #creating all data
        data = generateData(amountOfNumbers, numberRange, random)
        D.setDisplay(data)

        #Creating my menu selections
        menu = []
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4*3), "Cocktail"))
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4), "Shell"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4*3), "Merge"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4), "Heap"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4*3), "Counting"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4), "Radix"))

        #Putting boxes around my menu items
        boxes = []
        for i in menu:
            boxes.append(D.boxify(i))

        #Making sorts into a list
        functions = []
        functions.append(CocktailSort)
        functions.append(ShellSort)
        functions.append(MergeSort)
        functions.append(HeapSort)
        functions.append(CountingSort)
        functions.append(RadixSort)
        
        #Coloring menu boxes
        for i in boxes:
            D.setColor(i)
            i.setOutline("White")
            i.draw(win)

        #Coloring Menu Text
        for i in menu:
            D.setColor(i)
            i.setOutline("White")
            i.draw(win)

        #waiting for user to select sort
        chosen = False
        while not chosen:

            mouse = win.getMouse()
            mousex = mouse.getX()
            mousey = mouse.getY()

            #checking if click is in a box
            for i in range(len(boxes)):
                if mousex >= boxes[i].getP1().getX() and mousex <= boxes[i].getP2().getX() and mousey >= boxes[i].getP1().getY() and mousey <= boxes[i].getP2().getY():
                    
                    for j in boxes:
                        j.undraw()
                    for k in menu:
                        k.undraw()

                    if i == 4:
                        data = CountingSort(data, D, base = numberRange)
                    else:
                        data = functions[i](data, D)

                    chosen = True

        #creating boxes for restarting or closing
        close = Text(Point(WINWIDTH/4*3, WINHEIGHT/2), "Exit")
        again = Text(Point(WINWIDTH/4, WINHEIGHT/2), "Again?")

        closeBox = D.boxify(close)
        againBox = D.boxify(again)

        D.setColor([closeBox, againBox]),
        closeBox.setOutline("White")
        againBox.setOutline("White")

        close.setFill("White")
        again.setFill("White")

        closeBox.draw(win)
        againBox.draw(win)
        close.draw(win)
        again.draw(win)

        #waiting for user to select box
        chosen = False
        while not chosen:

            mouse = win.getMouse()
            mousex = mouse.getX()
            mousey = mouse.getY()
            if mousex >= againBox.getP1().getX() and mousex <= againBox.getP2().getX() and mousey >= againBox.getP1().getY() and mousey <= againBox.getP2().getY():
                done = False
                chosen = True
            elif mousex >= closeBox.getP1().getX() and mousex <= closeBox.getP2().getX() and mousey >= closeBox.getP1().getY() and mousey <= closeBox.getP2().getY():
                done = True
                chosen = True

        #removing box objects
        closeBox.undraw()
        close.undraw()
        againBox.undraw()
        again.undraw()

        #removing all data
        D.reset()