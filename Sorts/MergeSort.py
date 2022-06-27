from Display import *
from graphics import *
from Sorts.InsertionSort import InsertionSort

def MergeSort(*args):
    data, display, D = args[0], args[1], args[2]

    data = mainDriver(data, display, D)
    return data

def mainDriver(*args):
    data, display, D = args[0], args[1], args[2]

    if len(data) <= 1:
        return data
    else:

        # Finding the mid of the array
        mid = len(data)//2

        # Dividing the array elements
        L = data[:mid]

        # into 2 halves
        R = data[mid:]


        # Sorting the first half
        mainDriver(L, None, D)
        # Sorting the second half
        mainDriver(R, None, D)

        index = 0

        while len(L) and len(R):
            if L[0] < R[0]:
                data[index] = L[0]

                del L[0]
            else:
                data[index] = R[0]

                del R[0]
            index += 1

        # Checking if any element was left
        while len(L) > 0:
            data[index] = L[0]

            del L[0]
            index += 1

        while len(R) > 0:
            data[index] = R[0]

            del R[0]
            index += 1

    return data
