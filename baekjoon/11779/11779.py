import sys, copy
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    cost[start] = 0
    heap = []
    heappush(heap, [cost[start], start])

    while heap:
        curr_cost, curr = heappop(heap)

        if curr_cost > cost[curr]:
            continue

        for next, next_cost in bus[curr]:
            new_cost = curr_cost + next_cost

            if new_cost < cost[next]:
                cost[next] = new_cost
                heappush(heap, [new_cost, next])
                path[next] = copy.deepcopy(path[curr]) + [next]

n, m = int(input()), int(input())

bus = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append([b, c])

start, end = map(int, input().split())

cost = [inf] * (n + 1)
path = [[] for _ in range(n + 1)]
path[start] = [start]

dijkstra(start)

print(cost[end])
print(len(path[end]))
print(*path[end])