n, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in  range(n + 1):
    graph[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if graph[u][i] and graph[i][v]:
                graph[u][v] = 1

for _ in range(int(input())):
    u, v = map(int, input().split())

    if graph[u][v]:
        print(-1)
    elif graph[v][u]:
        print(1)
    else:
        print(0)