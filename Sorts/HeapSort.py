from graphics import *
from Display import *


def HeapSort(*args):
    data, display, win = args[0], args[1], args[2]
    
    data = buildMaxHeap(data, display, win)
    end = len(data)-1

    for i in range(end, 0, -1):
        temp = data[0]
        data[0] = data[i]
        data[i] = temp

        maxHeapify(data, display, 0, win, i)

        display[0] = updateBar(display[0], data[0], max(data), win)
        display[i] = updateBar(display[i], data[i], max(data), win)

        flash([display[0], display[i]], "Red")
        finish(display[i])
    finish(display[0])
    return data


def buildMaxHeap(data, display, win):
    for i in range((len(data)-1)//2, -1, -1):
        data = maxHeapify(data, display, i, win)
    return data


#for any index i where 1 <= i <= n
#data[1] is root
#data[i/2] is parent
#data[2i] is left child
#data[2i+1] is right child

def maxHeapify(data, display, index, win, end = 0):

    if end == 0:
        end = len(data)

    if 2 * index < end and data[2 * index] > data[index]:
        largest = 2 * index
    else:
        largest = index

    if 2 * index + 1 < end and data[2 * index + 1] > data[largest]:
        largest = 2 * index + 1

    if largest != index:
        temp = data[index]
        data[index] = data[largest]
        data[largest] = temp

        display[index] = updateBar(display[index], data[index], max(data), win)
        display[largest] = updateBar(display[largest], data[largest], max(data), win)

        flash([display[index], display[largest]], "Blue")

        data = maxHeapify(data, display, largest, win, end)


    return data