import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] or (graph[a][c] and graph[c][b]):
                graph[a][b] = 1

cnt = 0
for i in range(1, n + 1):
    if sum([graph[i][j] + graph[j][i] for j in range(1, n + 1)]) == n - 1:
        cnt += 1

print(cnt)