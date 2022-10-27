c, n = map(int, input().split())
A, B = [], []
tmp = 0

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    tmp = max(tmp, b)

dp = [0] + [int(1e9)] * (c + tmp)

for i in range(n):
    for j in range(1, c + tmp + 1):
        dp[j] = min(dp[j], A[i] + dp[j - B[i]])

print(min(dp[c:]))