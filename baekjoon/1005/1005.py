import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        dp[u] += t[u]

        if u == w:
            break

        for v in graph[u]:
            indegree[v] -= 1
            dp[v] = max(dp[v], dp[u])

            if indegree[v] == 0:
                queue.append(v)


for _ in range(int(input())):
    n, k = map(int, input().split())
    t = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    topology_sort()
    print(dp[w])