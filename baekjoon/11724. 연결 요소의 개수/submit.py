from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v)
    graph[v-1].append(u)

def bfs(v):
    visited[v-1] = True
    queue = deque(graph[v-1])

    while queue:
        u = queue.popleft()
        if not visited[u-1]:
            visited[u-1] = True
            queue.extend(graph[u-1])

    return 0

answer = 0
for i in range(N):
    if not visited[i]:
        bfs(i+1)
        answer += 1

print(answer)