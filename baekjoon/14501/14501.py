N = int(input())
T, P = [], []
dp = [0] * (N + 1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    if T[i] + i <= N:
        dp[i] = max(dp[i + 1], P[i] + dp[T[i] + i])
    else:
        dp[i] = dp[i + 1]

print(dp[0])