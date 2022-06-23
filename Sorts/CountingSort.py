from Display import *


def CountingSort(*args, divisor = None):
    data, display, win, base = args[0], args[1], args[2], args[3]

    count = [0] * (base + 1)
    sorted = [0] * len(data)

    high = highlight(win, target = display[0], mode = "Create", color = "Yellow",)

    for i in range(len(data)):
        if divisor is not None:
            count[(data[i]//divisor) % 10] += 1
            highlight(win, display[i], "Move", highlighter = high)
        else:
            count[data[i]] += 1
            highlight(win, display[i], "Move", highlighter = high)

    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in range(len(count)-1, 0, -1):
        count[i] = count[i-1]

    count[0] = 0


    if divisor is not None:
        for i in range(0, len(data)):
            sorted[count[(data[i]//divisor) % 10]] = data[i]
            count[(data[i]//divisor) % 10] += 1
    else:
        for i in range(len(data)):
            sorted[count[data[i]]] = data[i]
            count[data[i]] += 1
    
    data = sorted[:]
    highlight(win, mode = "Change", highlighter = high)

    for i in range(len(sorted)):
        display[i] = updateShape(display[i], data[i], max(data), win)
        highlight(win, display[i], "Move", highlighter = high)
        
        if divisor is None:
            finish(display[i])
        elif divisor * 10 > max(data):
            finish(display[i])
    
    highlight(win, mode = "Delete", highlighter = high)

    return data