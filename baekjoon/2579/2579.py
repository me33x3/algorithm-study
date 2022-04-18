N = int(input())
stairs, dp = [], []
for i in range(N):
    stairs.append(int(input()))

dp.append(stairs[0])
if len(stairs) > 1:
    dp.append(stairs[0] + stairs[1])
if len(stairs) > 2:
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

for i in range(3, N):
    dp.append(max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]))


print(dp[-1])