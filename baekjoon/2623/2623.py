from collections import deque


def topology_sort():
    queue = deque([i for i in range(1, n+1) if indegree[i] == 0])

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            indegree[v] -= 1

            if indegree[v] == 0:
                queue.append(v)


n, m = map(int, input().split())

order = []
graph = [set() for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    data = list(map(int, input().split()))
    cnt = data[0]

    for i in range(1, cnt):
        for j in range(i+1, cnt+1):
            a, b = data[i], data[j]
            if b not in graph[a]:
                graph[a].add(b)
                indegree[b] += 1

topology_sort()

if len(order) == n:
    for i in order:
        print(i)
else:
    print(0)