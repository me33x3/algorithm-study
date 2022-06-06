import copy
from collections import deque
from itertools import combinations

def bfs():
    v = set()
    L = len(queue)
    for _ in range(L):
        num = list(queue.popleft())

        for i, j in change:
            tmp = copy.deepcopy(num)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            tmp = ''.join(tmp)

            if tmp[0] != '0' and tmp not in v:
                v.add(tmp)
                queue.append(tmp)

n, k = input().split()
queue = deque([])

if len(n) > 1:
    change = list(combinations(range(len(n)), 2))
    queue.append(n)
    for _ in range(int(k)):
        bfs()

print(max(map(int, queue)) if queue else -1)