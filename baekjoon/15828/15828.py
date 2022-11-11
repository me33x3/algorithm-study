import sys
from collections import deque

input = sys.stdin.readline

size = int(input())
q = deque()

while 1:
    data = int(input())

    if data == -1:
        break
    elif data == 0:
        q.popleft()
    elif len(q) < size:
        q.append(data)

if q:
    print(*q)
else:
    print('empty')