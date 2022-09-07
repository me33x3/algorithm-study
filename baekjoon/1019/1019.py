n = int(input())
cnt = [0] * 10
d = 1

while n >= 10:
    while n % 10 != 9:
        for ch in str(n):
            cnt[int(ch)] += d
        n -= 1

    nn = n // 10

    for i in range(10):
        cnt[i] += (nn + 1) * d

    cnt[0] -= d
    d *= 10
    n = nn

for i in range(1, n+1):
    cnt[i] += d

print(*cnt)