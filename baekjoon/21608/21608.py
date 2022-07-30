n = int(input())

score = [0, 1, 10, 100, 1000]
board = [[0] * n for _ in range(n)]
graph = dict()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n ** 2):
    temp = list(map(int, input().split()))
    s = temp[0]
    graph[s] = set(temp[1:])

    l = []
    blank = [[0] * n for _ in range(n)]
    max_ = 0

    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                cnt = 0

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in graph[s]:
                            cnt += 1

                        if not board[nx][ny]:
                            blank[x][y] += 1

                if cnt > max_:
                    max_ = cnt
                    l = [[x, y]]
                elif cnt == max_:
                    l.append([x, y])

    if len(l) != 1:
        max_ = 0

        tmp_l = []
        for x, y in l:
            if blank[x][y] > max_:
                max_ = blank[x][y]
                tmp_l = [[x, y]]
            elif blank[x][y] == max_:
                tmp_l.append([x, y])

        l = tmp_l

    board[l[0][0]][l[0][1]] = s

answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in graph[board[x][y]]:
                cnt += 1

        answer += score[cnt]

print(answer)