from Display import *

#fix highlighting
#"done" but not displaying how i would like

def MergeSort(data, D):

    if len(data) > 1:


        mid = len(data)//2

        L = data[:mid]
        R = data[mid:]
        
        L = MergeSort(L, D)
        R = MergeSort(R, D)

        tempData = [0] * (len(L) + len(R))

        index = 0

        while len(L) and len(R):
            if L[0] < R[0]:
                tempData[index] = L[0]
                D.updateShape(tempData[index], index)
                del L[0]
            else:
                tempData[index] = R[0]
                D.updateShape(tempData[index], index)
                del R[0]
            index += 1
            update()

        while len(L):
            tempData[index] = L[0]
            D.updateShape(tempData[index], index)
            del L[0]
            index += 1
            update()

        while len(R):
            tempData[index] = R[0]
            D.updateShape(tempData[index], index)
            del R[0]
            index += 1
            update()
        data = tempData

    if len(data) == len(D.display):
        for i in range(len(data)):
            D.finish(i)

    return data