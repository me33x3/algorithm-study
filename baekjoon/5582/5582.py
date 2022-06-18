a, b = input(), input()
n, m = len(a), len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]
answer = 0

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])

print(answer)