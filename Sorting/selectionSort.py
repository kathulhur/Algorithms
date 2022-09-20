

def selectionSort(arr):
    for i in range(len(arr)):
        smallest = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


print(selectionSort([3, 5, 7, 1, 0, 6, 9, 2]))