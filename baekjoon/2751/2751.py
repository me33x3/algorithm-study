import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

while heap:
    print(heapq.heappop(heap))