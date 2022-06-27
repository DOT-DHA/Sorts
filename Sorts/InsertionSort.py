from Display import *
from graphics import *

def InsertionSort(*args):
    data, D = args[0], args[1]

    end = len(data)

    for i in range(1, end):
        pos = i

        while data[pos] < data[pos - 1]:

            data[pos], data[pos - 1] = data[pos - 1], data[pos]

            D.updateShape(data[pos], pos)
            D.updateShape(data[pos - 1], pos - 1)

            pos -= 1

            D.finish(pos + 1)
            D.finish(pos)

            if pos == 0:
                break
        if pos == 0: 
            D.finish(pos)
        else:
            D.finish(pos - 1)

    D.finish(end - 1)

            

    return data