n = int(input())
S = list(map(int, input().split()))
S_r = S[::-1]

dp = [0 for _ in range(n)]
dp_r = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if S[i] > S[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
        if S_r[i] > S_r[j] and dp_r[i] < dp_r[j]:
            dp_r[i] = dp_r[j]
    dp[i] += 1
    dp_r[i] += 1

print(max([sum(x) - 1 for x in zip(dp, dp_r[::-1])]))