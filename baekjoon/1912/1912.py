n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]
for i in range(1, n):
    dp.append(max(dp[i - 1] + A[i], A[i]))

print(max(dp))