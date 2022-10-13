from collections import deque


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def chk(x, y):
    return 0 <= x < n and 0 <= y < m and not board[x][y] and not v[x][y]


def bfs():
    while q:
        x, y, nl, nr = q.popleft()

        for d in range(2):
            nx, ny = x + dx[d], y + dy[d]
            while chk(nx, ny):
                v[nx][ny] = 1
                q.append((nx, ny, nl, nr))
                nx += dx[d]
                ny += dy[d]

        if nl:
            nx, ny = x + dx[2], y + dy[2]
            if chk(nx, ny):
                v[nx][ny] = 1
                q.append((nx, ny, nl - 1, nr))

        if nr:
            nx, ny = x + dx[3], y + dy[3]
            if chk(nx, ny):
                v[nx][ny] = 1
                q.append((nx, ny, nl, nr - 1))

    return sum(map(sum, v))


n, m = map(int, input().split())
l, r = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append((i, j, l, r))
            board[i][j] = 0
            v[i][j] = 1
            break
    if q:
        break

print(bfs())