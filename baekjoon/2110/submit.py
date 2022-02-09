import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

l, r = 1, houses[-1] - houses[0]
while l <= r:
    m = (l + r) // 2
    curr, cnt = houses[0], 1

    for i in range(1, N):
        if houses[i] - curr >= m:
            curr = houses[i]
            cnt += 1

    if C <= cnt:
        l = m + 1
    else:
        r = m - 1

print(r)