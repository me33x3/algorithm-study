n = int(input())
m = 2 * n - 1
star = [[' '] * m for _ in range(m)]

for i in range(n):
    for j in range(m - (i * 2)):
        star[i][i + j] = '*'
        star[-(i + 1)][i + j] = '*'

for line in star:
    print(''.join(line).rstrip())