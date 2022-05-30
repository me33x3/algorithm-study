import sys
from collections import deque

INF = sys.maxsize

def bfs():
    visited = [[[[[False] * 2 for _ in range(2)] for _ in range(4)] for _ in range(m)] for _ in range(n)]
    queue = deque([[pos[0], pos[1], -1, 0, 0, 0]])
    while queue:
        x, y, curr, c1, c2, sec = queue.popleft()

        for d in range(4):
            if curr == d:
                continue

            mx, my = x + dx[d], y + dy[d]
            mc1, mc2 = c1, c2

            if 0 <= mx < n and 0 <= my < m and not visited[mx][my][d][mc1][mc2]:
                if board[mx][my] != '#':
                    if board[mx][my] == 'C1':
                        mc1 = 1
                    elif board[mx][my] == 'C2':
                        mc2 = 1

                    if mc1 and mc2:
                        return sec + 1

                    queue.append([mx, my, d, mc1, mc2, sec + 1])
                    visited[mx][my][d][mc1][mc2] = True

    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
pos, cflag = [], False
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            pos = [i, j]
        if board[i][j] == 'C':
            if cflag:
                board[i][j] = 'C2'
            else:
                board[i][j] = 'C1'
                cflag = True

print(bfs())