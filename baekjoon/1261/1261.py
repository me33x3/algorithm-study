from collections import deque

def bfs():
    dist[0][0] = 0
    queue = deque([[0, 0]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if dist[mx][my] == -1:
                    if board[mx][my] == 1:
                        dist[mx][my] = dist[x][y] + 1
                        queue.append([mx, my])
                    else:
                        dist[mx][my] = dist[x][y]
                        queue.appendleft([mx, my])

m, n = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dist = [[-1] * m for _ in range(n)]
bfs()
print(dist[n - 1][m - 1])