import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    cnt = 1
    wall = []
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny
            if 0 <= mx < n and 0 <= my < m and not v[mx][my]:
                v[mx][my] = True

                if not board[mx][my]:
                    cnt += 1
                    queue.append((mx, my))
                else:
                    wall.append((mx, my))

    for x, y in wall:
        v[x][y] = False
        board[x][y] += cnt

n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
v = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not board[i][j] and not v[i][j]:
            v[i][j] = True
            bfs(i, j)

for i in range(n):
    for j in range(m):
        print(board[i][j] % 10, end='')
    print()