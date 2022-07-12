from Display import *
from graphics import *

#insertion sort works by picking the next 
#element and putting it in the right place
def InsertionSort(data, D):
    end = len(data)

    #start at the second element assuming the first is sorted
    for i in range(1, end):
        pos = i

        #swapping data down while smaller then element to its left
        while data[pos] < data[pos - 1]:

            #swapping data and updating shape
            data[pos], data[pos - 1] = data[pos - 1], data[pos]
            D.updateShape(data[pos], pos)
            D.updateShape(data[pos - 1], pos - 1)
            D.finish(pos)
            update()
            pos -= 1

            #dont want negative numbers
            if pos == 0:
                break
        
        #finishing the array
        D.finish(pos)
        if pos != 0:
            D.finish(pos - 1)

    return data