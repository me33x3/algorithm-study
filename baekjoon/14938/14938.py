INF = int(1e9)

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

answer = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += t[j]
    answer = max(answer, tmp)

print(answer)