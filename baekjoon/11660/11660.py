import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
coords = [list(map(int, input().split())) for _ in range(m)]

dp = []
for i in range(n):
    dp.append([board[i][0]])
    for j in range(1, n):
        dp[i].append(dp[i][j-1] + board[i][j])

for x1, y1, x2, y2 in coords:
    res = 0
    for i in range(x1-1, x2):
        res += dp[i][y2-1]
        if y1 > 1:
            res -= dp[i][y1 - 2]
    print(res)