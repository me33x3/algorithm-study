MAX = 1000000
prime = [False, False] + [True] * (MAX - 1)

for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i , MAX + 1, i):
            prime[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    x, y = 2, n - 2

    while x <= y:
        if prime[x] and prime[y]:
            print(n, '=', x, '+', y)
            break
        x += 1
        y -= 1

    if x > y:
        print('Goldbach\'s conjecture is wrong.')