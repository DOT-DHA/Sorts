from Display import *
from graphics import *
from NumberGen import generateData
from Sorts.BubbleSort import BubbleSort
from Sorts.ShellSort import ShellSort
from Sorts.MergeSort import MergeSort
from Sorts.CountingSort import CountingSort
from Sorts.RadixSort import RadixSort
from Sorts.HeapSort import HeapSort

if __name__ == "__main__":
    WINHEIGHT = 9 * 90
    WINWIDTH = 9 * 160
    amountOfNumbers = 5000
    numberRange = 10
    random = False
    done = False

    win = start("Sorting Examples", WINWIDTH, WINHEIGHT)
    win.setBackground("black")

    while not done:
        data, display = generateData(win, amountOfNumbers, numberRange, random)

        menu = []
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4*3), "Bubble sort"))
        menu.append(Text(Point(WINWIDTH/6, WINHEIGHT/4), "Shell sort"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4*3), "Merge sort"))
        menu.append(Text(Point(WINWIDTH/6*3, WINHEIGHT/4), "Heap sort"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4*3), "Counting sort"))
        menu.append(Text(Point(WINWIDTH/6*5, WINHEIGHT/4), "Radix sort"))

        functions = []
        functions.append(BubbleSort)
        functions.append(ShellSort)
        functions.append(MergeSort)
        functions.append(HeapSort)
        functions.append(CountingSort)
        functions.append(RadixSort)

        boxes = []
        for i in menu:
            boxes.append(boxify(i))

        for i in boxes:
            flash(i, "white")
            i.setOutline("white")
            i.draw(win)

        for i in menu:
            flash(i, "white")
            i.setOutline("white")
            i.draw(win)

        mouse = win.getMouse()

        mousex = mouse.getX()
        mousey = mouse.getY()
        chosen = False

        while not chosen:
            for i in range(len(boxes)):
                if mousex >= boxes[i].getP1().getX() and mousex <= boxes[i].getP2().getX() and mousey >= boxes[i].getP1().getY() and mousey <= boxes[i].getP2().getY():
                    for j in boxes:
                        j.undraw()

                    for k in menu:
                        k.undraw()

                    functions[i](data, display, win, numberRange)
                    chosen = True


        close = Text(Point(WINWIDTH/4*3, WINHEIGHT/2), "close")
        redo = Text(Point(WINWIDTH/4, WINHEIGHT/2), "redo")

        closeBox = boxify(close)
        redoBox = boxify(redo)

        flash([closeBox, redoBox]),
        closeBox.setOutline("white")
        redoBox.setOutline("white")

        close.setFill("white")
        redo.setFill("white")

        closeBox.draw(win)
        redoBox.draw(win)
        close.draw(win)
        redo.draw(win)

        mouse = win.getMouse()

        if mouse.getX() < WINWIDTH/2:
            done = False
        else:
            done = True

        closeBox.undraw()
        close.undraw()
        redoBox.undraw()
        redo.undraw()
        reset(display)