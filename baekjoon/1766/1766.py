import heapq

n, m = map(int, input().split())

indegree = [0] * (n + 1)
better = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    better[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(heap, i)

while heap:
    a = heapq.heappop(heap)
    print(a, end=' ')

    for b in better[a]:
        indegree[b] -= 1
        if not indegree[b]:
            heapq.heappush(heap, b)