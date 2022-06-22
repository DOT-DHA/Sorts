from Display import *
from graphics import *
import math

def MergeSort(*args):
    data, display, win = args[0], args[1], args[2]

    data, display = mainDriver(data, display, win, max(data))
    print(data)

    for i in display:
        print(i.getCenter())

def mainDriver(*args):
    data, display, win, SMAX = args[0], args[1], args[2], args[3]

    if len(data) > 1:

        # Finding the mid of the array
        mid = len(data)//2

        # Dividing the array elements
        L = data[:mid]
        disL = display[:mid]

        # into 2 halves
        R = data[mid:]
        disR = display[mid:]

        # Sorting the first half
        L, disL = mainDriver(L, disL, win, SMAX)

        # Sorting the second half
        R, disR = mainDriver(R, disR, win, SMAX)

        index = 0

        while len(L) and len(R):
            if L[0] < R[0]:
                data[index] = L[0]
                display[index] = disL[0]
                highlightFlash(win, display[index],"Blue")
            
                disL[0].undraw()
                updateShape(display[index], data[index], SMAX, win)
                del disL[0]
                del L[0]
            else:
                data[index] = R[0]
                display[index] = disR[0]
                highlightFlash(win, display[index],"Blue")
            
                disR[0].undraw()
                display[index].draw(win)
                updateShape(display[index], data[index], SMAX, win)
                del disR[0]
                del R[0]
            index += 1

        # Checking if any element was left
        while len(L) > 0:
            data[index] = L[0]
            display[index] = disL[0]
            highlightFlash(win, display[index],"Blue")
            
            disL[0].undraw()
            display[index].draw(win)
            updateShape(display[index], data[index], SMAX, win)
            del disL[0]
            del L[0]
            index += 1

        while len(R) > 0:
            data[index] = R[0]
            display[index] = disR[0]
            highlightFlash(win, display[index],"Blue")
            
            disR[0].undraw()
            display[index].draw(win)
            updateShape(display[index], data[index], SMAX, win)
            del disR[0]
            del R[0]
            index += 1

        return data, display
    return data, display
