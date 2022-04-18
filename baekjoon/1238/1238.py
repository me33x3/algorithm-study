import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(graph):
    dp = [INF for _ in range(N + 1)]
    dp[0], dp[X] = 0, 0

    queue = []
    heapq.heappush(queue, [0, X])
    while queue:
        dist, u = heapq.heappop(queue)

        if dp[u] < dist:
            continue

        for v, v_dist in graph[u]:
            new_dist = dist + v_dist

            if dp[v] > new_dist:
                dp[v] = new_dist
                heapq.heappush(queue, [new_dist, v])

    return dp

N, M, X = map(int, input().split())
village = [[] for _ in range(N + 1)]
rev_village = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    village[u].append([v, w])
    rev_village[v].append([u, w])

print(max(list(map(lambda x, y: x + y, dijkstra(village), dijkstra(rev_village)))))