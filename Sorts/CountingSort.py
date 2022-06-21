from Display import *


def CountingSort(*args):
    if len(args) > 4:
        data, display, win, base, divisor = args[0], args[1], args[2], args[3], args[4]
    else:
        data, display, win, base = args[0], args[1], args[2], args[3]
        divisor = 0

    count = [0] * (base + 1)
    sorted = [0] * len(data)

    for i in range(len(data)):
        if divisor > 0:
            count[(data[i]//divisor) % 10] += 1
            flash(display[i], "blue")
        else:
            count[data[i]] += 1
            flash(display[i], "blue")

    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in range(len(count)-1, 0, -1):
        count[i] = count[i-1]

    count[0] = 0


    if divisor > 0:
        for i in range(0, len(data)):
            sorted[count[(data[i]//divisor) % 10]] = data[i]
            count[(data[i]//divisor) % 10] += 1
    else:
        for i in range(len(data)):
            sorted[count[data[i]]] = data[i]
            count[data[i]] += 1
    
    data = sorted[:]

    for i in range(len(sorted)):
        display[i] = updateBar(display[i], data[i], max(data), win)
        flash(display[i], "green")
    
    return data