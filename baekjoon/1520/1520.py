import sys
sys.setrecursionlimit(10 ** 6)


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] < 0:
        dp[x][y] = 0

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < m and 0 <= ny < n:
                if board[x][y] > board[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))