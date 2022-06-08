import sys
from collections import deque
input = sys.stdin.readline

def melt():
    nextq = deque()

    while meltq:
        x, y = meltq.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < r and 0 <= my < c:
                if lake[mx][my] == 'X':
                    nextq.append([mx, my])
                    lake[mx][my] = '.'

    return nextq

def meet():
    while meetq:
        x, y = meetq.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < r and 0 <= my < c and not v[mx][my]:
                if mx == swan[1][0] and my == swan[1][1]:
                    return True

                if lake[mx][my] != 'X':
                    meetq.append([mx, my])
                else:
                    meetq_tmp.append([mx, my])

                v[mx][my] = True

    return False

r, c = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(r)]

swan = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

v = [[False] * c for _ in range(r)]

meltq = deque()
meetq, meetq_tmp = deque(), deque()

for i in range(r):
    for j in range(c):
        if lake[i][j] != 'X':
            meltq.append([i, j])

            if lake[i][j] == 'L':
                if swan:
                    meetq.append([swan[0][0], swan[0][1]])
                    v[swan[0][0]][swan[0][1]] = True
                swan.append([i, j])

day = 1
while True:
    meltq = melt()

    if meet():
        print(day)
        break

    day += 1
    meetq, meetq_tmp = meetq_tmp, deque()
