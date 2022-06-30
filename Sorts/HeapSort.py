from graphics import *
from Display import *

#heap sort creates a heap then swaps the first index 
#with the last index making the sorted array
def HeapSort(data, D):
    
    data = buildMaxHeap(data, D)
    end = len(data) - 1

    #swaps first element and the last element and then remakes the heap
    for i in range(end, 0, -1):
        data[0], data[i] = data[i], data[0]

        #swap and finish
        D.updateShape(data[0], 0)
        D.updateShape(data[i], i)
        D.finish(i)

        #re-heap after moving
        maxHeapify(data, 0, D, i)

    return data

#builds the heap by heapifying the array starting in the middle
def buildMaxHeap(data, D):
    end = len(data) - 1

    for i in range(end//2, -1, -1):
        data = maxHeapify(data, i, D, end)
    return data


#for any index i where 1 <= i <= n
#data[i] is root
#data[i/2] is parent
#data[2i] is left child
#data[2i+1] is right child

#maxheapify function builds binary tree with the data provided.
def maxHeapify(data, index, D, end):

    #checks if left child is bigger then parent
    if 2 * index < end and data[2 * index] > data[index]:
        largest = 2 * index
    else:
        largest = index

    #checks if right child is bigger then parent or left child
    if 2 * index + 1 < end and data[2 * index + 1] > data[largest]:
        largest = 2 * index + 1

    #checks if a swap is nessisary
    if largest != index:
        #swaps
        data[index], data[largest] = data[largest], data[index]
        D.updateShape(data[index], index)
        D.updateShape(data[largest], largest)

        #move down array if needed.
        data = maxHeapify(data, largest, D, end)

    return data