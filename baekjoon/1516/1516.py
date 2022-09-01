from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)
dp = [0] * (n+1)

for v in range(1, n+1):
    data = list(map(int, input().split()))
    cost[v] = data[0]

    for u in data[1:-1]:
        graph[u].append(v)
        indegree[v] += 1

queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
while queue:
    u = queue.popleft()
    dp[u] += cost[u]

    for v in graph[u]:
        dp[v] = max(dp[v], dp[u])
        indegree[v] -= 1

        if indegree[v] == 0:
            queue.append(v)

for i in range(1, n+1):
    print(dp[i])