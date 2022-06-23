from Display import *
from graphics import *
from Sorts.CocktailSort import CocktailSort


def ShellSort(*args):
    data, display, win = args[0], args[1], args[2]
    done = False
    end = len(data)

    found = False
    cIndex = 0
    gap = ciuraSeq(1)

    high1 = highlight(win, None, "Create", "Blue", None)
    high2 = highlight(win, None, "Create", "Blue", None)

    while not found:
        cIndex += 1
        gap = ciuraSeq(cIndex)
        if gap > end:
            cIndex -= 1
            found = True

    while not done:
        done = True
        gap = int(ciuraSeq(cIndex))

        for i in range(end):
            if gap+i < end:
                if data[i] > data[gap + i]:

                    temp = data[gap + i]
                    data[gap+i] = data[i]
                    data[i] = temp
                    
                    display[i] = updateShape(display[i], data[i], max(data), win)
                    display[gap + i] = updateShape(display[gap + i], data[gap + i], max(data), win)

                    highlight(win, display[i], "Move", None, high1)
                    highlight(win, display[gap + i], "Move", "Blue", high2)

                    done = False
        cIndex -=1
        if cIndex == 1:
            highlight(win, None, "Delete", None, high1)
            highlight(win, None, "Delete", None, high2)
            CocktailSort(data, display, win)
            done = True

    return data

def ciuraSeq(num):
    if num < 1:
        return 1
    return 2.25 * ciuraSeq(num-1)