import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    dist = [inf] * (n + 1)
    dist[1] = 0

    heap = []
    heappush(heap, [0, 1])

    while heap:
        curr_dist, curr = heappop(heap)

        if curr_dist > dist[curr]:
            continue

        for next, next_dist in edges[curr]:
            new_dist = curr_dist + next_dist

            if dist[next] > new_dist:
                dist[next] = new_dist
                heappush(heap, [new_dist, next])

    return int(dist[n] * 1000)

n, w = map(int, input().split())
m = float(input())

plants = [[]]
for _ in range(n):
    plants.append(list(map(int, input().split())))

edges = {i: [] for i in range(1, n + 1)}
for _ in range(w):
    a, b = map(int, input().split())
    edges[a].append([b, 0])
    edges[b].append([a, 0])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dist = (abs(plants[i][0] - plants[j][0]) ** 2 + abs(plants[i][1] - plants[j][1]) ** 2) ** 0.5
        if dist <= m:
            edges[i].append([j, dist])
            edges[j].append([i, dist])

print(dijkstra())