import sys
input = sys.stdin.readline

n = int(input())
T, P = [], []
dp = [0] * (n + 1)

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(n - 1, -1, -1):
    if T[i] + i <= n:
        dp[i] = max(dp[i + 1], P[i] + dp[T[i] + i])
    else:
        dp[i] = dp[i + 1]

print(dp[0])