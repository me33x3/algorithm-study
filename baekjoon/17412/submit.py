from collections import deque

def network_flow():
    start, end = 1, 2
    res = 0
    while True:
        visited = [-1] * (n + 1)
        visited[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for v in range(1, n + 1):
                if visited[v] == -1 and c[u][v] > f[u][v]:
                    visited[v] = u
                    q.append(v)
                    if v == end: break

        if visited[end] == -1: break

        i = end
        while i != start:
            f[visited[i]][i] += 1
            f[i][visited[i]] -= 1
            i = visited[i]
        res += 1

    return res

n, p = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
c = [[0] * (n + 1) for _ in range(n + 1)]
f = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(p):
    u, v = map(int, input().split())
    graph[u].append(v)
    c[u][v] = 1

print(network_flow())