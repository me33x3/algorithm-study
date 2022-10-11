from collections import deque


def check(x, y, k):
    return 0 <= x < w and 0 <= y < h and not board[y][x] and not v[y][x][k]


def bfs():
    q = deque([[0, 0, k, 0]])
    v[0][0][k] = 1

    while q:
        x, y, nk, m = q.popleft()

        if x == w - 1 and y == h - 1:
            return m

        if nk:
            for i in range(8):
                nx, ny = x + kx[i], y + ky[i]

                if check(nx, ny, nk - 1):
                    v[ny][nx][nk - 1] = 1
                    q.append([nx, ny, nk - 1, m + 1])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if check(nx, ny, nk):
                v[ny][nx][nk] = 1
                q.append([nx, ny, nk, m + 1])

    return -1


k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
v = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
kx, ky = [-2, -1, 1, 2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]

print(bfs())