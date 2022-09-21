
def mergeSort(A, p, r):
    if p >= r:
        return

    q = (p + r) // 2

    mergeSort(A, p, q)
    mergeSort(A, q+1, r)

    merge(A, p, q, r)

    return A


def merge(A, p, q, r):
    B = A[p:q+1]
    C = A[q+1:r+1]

    B.append(float('inf'))
    C.append(float('inf'))

    i = j = 0
    for k in range(p, r+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1


if __name__ == '__main__':
    print(mergeSort([5, 19, 0, 3, -34, 1, 12, 34, 2, 8, 6, 9], 0, 11))