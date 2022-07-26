board = [list(map(int, input().split())) for _ in range(19)]

dx, dy = [0, 1, 1, -1], [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y]:
            stone = board[x][y]

            for d in range(4):
                cnt = 1
                nx, ny = x + dx[d], y + dy[d]
                tx, ty = x - dx[d], y - dy[d]

                flag = True if 0 <= tx < 19 and 0 <= ty < 19 and stone == board[tx][ty] else False

                while 0 <= nx < 19 and 0 <= ny < 19 and stone == board[nx][ny]:
                    cnt += 1

                    if cnt > 5:
                        break

                    nx += dx[d]
                    ny += dy[d]

                if cnt == 5 and not flag:
                    print(stone)
                    print(x + 1, y + 1)
                    exit()
print(0)