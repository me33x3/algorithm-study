import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    v = [[[False] * m for _ in range(n)] for _ in range(2)]
    v[0][0][0] = True
    v[1][0][0] = True

    queue = deque([[0, 0, 0, 1]])
    while queue:
        cx, cy, b, cnt = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return cnt

        for x, y in zip(dx, dy):
                mx = x + cx
                my = y + cy

                if 0 <= mx < n and 0 <= my < m and not v[b][mx][my]:
                    if board[mx][my] == '0':
                        queue.append([mx, my, b, cnt + 1])
                        v[b][mx][my] = True
                    else:
                        if b == 0:
                            queue.append([mx, my, 1, cnt + 1])
                            v[1][mx][my] = True

    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
print(bfs())