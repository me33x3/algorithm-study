import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    dist = [inf] * (n + 1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        curr_dist, curr = heapq.heappop(heap)

        if curr_dist > dist[curr]:
            continue

        for next, next_dist in routes[curr]:
            new_dist = curr_dist + next_dist

            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(heap, [new_dist, next])

    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    routes = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        routes[a].append([b, d])
        routes[b].append([a, d])

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    res = []
    for _ in range(t):
        x = int(input())
        if s_[g] + g_[h] + h_[x] == s_[x] or s_[h] + h_[g] + g_[x] == s_[x]:
            res.append(x)

    print(*sorted(res))