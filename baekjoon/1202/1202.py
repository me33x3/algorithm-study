import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
gems = sorted(list(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))

answer = 0
heap = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(heap, -gems[0][1])
        heapq.heappop(gems)

    if heap:
        answer += -heapq.heappop(heap)

print(answer)