
def quickSort(A, p, r):
    if p >= r:
        return
    
    q = partition(A, p, r)

    quickSort(A, p, q-1)
    quickSort(A, q+1, r)

    return A


def partition(A, p, r):
    q = p

    for u in range(p, r):
        if A[u] <= A[r]:
            A[q], A[u] = A[u], A[q]
            q += 1

    A[r], A[q] = A[q], A[r]

    return q


if __name__ == '__main__':
    print(quickSort([1, 8, 7, 5, 2, 3, 5, 6, -4, 0, -1, 10, 9, -6, -2, 11, 7], 0, 16))