import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]

dp = []
for i in range(n):
    dp.append([0] * n)
    dp[i][i] = 1
    if i < n - 1 and arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, n):
    for j in range(n - i):
        k = i + j
        if arr[j] == arr[k] and dp[j + 1][k -1] == 1:
            dp[j][k] = 1

for s, e in q:
    print(dp[s - 1][e - 1])