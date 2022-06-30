import math as M
from Display import *
from graphics import *

#shell sort does an insertion sort with gaps
def ShellSort(data, D):
    
    end = len(data)
    cIndex = 0

    #finding the largest gap for the data set
    while True:
        temp = M.ceil((9*(9/4)**cIndex-4)/5)
        if temp > end:
            cIndex -= 1
            break
        cIndex += 1

    #Moving throught the array at a smaller and smaller gap
    for i in range(cIndex, -1, -1):
        gap = M.ceil((9 * (9 / 4) ** i - 4) / 5)
        
        #moving up the array from gap to end one place at a time
        for j in range(gap, end):
            pos = j

            #swapping data down while not in the right place
            while data[pos] < data[pos - gap]:

                #swaping data and updating display
                data[pos], data[pos - gap] = data[pos - gap], data[pos]
                D.updateShape(data[pos], pos)
                D.updateShape(data[pos - gap], pos - gap)

                pos -= gap

                #finishing if we are on the last loop
                if gap == 1:
                    D.finish(pos + gap)

                #dont want to go negative
                if pos - gap < 0:
                    break

            #finishing if we are on the last loop
            if gap == 1:
                D.finish(pos)
                
                #if at the first element then i need to skip this finish step
                if pos == 0:
                    continue
                D.finish(pos - gap)

    return data