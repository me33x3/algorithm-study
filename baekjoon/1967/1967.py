import sys
sys.setrecursionlimit(10**6)

def dfs(vtx, wei):
    for child, w in tree[vtx]:
        if dist[child] == -1:
            dist[child] = wei + w
            dfs(child, dist[child])

n = int(input())
tree = {i: [] for i in range(1, n + 1)}
wei = [0] * (n + 1)

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])
    wei[v] = w

dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1] * (n + 1)
dist[start] = 0
dfs(start, 0)
print(max(dist))