n = int(input())
k = int(input())

l, r = 1, k
answer = 0
while l <= r:
    m = (l + r) // 2

    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, m // i)

    if cnt >= k:
        r = m - 1
        answer = m
    else:
        l = m + 1

print(answer)