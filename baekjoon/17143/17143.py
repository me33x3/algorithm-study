import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d - 1, z]

change = [1, 0, 3, 2]
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
answer = 0

for i in range(C):
    tmp_board = [[0] * C for _ in range(R)]

    for j in range(R):
        if board[j][i] != 0:
            answer += board[j][i][-1]
            board[j][i] = 0
            break

    for y in range(R):
        for x in range(C):
            if board[y][x]:
                s, d, z = board[y][x]
                nx, ny = x, y

                for _ in range(s):
                    nx += dx[d]
                    ny += dy[d]

                    if not (0 <= ny < R) or not (0 <= nx < C):
                        d = change[d]
                        nx += dx[d] * 2
                        ny += dy[d] * 2

                if not tmp_board[ny][nx] or tmp_board[ny][nx][-1] < z:
                    tmp_board[ny][nx] = [s, d, z]

    board = tmp_board

print(answer)