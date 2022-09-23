

def topologicalSort(G):
    N = len(G)

    inDegrees = [0 for _ in range(N)]

    for i in range(N):
        for v in G[i]:
            inDegrees[v-1] += 1
    
    linearOrder = []
    next = []

    for i in range(N):
        if inDegrees[i] == 0:
            next.append(i+1)

    while next:
        u = next.pop(0)
        linearOrder.append(u)

        for v in G[u-1]:
            inDegrees[v-1] -= 1
            if inDegrees[v-1] == 0:
                next.append(v)

    return linearOrder

if __name__ == '__main__':
    print(topologicalSort([
        [3],
        [4],
        [4, 5],
        [6],
        [6],
        [7, 11],
        [8],
        [13],
        [10],
        [11],
        [12],
        [13],
        [14],
        [],
    ]))
