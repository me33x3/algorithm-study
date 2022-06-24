import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    dist = [inf] * (N + 1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        curr_dist, curr = heapq.heappop(heap)

        if dist[curr] < curr_dist:
            continue

        for next, next_dist in graph[curr]:
            new_dist = curr_dist + next_dist

            if dist[next] > new_dist:
                dist[next] = new_dist
                heapq.heappush(heap, [dist[next], next])

    return dist

N, E = map(int, input().split())

graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())
dist = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

cnt = min(dist[v1] + dist_v1[v2] + dist_v2[N], dist[v2] + dist_v2[v1] + dist_v1[N])
print(cnt if cnt < inf else -1)