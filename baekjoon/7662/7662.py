import sys, heapq
input = sys.stdin.readline

def sync(heap):
    while heap and not v[heap[0][1]]:
        heapq.heappop(heap)
    return True if len(heap) else False

for _ in range(int(input())):
    minheap, maxheap = [], []
    k = int(input())
    v = [False] * k
    for i in range(k):
        order, n = input().rstrip().split()
        n = int(n)

        if order == 'I':
            heapq.heappush(minheap, (n, i))
            heapq.heappush(maxheap, (-n, i))
            v[i] = True
        else:
            if n == 1 and sync(maxheap):
                v[heapq.heappop(maxheap)[1]] = False
            elif n == -1 and sync(minheap):
                v[heapq.heappop(minheap)[1]] = False

    if sync(maxheap) and sync(minheap):
        print(-maxheap[0][0], minheap[0][0])
    else:
        print('EMPTY')