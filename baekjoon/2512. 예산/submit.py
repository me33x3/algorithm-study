N = int(input())
budget = sorted(map(int, input().split()))
M = int(input())

l, r = 0, budget[-1]
answer = 0

while l <= r:
    m = (l + r) // 2
    p = sum([b if b <= m else m for b in budget])

    if p <= M:
        l = m + 1
        answer = m
    else:
        r = m - 1

print(answer)