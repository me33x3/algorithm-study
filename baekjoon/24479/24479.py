import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    global cnt
    res[i] = cnt
    graph[i].sort()

    for v in graph[i]:
        if not res[v]:
            cnt += 1
            dfs(v)

N, M, R = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
res = [0] * (N + 1)
dfs(R)
print('\n'.join(map(str, res[1:])))