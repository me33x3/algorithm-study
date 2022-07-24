import heapq

def dijkstra():
    dist[Y] = 0
    heap = []
    heapq.heappush(heap, [Y, 0])

    while heap:
        curr, curr_dist = heapq.heappop(heap)

        if curr_dist > dist[curr]:
            continue

        for next, next_dist in edges[curr]:
            new_dist = curr_dist + next_dist

            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(heap, [next, new_dist])

inf = int(1e9)

N, M, X, Y = map(int, input().split())

dist = [inf] * N

edges = {i: [] for i in range(N)}
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])

dijkstra()

dist.sort()
day, tmp = 1, 0

for d in dist:
    if d * 2 > X:
        day = -1
        break
    else:
        if tmp + d * 2 > X:
            day += 1
            tmp = 0
        tmp += d * 2

print(day)