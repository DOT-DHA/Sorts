from Display import *

#fix highlighting
#not currently working

def MergeSort(data, display, D):
    if len(data) > 1:

        mid = len(data)//2

        L = data[:mid]
        disL = display[:mid]

        R = data[mid:]
        disR = display[mid:]

        data, display = MergeSort(L, disL, D)

        data, display = MergeSort(R, disR, D)

        
        lIndex, index, rIndex = 0, 0, 0
        tempData = [0] * (len(L)+len(R))

        while lIndex < len(L) and rIndex < len(R):
            if L[0] < R[0]:
                tempData[index] = L[lIndex]
                display[index] = disL[lIndex]
                D.updateShape(tempData[index], index)
                lIndex += 1
            else:
                tempData[index] = R[rIndex]
                display[index] = disR[rIndex]
                D.updateShape(tempData[index], index)
                rIndex += 1 
            index += 1

        while lIndex < len(L):
            tempData[index] = L[lIndex]
            display[index] = disL[lIndex]
            D.updateShape(tempData[index], index)
            lIndex += 1
            index += 1

        while lIndex < len(R):
            tempData[index] = R[rIndex]
            display[index] = disR[rIndex]
            D.updateShape(tempData[index], index)
            rIndex += 1
            index += 1

    return tempData, display