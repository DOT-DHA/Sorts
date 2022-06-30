from Display import *

#counting sort counts how many times a number shows up 
#then makes a new array with that
def CountingSort(data, D, base = None, divisor = None):

    size = len(data)
    count = [0] * base
    sorted = [0] * size

    #counting amout of times a number shows up
    #also changes base for radix sort
    for i in range(size):
        if divisor is not None:
            count[(data[i]//divisor) % base] += 1
        else:
            count[data[i]] += 1

    #adding count of each number to get ending position in array
    for i in range(1, base):
        count[i] += count[i-1]
    
    #moving count over 1 space to find starting space for number
    for i in range(base-1, 0, -1):
        count[i] = count[i-1]
    count[0] = 0

    #Creating final sorted array by placing numbers at their count position
    if divisor is not None:
        for i in range(0, size):
            sorted[count[(data[i]//divisor) % base]] = data[i]
            count[(data[i]//divisor) % base] += 1
    else:
        for i in range(size):
            sorted[count[data[i]]] = data[i]
            count[data[i]] += 1
    
    #copying sorted data
    data = sorted[:]

    #showing updated data
    for i in range(len(data)):
        D.updateShape(data[i], i)
        if divisor is not None:
            if divisor * base > max(data):
                D.finish(i)
        else:
            D.finish(i)

    return data