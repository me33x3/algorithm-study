M = int(input())
N = int(input())

res = []
for i in range(int(M ** 0.5), int(N ** 0.5) + 1):
    if M <= i ** 2 <= N:
        res.append(i ** 2)

if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)