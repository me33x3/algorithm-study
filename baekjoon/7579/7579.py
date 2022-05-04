n, m = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

val = sum(cost)
dp = [[0] * (val+1)for _ in range(n+1)]
answer = val

for i in range(1, n+1):
    b = byte[i - 1]
    c = cost[i-1]
    for j in range(1, val+1):
        if c > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], b + dp[i-1][j-c])

        if dp[i][j] >= m:
            answer = min(answer, j)

print(answer)