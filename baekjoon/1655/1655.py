import sys
from heapq import heappush, heappop

input = sys.stdin.readline

lh, rh = [], []
answer = []

for _ in range(int(input())):
    if len(lh) == len(rh):
        heappush(lh, -int(input()))
    else:
        heappush(rh, int(input()))

    if rh and -lh[0] > rh[0]:
        max = heappop(lh)
        min = heappop(rh)

        heappush(lh, -min)
        heappush(rh, -max)

    answer.append(-lh[0])

for i in answer:
    print(i)