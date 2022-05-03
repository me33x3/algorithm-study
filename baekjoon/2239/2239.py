import sys
input = sys.stdin.readline

def check(i, j):
    a, b = i // 3 * 3, j // 3 * 3
    for p in range(a, a + 3):
        for q in range(b, b + 3):
            if i == p and j == q:
                continue
            if board[i][j] == board[p][q]:
                return False

    for k in range(9):
        if i != k and board[i][j] == board[k][j]:
            return False
        if j != k and board[i][j] == board[i][k]:
            return False

    return True

def dfs(idx):
    if idx == len(zero_loc):
        for line in board:
            print(*line, sep='')
        sys.exit()

    i, j = zero_loc[idx]

    for num in range(1, 10):
        board[i][j] = num
        if check(i, j):
            dfs(idx + 1)
        board[i][j] = 0

board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zero_loc = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_loc.append([i, j])
dfs(0)