from collections import deque

def bfs():
    dist[0][0] = 0
    queue = deque([[0, 0]])

    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx <= 500 and 0 <= my <= 500 and board[mx][my] < 2:
                if dist[mx][my] == -1:
                    if board[mx][my]:
                        dist[mx][my] = dist[x][y] + 1
                        queue.append([mx, my])
                    else:
                        dist[mx][my] = dist[x][y]
                        queue.appendleft([mx, my])

board = [[0] * 501 for _ in range(501)]
dist = [[-1] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = 1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = 2

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

bfs()
print(dist[500][500])