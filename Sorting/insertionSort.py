

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print(insertionSort([5, 2, 4, 6, 1, 3, 7, 43, 2, 0, 5, -1, -6]))