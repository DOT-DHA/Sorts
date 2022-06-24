from Display import *
from graphics import *
from Sorts.InsertionSort import InsertionSort

def MergeSort(*args):
    data, display, win = args[0], args[1], args[2]

    mainDriver(data, display, win, max(data))

    finish(display)

def mainDriver(*args):
    data, display, win, SMAX = args[0], args[1], args[2], args[3]

    if len(data) <= 1:
        return
    elif len(data) > 4 and len(data) < 15:
        InsertionSort(data, display, win)
    else:

        # Finding the mid of the array
        mid = len(data)//2

        # Dividing the array elements
        L = data[:mid]
        disL = display[:mid]

        # into 2 halves
        R = data[mid:]
        disR = display[mid:]


        # Sorting the first half
        mainDriver(L, disL, win, SMAX)
        # Sorting the second half
        mainDriver(R, disR, win, SMAX)

        highL = highlight(win, target = disL[0], mode = "Create", color = "Blue")
        highR = highlight(win, target = disR[0], mode = "Create", color = "Blue")

        index = 0

        while len(L) and len(R):
            if L[0] < R[0]:
                disL[0].undraw()
                data[index] = L[0]
                highlight(win, display[index], "Move", highlighter = highL)
            
                display[index] = updateShape(display[index], data[index], SMAX, win)
                del disL[0]
                del L[0]
            else:
                disR[0].undraw()
                data[index] = R[0]
                highlight(win, display[index], "Move", highlighter = highR)
            
                display[index] = updateShape(display[index], data[index], SMAX, win)
                del disR[0]
                del R[0]
            index += 1

        # Checking if any element was left
        while len(L) > 0:
            disL[0].undraw()
            data[index] = L[0]
            highlight(win, display[index], "Move", highlighter = highL)
            
            display[index] = updateShape(display[index], data[index], SMAX, win)
            del disL[0]
            del L[0]
            index += 1

        while len(R) > 0:
            disR[0].undraw()
            data[index] = R[0]
            highlight(win, display[index], "Move", highlighter = highR)
            
            display[index] = updateShape(display[index], data[index], SMAX, win)
            del disR[0]
            del R[0]
            index += 1

        highlight(win, mode = "Delete", highlighter = highL)
        highlight(win, mode = "Delete", highlighter = highR)
