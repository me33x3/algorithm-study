from collections import deque


def topology_sort():
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while len(queue) == 1:
        u = queue.popleft()
        ranking.append(u)

        for v in graph[u]:
            indegree[v] -= 1

            if indegree[v] == 0:
                queue.append(v)
            elif indegree[v] < 0:
                break


for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))

    ranking = []
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        u = t[i]
        for j in range(i+1, n):
            v = t[j]
            graph[u].append(v)
            indegree[v] += 1

    m = int(input())

    for _ in range(m):
        u, v = map(int, input().split())

        if u not in graph[v]:
            u, v = v, u

        graph[u].append(v)
        graph[v].remove(u)
        indegree[u] -= 1
        indegree[v] += 1

    topology_sort()

    if len(ranking) == n:
        print(*ranking)
    else:
        print('IMPOSSIBLE')