n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(2, n):
    if not board[0][i]:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        if not board[r][c]:
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

            if not board[r][c - 1] and not board[r - 1][c]:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))