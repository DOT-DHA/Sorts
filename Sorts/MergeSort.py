from Display import *

#fix highlighting
#Working but not how i would like for show

def MergeSort(data, D):

    if len(data) > 1:


        mid = len(data)//2

        L = data[:mid]
        R = data[mid:]
        
        index = 0

        L = MergeSort(L, D)
        R = MergeSort(R, D)

        
        tempData = [0] * (len(L) + len(R))

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

        while len(L):
            tempData[index] = L[0]
            D.updateShape(tempData[index], index)
            del L[0]
            index += 1

        while len(R):
            tempData[index] = R[0]
            D.updateShape(tempData[index], index)
            del R[0]
            index += 1
        data = tempData

    return data