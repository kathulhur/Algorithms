
def countKeysEqual(A, n, m):
    equal = [0 for _ in range(m)]
    for i in range(n):
        key = A[i]
        equal[key] += 1

    return equal

def countKeysLess(equal, m):
    less = [0 for _ in range(m)]

    for j in range(1, m):
        less[j] = less[j-1] + equal[j-1]

    return less

def rearrange(A, less, n, m):
    B = [0 for _ in range(n)]
    next = [0 for _ in range(m)]

    for j in range(m):
        next[j] = less[j]

    for i in range(n):
        key = A[i]
        index = next[key]
        B[index] = A[i]
        next[key] += 1
    
    return B


def countingSort(A, n, m):
    equal = countKeysEqual(A, n, m)
    less = countKeysLess(equal, m)
    B = rearrange(A, less, n, m)
    return B


# same with counting sort but uses only a single array instead of 3 separate for the equal, less, and next
def betterCountingSort(A, n, m):
    next = [0 for _ in range(m)]
    # get the number of keys
    for i in range(n):
        key = A[i]
        next[key] += 1
    
    # get the number of elements less than a key as well as the next indices for the keys
    prev = 0
    for i in range(1, m):
        tmp = next[i]
        next[i] = next[i-1] + prev
        prev = tmp
    
    # sort the array
    B = [0 for _ in range(n)]
    for i in range(n):
        key = A[i]
        index = next[key]
        B[index] = A[i]
        next[key] += 1

    return B

if __name__ == '__main__':
    print(betterCountingSort([9, 8, 7, 6, 0, 3, 5, 4, 3, 2, 1, 7], 12, 10))