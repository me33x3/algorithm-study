import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    cnt = 1
    queue = deque([start])
    visited = [False for _ in range(n+1)]
    visited[start] = True

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                queue.append(v)

    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_cnt, max_list = 1, []
for i in range(1, n + 1):
    cnt = bfs(i)

    if cnt > max_cnt:
        max_cnt = cnt
        max_list.clear()
        max_list.append(i)
    elif cnt == max_cnt:
        max_list.append(i)

print(*max_list)