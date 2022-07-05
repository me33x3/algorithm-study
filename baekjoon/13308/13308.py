import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    heap = []
    heapq.heappush(heap, [0, costs[1], 1])

    dp = [[inf] * (max(costs) + 1) for _ in range(N + 1)]
    dp[1][costs[1]] = 0

    while heap:
        dist, cost, curr = heapq.heappop(heap)

        if curr == N:
            return dist

        if dist > dp[curr][cost]:
            continue

        for next, next_dist in routes[curr]:
            new_dist = dist + next_dist * cost

            if dp[next][cost] > new_dist:
                dp[next][cost] = new_dist
                heapq.heappush(heap, [new_dist, min(cost, costs[next]), next])

N, M = map(int, input().split())
costs = [0] + list(map(int, input().split()))

routes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    routes[a].append([b, c])
    routes[b].append([a, c])

print(dijkstra())