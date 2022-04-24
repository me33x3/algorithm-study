dp = [0, 1, 2, 4]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp[n])