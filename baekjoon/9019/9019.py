import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    queue = deque([[a, '']])
    v = [False] * 10001
    v[a] = True

    while queue:
        n, orders = queue.popleft()

        for o in ['D', 'S', 'L', 'R']:
            if o == 'D':
                temp = n * 2 % 10000
            elif o == 'S':
                temp = (n - 1) % 10000
            elif o == 'L':
                temp = n // 1000
                temp = n % 1000 * 10 + temp
            elif o == 'R':
                temp = n % 10
                temp = n // 10 + 1000 * temp

            if temp == b:
                return orders + o

            if not v[temp]:
                queue.append([temp, orders + o])
                v[temp] = True

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))