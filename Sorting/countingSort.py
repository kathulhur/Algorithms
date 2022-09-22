
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


if __name__ == '__main__':
    print(countingSort([9, 8, 7, 6, 0, 3, 5, 4, 3, 2, 1], 11, 10))