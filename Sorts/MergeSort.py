from Display import *

def MergeSort(data, D, l, r):
    if(l < r):

        m = l + (r - l) // 2

        data = MergeSort(data, D, l, m)
        data = MergeSort(data, D, m + 1, r)

        finish = False
        if (r-l)+1 == len(data):
            finish = True

        data = Merge(data, D, l, m, r, finish)

    return data

def Merge(data, D, start, mid, end, finish):
    start2 = mid + 1

    if (data[mid] <= data[start2]):
        if finish:
            D.finish(mid)
            D.finish(start2)
        return data
    
    while (start <= mid and start2 <= end):

        if (data[start] <= data[start2]):
            if finish:
                D.finish(start2)
            start += 1

        else:
            value = data[start2]
            index = start2

            while(index != start):
                data[index] = data[index - 1]
                D.updateShape(data[index], index)
                index -= 1
                if finish:
                    D.finish(index + 1)
                    D.finish(index)
            
            data[start] = value
            D.updateShape(data[start], start)

            if finish:
                D.finish(start)

            start += 1
            mid += 1
            start2 += 1

    return data