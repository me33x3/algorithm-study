from copy import deepcopy

dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sx, sy, score, board, pos):
    global max_score

    sa, sb = board[sx][sy]
    pos[sa] = 0
    board[sx][sy][0] = 0
    score += sa
    max_score = max(max_score, score)

    # move fish
    for a in range(1, 17):
        if not pos[a]:
            continue

        x, y = pos[a]
        b = board[x][y][1]

        while True:
            nx, ny = x + dx[b], y + dy[b]

            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                board[x][y], board[nx][ny] = board[nx][ny], [a, b]

                if board[x][y][0]:
                    pos[board[x][y][0]] = [x, y]

                pos[a] = [nx, ny]
                break

            b = b + 1 if b < 8 else 1

    # move shark
    for i in range(1, 4):
        nx, ny = sx + dx[sb] * i, sy + dy[sb] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0]:
            dfs(nx, ny, score, deepcopy(board), deepcopy(pos))

board, pos = [], [0] * 17
max_score = 0

for i in range(4):
    board.append([])
    row = list(map(int, input().split()))

    for j in range(4):
        a, b = row[j * 2], row[j * 2 + 1]
        board[-1].append([a, b])
        pos[a] = [i, j]

dfs(0, 0, 0, board, pos)
print(max_score)