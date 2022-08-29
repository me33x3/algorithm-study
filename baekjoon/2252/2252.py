from collections import deque


def topology_sort():
    queue = deque()

    for i in range(1, v + 1):
        if not indegree[i]:
            queue.append(i)

    while queue:
        n = queue.popleft()
        print(n, end=' ')

        for i in graph[n]:
            indegree[i] -= 1

            if not indegree[i]:
                queue.append(i)


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

topology_sort()