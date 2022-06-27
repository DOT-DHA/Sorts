import math as M
from Display import *
from graphics import *


def ShellSort(*args):
    data, D = args[0], args[1]

    end = len(data)

    cIndex = 0

    while True:
        temp = M.ceil((9*(9/4)**cIndex-4)/5)
        if temp > end:
            cIndex -= 1
            break
        cIndex += 1

    while cIndex >= 0:
        gap = M.ceil((9 * (9 / 4) ** cIndex - 4) / 5)
        
        for i in range(gap, end):
            pos = i

            while data[pos] < data[pos - gap]:
                data[pos], data[pos - gap] = data[pos - gap], data[pos]

                D.updateShape(data[pos], pos)
                D.updateShape(data[pos - gap], pos - gap)

                pos -= gap

                if gap == 1:
                    D.finish(pos + gap)
                    D.finish(pos)

                if pos - gap < 0:
                    break
            if gap == 1:
                D.finish(pos - gap)
            
        cIndex -= 1

    return data