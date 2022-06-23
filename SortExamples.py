from Display import *
from graphics import *
from NumberGen import generateData
from Sorts.CocktailSort import CocktailSort
from Sorts.ShellSort import ShellSort
from Sorts.MergeSort import MergeSort
from Sorts.CountingSort import CountingSort
from Sorts.RadixSort import RadixSort
from Sorts.HeapSort import HeapSort

if __name__ == "__main__":
    WINHEIGHT = 9 * 90
    WINWIDTH = 9 * 160
    amountOfNumbers = 100
    numberRange = amountOfNumbers * 5
    random = False
    done = False

    win = start("Sorting Examples", WINWIDTH, WINHEIGHT)
    win.setBackground("Black")

    while not done:

        data, display = generateData(win, amountOfNumbers, numberRange, random)

        menu = []
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4*3), "Cocktail"))
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4), "Shell"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4*3), "Merge"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4), "Heap"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4*3), "Counting"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4), "Radix"))

        functions = []
        functions.append(CocktailSort)
        functions.append(ShellSort)
        functions.append(MergeSort)
        functions.append(HeapSort)
        functions.append(CountingSort)
        functions.append(RadixSort)

        boxes = []
        for i in menu:
            boxes.append(boxify(i))

        for i in boxes:
            Flash(i, "White")
            i.setOutline("White")
            i.draw(win)

        for i in menu:
            Flash(i, "White")
            i.setOutline("White")
            i.draw(win)


        chosen = False
        while not chosen:

            mouse = win.getMouse()

            mousex = mouse.getX()
            mousey = mouse.getY()

            for i in range(len(boxes)):
                if mousex >= boxes[i].getP1().getX() and mousex <= boxes[i].getP2().getX() and mousey >= boxes[i].getP1().getY() and mousey <= boxes[i].getP2().getY():
                    for j in boxes:
                        j.undraw()

                    for k in menu:
                        k.undraw()

                    functions[i](data, display, win, numberRange)
                    chosen = True


        close = Text(Point(WINWIDTH/4*3, WINHEIGHT/2), "Exit")
        again = Text(Point(WINWIDTH/4, WINHEIGHT/2), "Again?")

        closeBox = boxify(close)
        redoBox = boxify(again)

        Flash([closeBox, redoBox]),
        closeBox.setOutline("White")
        redoBox.setOutline("White")

        close.setFill("White")
        again.setFill("White")

        closeBox.draw(win)
        redoBox.draw(win)
        close.draw(win)
        again.draw(win)

        mouse = win.getMouse()

        if mouse.getX() < WINWIDTH/2:
            done = False
        else:
            done = True

        closeBox.undraw()
        close.undraw()
        redoBox.undraw()
        again.undraw()
        reset(display)