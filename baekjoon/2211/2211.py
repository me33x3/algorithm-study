import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

res = [0] * (n + 1)
dp = [inf] * (n + 1)
dp[1] = 0

heap = []
heapq.heappush(heap, [0, 1])

while heap:
    t, curr = heapq.heappop(heap)

    if t > dp[curr]:
        continue

    for next, next_t in edges[curr]:
        new_t = t + next_t

        if new_t < dp[next]:
            res[next] = curr
            dp[next] = new_t
            heapq.heappush(heap, [new_t, next])

print(n - 1)
for i in range(2, n + 1):
    print(i, res[i])