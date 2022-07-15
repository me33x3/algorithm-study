import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    dist[X] = 0

    heap = []
    heapq.heappush(heap, [0, X])

    while heap:
        curr_dist, curr = heapq.heappop(heap)

        if curr_dist > dist[curr]:
            continue

        for next in roads[curr]:
            next_dist = curr_dist + 1

            if next_dist < dist[next]:
                dist[next] = next_dist
                heapq.heappush(heap, [next_dist, next])

N, M, K, X = map(int, input().split())

dist = [inf] * (N + 1)
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)

dijkstra()

res = []
for i in range(1, N + 1):
    if dist[i] == K:
        res.append(i)

if res:
    for i in res:
        print(i)
else:
    print(-1)