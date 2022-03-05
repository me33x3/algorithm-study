prime = [False, False] + [True] * 9999

for i in range(2, int(10000 ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, 10001, i):
            prime[j] = False

for _ in range(int(input())):
    n = int(input())

    mid = n // 2
    x, y = mid, mid

    for _ in range(mid):
        if prime[x] and prime[y]:
            print(x, y)
            break
        x -= 1
        y += 1