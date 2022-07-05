import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    heap = []
    heapq.heappush(heap, [0, 1])

    costs = [inf] * (n + 1)
    costs[1] = 0

    while heap:
        curr_c, curr = heapq.heappop(heap)

        if curr_c <= costs[curr]:
            for next, next_c in graph[curr]:
                new_c = curr_c + next_c

                if new_c < costs[next]:
                    costs[next] = new_c
                    heapq.heappush(heap, [new_c, next])

    return costs[-1]

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

print(dijkstra())