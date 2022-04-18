K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

l, r = 1, max(cables)

while l <= r:
    m = (l + r) // 2
    cnt = sum([cable // m for cable in cables])

    if cnt >= N:
        l = m + 1
    else:
        r = m - 1

print(r)