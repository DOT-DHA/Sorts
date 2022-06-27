from Display import *


def CountingSort(*args, divisor = None):
    data, D, base = args[0], args[1], args[2]

    size = len(data)
    count = [0] * base
    sorted = [0] * size

    for i in range(base):
        if divisor is not None:
            count[(data[i]//divisor) % base] += 1
        else:
            count[data[i]] += 1

    for i in range(1, base):
        count[i] += count[i-1]
    
    for i in range(base-1, 0, -1):
        count[i] = count[i-1]

    count[0] = 0


    if divisor is not None:
        for i in range(0, size):
            sorted[count[(data[i]//divisor) % base]] = data[i]
            count[(data[i]//divisor) % base] += 1
    else:
        for i in range(size):
            sorted[count[data[i]]] = data[i]
            count[data[i]] += 1
    
    data = sorted[:]

    for i in range(len(data)):
        D.updateShape(data[i], i)

    return data