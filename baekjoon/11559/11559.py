from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def fall():
    for j in range(6):
        i, t = 11, 0
        while i >= 0:
            if board[i][j] != '.':
                if t:
                    k = i
                    while k >= 0 and board[k][j] != '.':
                        board[k + t][j], board[k][j] = board[k][j], '.'
                        k -= 1
                    i += t
                    t = 0
            else:
                t += 1
            i -= 1

def bfs(i, j):
    target, pop = board[i][j], []
    queue = deque([[i, j]])

    while queue:
        x, y = queue.popleft()
        pop.append([x, y])

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == target:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

    if len(pop) < 4:
        return False
    else:
        while pop:
            x, y = pop.pop(0)
            board[x][y] = '.'
        return True

board = [list(input()) for _ in  range(12)]
answer = 0

while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                visited[i][j] = 1
                if bfs(i, j):
                    flag = True

    if flag:
        answer += 1
        fall()
    else:
        break

print(answer)