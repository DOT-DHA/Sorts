from Display import *
from graphics import *

#cocktail sort moves biggest to top then smallest to the bottom
def CocktailSort(data, D):

    done = False
    start = 0
    end = len(data) - 1

    #loop for as long as something has to be swapped
    while not done:

        #assume were done
        done = True

        #looking for the biggest object
        for i in range(start, end):
            
            #move biggest up
            if data[i] > data[i + 1]:

                #swap it
                data[i], data[i + 1] = data[i + 1], data[i]
                
                D.updateShape(data[i], i)
                D.updateShape(data[i + 1], i + 1)
                update()

                done = False

        #biggest is now in place
        D.finish(end)

        if done:
            break

        end -= 1
        
        #looking for the smallest
        for i in range(end-1, start-1, -1):

            #move smallest down
            if data[i] > data[i + 1]:

                #swap it
                data[i], data[i + 1] = data[i + 1], data[i]
                
                D.updateShape(data[i], i)
                D.updateShape(data[i + 1], i + 1)
                update()

                done = False

        #smallest is now in place
        D.finish(start)
        start += 1
    
    #finishing the rest of the array
    while start <= end:
        D.finish(start)
        start += 1 
        D.finish(end)
        end -= 1 