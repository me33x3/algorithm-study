from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def spread():
    L = len(fq)

    for _ in range(L):
        x, y = fq.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
                board[nx][ny] = 'F'
                fq.append([nx, ny])


def bfs():
    sec = 1

    while q:
        L = len(q)
        spread()

        for _ in range(L):
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == '.' and not v[nx][ny]:
                        v[nx][ny] = 1
                        q.append([nx, ny])
                else:
                    return sec

        sec += 1

    return 'IMPOSSIBLE'


r, c = map(int, input().split())
board = []

q, fq = deque(), deque()
v = [[0] * c for _ in range(r)]

for i in range(r):
    board.append(list(input()))

    for j in range(c):
        if board[i][j] == 'J':
            board[i][j] = '.'
            v[i][j] = 1
            q.append([i, j])
        elif board[i][j] == 'F':
            fq.append([i, j])

print(bfs())