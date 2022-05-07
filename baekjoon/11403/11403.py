from collections import deque

n = int(input())
graph = {}

for i in range(n):
    graph[i] = []
    for j, val in enumerate(input().split()):
        if val == '1':
            graph[i].append(j)

for i in range(n):
    visited = [False] * n
    queue = deque(graph[i])

    while queue:
        j = queue.popleft()
        visited[j] = True
        for k in graph[j]:
            if not visited[k]:
                queue.append(k)

    for v in visited:
        print(1 if v else 0, end=' ')
    print()