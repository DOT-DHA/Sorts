from Display import *
from graphics import *


def ShellSort(*args):
    data, display, win = args[0], args[1], args[2]
    done = False
    dist = 2
    end = len(data)

    while not done:
        done = True
        gap = end//dist
        if gap < 1:
            gap = 1

        for i in range(end):
            if gap+i < end:
                if data[i] > data[gap + i]:

                    temp = data[gap + i]
                    data[gap+i] = data[i]
                    data[i] = temp
                    
                    display[i] = updateBar(display[i], data[i], max(data), win)
                    display[gap + i] = updateBar(display[gap + i], data[gap + i], max(data), win)

                    flash([display[i], display[gap + i]], "Blue")

                    done = False
        dist *= 2
        
    for i in display:
        finish(i)
        
    return data