def fill(i, j, n):
    if n == 3:
        star[i][j] = star[i + 1][j - 1] = star[i + 1][j + 1] = '*'
        for k in range(5):
            star[i + 2][j + k - 2] = '*'
        return

    tmp = n // 2
    fill(i, j, tmp)
    fill(i + tmp, j - tmp, tmp)
    fill(i + tmp, j + tmp, tmp)

n = int(input())
star = [[' '] * (2 * n) for _ in range(n)]
fill(0, n - 1, n)
for line in star:
    print(''.join(line))