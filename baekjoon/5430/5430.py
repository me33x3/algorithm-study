import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    p = list(input().rstrip())
    n = int(input())
    queue = deque(list(input().rstrip()[1:-1].split(',')))
    flag = 1

    if n == 0:
        queue = deque()

    try:
        for order in p:
            if order == 'R':
                flag *= -1
            else:
                if flag > 0:
                    queue.popleft()
                else:
                    queue.pop()
        print('[' + ','.join(list(queue)[::flag]) + ']')
    except IndexError:
        print('error')