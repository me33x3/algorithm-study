def check(n):
    for i in range(3):
        if n == v[i][0] == v[i][1] == v[i][2]:
            return True
        if n == v[0][i] == v[1][i] == v[2][i]:
            return True

    if n == v[0][0] == v[1][1] == v[2][2]:
        return True
    if n == v[0][2] == v[1][1] == v[2][0]:
        return True

    return False


def backtracking(depth):
    n = 2 if depth % 2 else 1
    nn = 1 if depth % 2 else 2

    if depth == 9 or (depth == 9 - cnt[0] and check(nn)):
        return True

    if check(nn):
        return False

    for i in range(3):
        for j in range(3):
            if n == board[i][j] and not v[i][j]:
                v[i][j] = n
                if backtracking(depth + 1):
                    return True
                v[i][j] = 0

    return False


while True:
    line = input()

    if line == 'end':
        break

    board = []
    cnt = [0] * 3

    for i in range(3):
        board.append([])
        for j in range(3):
            ch = line[i * 3 + j]
            if ch == '.':
                board[i].append(0)
                cnt[0] += 1
            elif ch == 'X':
                board[i].append(1)
                cnt[1] += 1
            else:
                board[i].append(2)
                cnt[2] += 1

    v = [[0] * 3 for _ in range(3)]
    print('valid' if backtracking(0) else 'invalid')