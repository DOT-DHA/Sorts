from graphics import *
from Display import *


def HeapSort(data, D):
    
    data = buildMaxHeap(data, D)
    end = len(data) - 1

    for i in range(end, 0, -1):
        data[0], data[i] = data[i], data[0]

        D.updateShape(data[0], 0)
        D.updateShape(data[i], i)
        D.finish(0)
        D.finish(i)

        maxHeapify(data, 0, D, i)

    return data


def buildMaxHeap(data, D):
    end = len(data) - 1

    for i in range(end//2, -1, -1):
        data = maxHeapify(data, i, D, end)
    return data


#for any index i where 1 <= i <= n
#data[1] is root
#data[i/2] is parent
#data[2i] is left child
#data[2i+1] is right child


def maxHeapify(data, index, D, end):

    if 2 * index < end and data[2 * index] > data[index]:
        largest = 2 * index
    else:
        largest = index

    if 2 * index + 1 < end and data[2 * index + 1] > data[largest]:
        largest = 2 * index + 1

    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        D.updateShape(data[index], index)
        D.updateShape(data[largest], largest)

        data = maxHeapify(data, largest, D, end)

    return data