dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y, depth, score):
    global max_score

    if depth == 4:
        max_score = max(max_score, score)
        return

    if max_score >= score + max_val * (4 - depth):
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
            v[nx][ny] = 1

            if depth == 2:
                dfs(x, y, depth + 1, score + board[nx][ny])

            dfs(nx, ny, depth + 1, score + board[nx][ny])
            v[nx][ny] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

v = [[0] * m for _ in range(n)]
max_val = max(map(max, board))
max_score = 0

for r in range(n):
    for c in range(m):
        v[r][c] = 1
        dfs(r, c, 1, board[r][c])
        v[r][c] = 0

print(max_score)