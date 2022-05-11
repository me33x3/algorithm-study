n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
obj = []
for _ in range(n):
    obj.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = obj[i - 1]

        dp[i][j] = dp[i - 1][j]

        if w <= j:
            dp[i][j] = max(dp[i][j], v + dp[i - 1][j - w])

print(dp[n][k])