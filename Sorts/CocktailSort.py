from Display import *
from graphics import *


def CocktailSort(data, D):

    done = False

    start = 0
    end = len(data) - 1

    while not done:

        done = True
        for i in range(start, end):
            
            if data[i] > data[i + 1]:

                data[i], data[i + 1] = data[i + 1], data[i]
                
                D.updateShape(data[i], i)
                D.updateShape(data[i + 1], i + 1)

                done = False

        D.finish(end)

        if done:
            break

        end -= 1 
        
        for i in range(end-1, start-1, -1):

            if data[i] > data[i + 1]:

                data[i], data[i + 1] = data[i + 1], data[i]
                
                D.updateShape(data[i], i)
                D.updateShape(data[i + 1], i + 1)

                done = False

        D.finish(start)
        start += 1
    
    while start <= end:
        D.finish(start)
        start += 1 
        D.finish(end)
        end -= 1 