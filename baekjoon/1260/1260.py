from collections import deque

N, M, V = map(int, input().split())
graph = [ [0] * N for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1-1][v2-1] = graph[v2-1][v1-1] = 1

def dfs(v, visited=[]):
    visited.append(v)
    print(v, end=' ')

    for i, conn in enumerate(graph[v-1]):
        if conn and i+1 not in visited:
            dfs(i+1, visited)

def bfs(v):
    queue = deque([v])
    visited = [v]

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i, conn in enumerate(graph[v-1]):
            if conn and i+1 not in visited:
                queue.append(i+1)
                visited.append(i+1)

dfs(V)
print()
bfs(V)
