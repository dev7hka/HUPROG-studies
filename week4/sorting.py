def selectionSort(arr: [int]) -> [int]:
    length = len(arr)
    for i in range(length-1):
        tmp = i
        for j in range(i+1, length):
           if arr[j] < arr[i]:
               tmp = j
        arr[i], arr[tmp] = arr[tmp], arr[i]
    return arr

def bubbleSort(arr: [int]):
    length = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        length-=1

def insertionSort(arr: [int]) -> [int]:
    length = len(arr)
    for i in range(length-1):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def merge(arr: [int], l: int, m: int, r: int) -> [int]:

    arrLeft = arr[l: m+1]
    arrRight = arr[m+1:r+1]

    left, right, k = 0, 0, l

    while left < len(arrLeft) and right < len(arrRight):
        if arrLeft[left] < arrRight[right]:
            arr[k] = arrLeft[left]
            left+=1
        else:
            arr[k] = arrRight[right]
            right+=1
        k+=1

    while left < len(arrLeft):
        arr[k] = arrLeft[left]
        left+=1
        k+=1
    while right < len(arrRight):
        arr[k] = arrRight[right]
        right+=1
        k+=1

def mergeSort(arr: [int], l: int, r: int) -> [int]:
    if r <= l:
        return
    m = l + (r-l)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

def partition(arr: [int], l:int, r:int):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quickSort(arr: [int], l, r) -> [int]:
    if r-l < 2:
        return
    pivot = partition(arr, l, r)
    quickSort(arr, l, pivot-1)
    quickSort(arr, pivot+1, r)

test = [2,5,3,1,7,6,-1,-2,10]
print(bubbleSort(test))
print(test)