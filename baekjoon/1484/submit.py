G = int(input())

sq = [i ** 2 for i in range(1, (G + 1) // 2 + 1)]
l, r = 0, 1
cnt = 0
while r < len(sq):
    res = sq[r] - sq[l]
    if res == G:
        print(int(sq[r] ** 0.5))
        l += 1
        r += 1
        cnt += 1
    elif res < G:
        r += 1
    else:
        l += 1

if cnt == 0:
    print(-1)