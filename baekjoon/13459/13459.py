from collections import deque

def move(x, y, d):
    cnt = 0
    while board[x][y] != 'O' and board[x + dx[d]][y + dy[d]] != '#':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt

def bfs():
    queue = deque([pos + [1]])

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10:
            return 0

        for i in range(4):
            mrx, mry, rcnt = move(rx, ry, i)
            mbx, mby, bcnt = move(bx, by, i)

            if board[mbx][mby] != 'O':
                if board[mrx][mry] == 'O':
                    return 1

                if mrx == mbx and mry == mby:
                    if rcnt < bcnt:
                        mbx -= dx[i]
                        mby -= dy[i]
                    else:
                        mrx -= dx[i]
                        mry -= dy[i]

                if not v[mrx][mry][mbx][mby]:
                    queue.append([mrx, mry, mbx, mby, cnt + 1])

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
v = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

pos = [0, 0, 0, 0]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            pos[0], pos[1] = i, j
        elif board[i][j] == 'B':
            pos[2], pos[3] = i, j

print(bfs())