from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def numbering(r, c):
    q = deque([[r, c]])
    v[r][c] = 1
    board[r][c] = num

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] and not v[nx][ny]:
                v[nx][ny] = 1
                board[nx][ny] = num
                q.append([nx, ny])


def bfs(num):
    q = deque([])
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == num:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and dist[nx][ny] < 0:
                    q.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

                if board[nx][ny] > 0 and board[nx][ny] != num:
                    return dist[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
num = 2
answer = n ** 2

for i in range(n):
    for j in range(n):
        if board[i][j] and not v[i][j]:
            numbering(i, j)
            num += 1

for i in range(2, num):
    answer = min(answer, bfs(i))

print(answer)