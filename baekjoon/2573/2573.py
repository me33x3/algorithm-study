import copy
from collections import deque

def bfs(i, j):
    tmp_board = copy.deepcopy(board)
    queue = deque([[i, j]])

    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if not tmp_board[mx][my]:
                    board[x][y] = max(board[x][y] - 1, 0)
                elif not v[mx][my]:
                    v[mx][my] = True
                    queue.append([mx, my])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
day = cnt = 0

while True:
    v = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] and not v[i][j]:
                v[i][j] = True
                bfs(i, j)
                cnt += 1

    if cnt != 1:
        break

    day += 1
    cnt = 0

print(day if cnt else 0)