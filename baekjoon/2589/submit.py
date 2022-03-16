from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(r, c):
    visited = [[False] * w for _ in range(h)]
    queue = deque([[r, c, 0]])
    visited[r][c] = True
    res = 0

    while queue:
        n, m, move = queue.popleft()
        res = max(res, move)

        for x, y in zip(dx, dy):
            mx, my = x + m, y + n

            if 0 <= mx < w and 0 <= my < h:
                if board[my][mx] == 'L' and not visited[my][mx]:
                    visited[my][mx] = True
                    queue.append([my, mx, move + 1])

    return res

h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
answer = 0

for i in range(h):
    for j in range(w):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)