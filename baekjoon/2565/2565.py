n = int(input())
pole = [list(map(int, input().split())) for _ in range(n)]
pole.sort(key=lambda x:x[0])

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if pole[i][1] > pole[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))