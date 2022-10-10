from collections import deque


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def spread():
    L = len(fq)

    for _ in range(L):
        y, x = fq.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == '.':
                board[ny][nx] = '*'
                fq.append([ny, nx])


def bfs():
    move = 1

    while q:
        spread()
        L = len(q)

        for _ in range(L):
            y, x = q.popleft()

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]

                if 0 <= ny < h and 0 <= nx < w:
                    if board[ny][nx] == '.' and not v[ny][nx]:
                        v[ny][nx] = 1
                        q.append([ny, nx])
                else:
                    return move

        move += 1

    return 'IMPOSSIBLE'


for _ in range(int(input())):
    w, h = map(int, input().split())

    board = []
    v = [[0] * w for _ in range(h)]
    q, fq = deque([]), deque([])

    for i in range(h):
        board.append(list(input()))

        for j in range(w):
            if board[i][j] == '@':
                q.append([i, j])
                board[i][j] = '.'
                v[i][j] = 1
            elif board[i][j] == '*':
                fq.append([i, j])

    print(bfs())