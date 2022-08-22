import sys
input = sys.stdin.readline

def fall(i):
    while dp[i]:
        x, y = dp[i][-1]
        if board[x][y] == '.':
            break
        dp[i].pop()

    col, row = dp[i].pop() if dp[i] else (0, i)

    while col < (R - 1) and board[col + 1][row] != 'X':
        dp[i].append([col, row])

        if board[col + 1][row] == '.':
            col += 1
        else:
            if row > 0 and board[col][row - 1] == '.' and board[col + 1][row - 1] == '.':
                col += 1
                row -= 1
            elif row < (C - 1) and board[col][row + 1] == '.' and board[col + 1][row + 1] == '.':
                col += 1
                row += 1
            else:
                break

    board[col][row] = 'O'

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
dp = [[] for _ in range(C)]

N = int(input())
for _ in range(N):
    fall(int(input()) - 1)

for row in board:
    print(''.join(row))