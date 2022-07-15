import sys
inf = sys.maxsize

n, m = map(int, input().split())

graph = [[inf] * (n + 1) for _ in range(n + 1)]
res = [['-'] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = c
    res[a][b] = b
    res[b][a] = a

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            tmp = graph[a][i] + graph[i][b]

            if graph[a][b] > tmp:
                graph[a][b] = tmp
                res[a][b] = res[a][i]

for row in res[1:]:
    print(*row[1:])