
from textwrap import indent


def topologicalSort(G):
    N = len(G)

    inDegrees = [0 for _ in range(N)]

    for i in range(N):
        for v in G[i]:
            inDegrees[v] += 1

    linearOrder = []
    next = []

    for i in range(N):
        if inDegrees[i] == 0:
            next.append(i)
    
    while next:
        u = next.pop(0)
        linearOrder.append(u)

        for v in G[u]:
            inDegrees[v] -= 1
            if inDegrees[v] == 0:
                next.append(v)
                
    return linearOrder


def DAGShortestPaths(G, s, weights):
    l = topologicalSort(G)
    shortest = [float('inf') for _ in range(len(G))]
    shortest[s] = 0

    pred = [None for _ in range(len(G))]

    for u in l:
        for v in G[u]:
            if shortest[u] + weights[u][v]  < shortest[v]:
                shortest[v] = shortest[u] + weights[u][v]
                pred[v] = u


    return shortest

if __name__ == '__main__':
    print(DAGShortestPaths([
            [2, 3],
            [0, 2],
            [3, 4, 5],
            [4, 5],
            [5],
            []
        ],
        1, 
        [
            [0, 0, 2, 6, 0, 0],
            [5, 0, 3, 0, 0, 0],
            [0, 0, 0, 7, 4, 2],
            [0, 0, 0, 0, -1, 1],
            [0, 0, 0, 0, 0, -2],
            [0, 0, 0, 0, 0, 0],
        ]
    ))
    
