N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

answer = 0
for coin in coins[::-1]:
    t = K // coin
    if t > 0:
        K -= coin * t
        answer += t

print(answer)