from collections import deque

def bfs():
    t = 0
    queue = deque([[ax, ay]])
    visited = [[0] * n for _ in range(m)]
    visited[ax][ay] = 1

    while queue:
        t += 1
        L = len(queue)

        for _ in range(L):
            x, y = queue.popleft()

            for d in range(4):
                mx, my = x + dx[d], y + dy[d]

                if 0 <= mx < m and 0 <= my < n and not visited[mx][my]:
                    ch = board[mx][my]

                    if ch == '.':
                        continue
                    elif ch == '#':
                        visited[mx][my] = 1
                        queue.append([mx, my])
                    elif "0" <= ch <= "9":
                        if 0 <= d <= 1:
                            if rotaries[ch][0] == '|':
                                visited[mx][my] = 1
                                queue.append([mx, my])
                            else:
                                queue.append([x, y])
                        else:
                            if rotaries[ch][0] == '-':
                                visited[mx][my] = 1
                                queue.append([mx, my])
                            else:
                                queue.append([x, y])
                    else:
                        return t

        for i in rotaries.keys():
            rotaries[i][-1] += 1

            if rotaries[i][0] == '-':
                if rotaries[i][-1] > rotaries[i][1]:
                    rotaries[i][0] = '|'
                    rotaries[i][-1] = 1
            else:
                if rotaries[i][-1] > rotaries[i][2]:
                    rotaries[i][0] = '-'
                    rotaries[i][-1] = 1

    return "impossible"

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    board = []
    ax, ay = 0, 0
    bx, by = 0, 0

    for i in range(m):
        board.append(list(input()))

        for j in range(n):
            if board[i][j] == 'A':
                ax, ay = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    rotaries = {}
    while True:
        rotary = input().rstrip().split()

        if rotary:
            rotaries[rotary[0]] = [rotary[1], int(rotary[2]), int(rotary[3]), 1]
        else:
            break

    print(bfs())