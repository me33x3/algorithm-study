def star(n, x, y):
    if n == 3:
        for i in range(3):
            for j in range(3):
                arr[x + i][y + j] = '*'
        arr[x + 1][y + 1] = ' '
        return

    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1):
                star(n // 3, x + i * (n // 3), y + j * (n // 3))

n = int(input())
arr = [[' '] * n for _ in range(n)]
star(n, 0, 0)

for line in arr:
    for ch in line:
        print(ch, end='')
    print()