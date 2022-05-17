from copy import deepcopy

def und(board, d):
    start, end = (1, n) if d == 1 else (n - 2, -1)

    for j in range(n):
        k = 0 if d == 1 else n - 1
        for i in range(start, end, d):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[k][j] == 0:
                    board[k][j] = tmp
                elif board[k][j] == tmp:
                    board[k][j] *= 2
                    k += d
                else:
                    k += d
                    board[k][j] = tmp
    return board

def lnr(board, d):
    start, end = (1, n) if d == 1 else (n - 2, -1)

    for i in range(n):
        k = 0 if d == 1 else n - 1
        for j in range(start, end, d):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][k] == 0:
                    board[i][k] = tmp
                elif board[i][k] == tmp:
                    board[i][k] *= 2
                    k += d
                else:
                    k += d
                    board[i][k] = tmp
    return board

def dfs(board, cnt):
    global answer

    if cnt == 5:
        answer = max(answer, max(map(max, board)))
        return

    for d in (1, -1):
        dfs(und(deepcopy(board), d), cnt + 1)
        dfs(lnr(deepcopy(board), d), cnt + 1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(board, 0)
print(answer)