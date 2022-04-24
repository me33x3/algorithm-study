import sys
import heapq
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(heapq.heappop(heap) * -1 if heap else 0)
    else:
        heapq.heappush(heap, n * -1)