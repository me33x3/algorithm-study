n = int(input())

dp = [[0] * 3 for _ in range(2)]
tmp = [[0] * 3 for _ in range(2)]

for _ in range(n):
    a, b, c = map(int, input().split())

    tmp[0][0] = a + max(dp[0][0], dp[0][1])
    tmp[1][0] = a + min(dp[1][0], dp[1][1])

    tmp[0][1] = b + max(dp[0])
    tmp[1][1] = b + min(dp[1])

    tmp[0][2] = c + max(dp[0][1], dp[0][2])
    tmp[1][2] = c + min(dp[1][1], dp[1][2])

    for i in range(3):
        dp[0][i] = tmp[0][i]
        dp[1][i] = tmp[1][i]

print(max(dp[0]), min(dp[1]))