from heapq import heappush, heappop

n = int(input())
q = [list(map(int, input().split())) for _ in range(n)]
q.sort()

heap = []
heappush(heap, q[0][1])

for i in range(1, n):
    if heap[0] <= q[i][0]:
        heappop(heap)
    heappush(heap, q[i][1])

print(len(heap))