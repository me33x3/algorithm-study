import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    heap = []
    heapq.heappush(heap, [0, 0])

    time = [inf] * n
    time[0] = 0

    while heap:
        curr_t, curr = heapq.heappop(heap)

        if curr_t > time[curr]:
            continue

        for next, next_t in graph[curr]:
            new_t = curr_t + next_t

            if not arr[next] and new_t < time[next]:
                time[next] = new_t
                heapq.heappush(heap, [new_t, next])

    return time[-1] if time[-1] != inf else -1

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr[-1] = 0

graph = {i: [] for i in range(n)}
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

print(dijkstra())