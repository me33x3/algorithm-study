from collections import deque

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque([[sx, sy, sz]])
    v = [[[0] * C for _ in range(R)] for _ in range(L)]
    v[sz][sx][sy] = 1

    while q:
        x, y, z = q.popleft()

        # print(x, y, z)

        if x == ex and y == ey and z == ez:
            return v[z][x][y]

        for d in range(6):
            nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]

            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and board[nz][nx][ny] == '.' and not v[nz][nx][ny]:
                v[nz][nx][ny] = v[z][x][y] + 1
                q.append([nx, ny, nz])

    return -1


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    board = []
    sx, sy, sz = 0, 0, 0
    ex, ey, ez = 0, 0, 0

    for k in range(L):
        board.append([])
        for i in range(R):
            board[k].append(list(input()))

            for j in range(C):
                if board[k][i][j] == 'S':
                    sx, sy, sz = i, j, k
                    board[k][i][j] = '.'
                elif board[k][i][j] == 'E':
                    ex, ey, ez = i, j, k
                    board[k][i][j] = '.'

        input()

    sec = bfs()
    print('Escaped in ' + str(sec-1) + ' minute(s).' if sec > 0 else 'Trapped!')