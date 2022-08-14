dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def turn(dir):
    global dice
    a, b, c, d, e, f = dice

    if dir == 1:
        dice = [d, b, a, f, e, c]
    elif dir == 2:
        dice = [c, b, f, a, e, d]
    elif dir == 3:
        dice = [e, a, c, d, f, b]
    else:
        dice = [b, f, c, d, a, e]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 6

for i in list(map(int, input().split())):
    x += dx[i-1]
    y += dy[i-1]

    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i-1]
        y -= dy[i-1]
        continue

    turn(i)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0

    print(dice[0])