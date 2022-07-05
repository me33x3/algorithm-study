import sys
from heapq import heappush, heappop
from collections import defaultdict

input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])

    seconds = [inf] * (n + 1)
    seconds[start] = 0

    while heap:
        curr_sec, curr = heappop(heap)

        for next, next_sec in net[curr]:
            new_sec = curr_sec + next_sec

            if new_sec < seconds[next]:
                seconds[next] = new_sec
                heappush(heap, [new_sec, next])

    res = [sec for sec in seconds if sec != inf]

    return [len(res), max(res)]

for _ in range(int(input())):
    n, d, c = map(int, input().split())

    net = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        net[b].append([a, s])

    print(*dijkstra(c))