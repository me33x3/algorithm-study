import heapq
from heapq import heappush, heappop

inf = int(1e9)

def dijkstra(start):
    dist = [inf] * (V + 1)
    dist[start] = 0

    heap = []
    heappush(heap, [start, 0])

    while heap:
        curr, curr_dist = heappop(heap)

        if curr_dist > dist[curr]:
            continue

        for next, next_dist in edges[curr]:
            new_dist = curr_dist + next_dist

            if new_dist < dist[next]:
                dist[next] = new_dist
                heappush(heap, [next, new_dist])

    return dist

V, E, P = map(int, input().split())

edges = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

dist_m = dijkstra(1)
dist_g = dijkstra(P)

print('SAVE HIM' if dist_m[P] + dist_g[V] <= dist_m[V] else 'GOOD BYE')