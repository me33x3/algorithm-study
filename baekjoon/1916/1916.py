import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
dp = [INF for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dept, dest = map(int, input().split())

queue = []
heapq.heappush(queue, [0, dept])

while queue:
    cost, u = heapq.heappop(queue)

    if dp[u] < cost:
        continue

    for v, new_cost in graph[u]:
        tmp = cost + new_cost

        if dp[v] > tmp:
            dp[v] = tmp
            heapq.heappush(queue, [tmp, v])

print(dp[dest])