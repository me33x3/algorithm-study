from heapq import heappush, heappop

inf = int(1e9)

def dijkstra():
    heap = []
    heappush(heap, [0, s])

    dist = [inf] * (n + 1)
    dist[s] = 0

    while heap:
        curr_dist, curr = heappop(heap)

        if dist[curr] < curr_dist:
            continue

        for next, next_dist in graph[curr]:
            new_dist = curr_dist + next_dist

            if new_dist < dist[next]:
                dist[next] = new_dist
                heappush(heap, [new_dist, next])

    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

print(dijkstra()[t])