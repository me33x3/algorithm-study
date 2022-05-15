def check(num, x, y):
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            if sudoku[i][j] == num:
                return False

    for k in range(9):
        if sudoku[x][k] == num or sudoku[k][y] == num:
            return False

    return True

def solve(idx):
    if idx == len(zero_loc):
        for line in sudoku:
            print(' '.join(map(str, line)))
        exit()

    x, y = zero_loc[idx]
    for num in range(1, 10):
        if check(num, x, y):
            sudoku[x][y] = num
            solve(idx + 1)
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]

zero_loc = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_loc.append([i, j])

solve(0)