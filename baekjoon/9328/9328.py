from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def unlock():
    for i in range(r + 2):
        for j in range(c + 2):
            if board[i][j].lower() in keys:
                board[i][j] = '.'
    keys.clear()


def bfs():
    global cnt

    q = deque([[0, 0]])
    v = [[0] * (c + 2) for _ in range(r + 2)]
    v[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < (r + 2) and 0 <= ny < (c + 2) and not v[nx][ny]:
                if board[nx][ny] == '*':
                    continue
                elif board[nx][ny].isupper():
                    continue
                elif board[nx][ny].islower():
                    keys.append(board[nx][ny])
                elif board[nx][ny] == '$':
                    cnt += 1

                board[nx][ny] = '.'
                v[nx][ny] = 1
                q.append([nx, ny])


for _ in range(int(input())):
    r, c = map(int, input().split())

    board = [['.'] * (c + 2)]

    for _ in range(r):
        board.append(['.'] + list(input()) + ['.'])
    board.append(['.'] * (c + 2))

    keys = list(input())
    cnt = 0

    while keys:
        if keys[0] == '0':
            keys.clear()
        else:
            unlock()
        bfs()

    print(cnt)