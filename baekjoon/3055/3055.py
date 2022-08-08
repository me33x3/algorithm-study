from collections import deque

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def flood():
    L = len(water)

    for _ in range(L):
        r, c = water.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == '.':
                water.append([nr, nc])
                board[nr][nc] = '*'

def move():
    while queue:
        flood()

        L = len(queue)
        for _ in range(L):
            r, c = queue.popleft()

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    if board[nr][nc] == 'D':
                        return visited[r][c]
                    elif board[nr][nc] == '.':
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append([nr, nc])

    return 'KAKTUS'

R, C = map(int, input().split())

board, visited = [], []
queue, water = deque(), deque()

for i in range(R):
    board.append(list(input()))
    visited.append([0] * C)

    for j in range(C):
        if board[i][j] == 'S':
            queue.append([i, j])
            board[i][j] = '.'
            visited[i][j] = 1
        elif board[i][j] == '*':
            water.append([i, j])

print(move())