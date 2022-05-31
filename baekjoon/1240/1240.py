from collections import deque

def bfs(start, end):
    visited = [False] * (n + 1)
    visited[start] = True

    queue = deque([[start, 0]])
    while queue:
        u, dist = queue.popleft()

        for v in tree[u].keys():
            if v == end:
                return dist + tree[u][v]

            if not visited[v]:
                visited[v] = True
                queue.append([v, dist + tree[u][v]])

n, m = map(int, input().split())
tree = {i: dict() for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v, dist = map(int, input().split())
    tree[u][v] = dist
    tree[v][u] = dist

for _ in range(m):
    print(bfs(*map(int, input().split())))