import sys
INF = sys.maxsize

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    min_val = INF
    for j in range(1, int(i ** 0.5) + 1):
        min_val = min(min_val, dp[i - (j ** 2)])
    dp[i] = min_val + 1

print(dp[n])