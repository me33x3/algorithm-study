from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    v, k = 0, 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    visited[i][j] = 1
    if board[i][j] == 'v':
        v += 1
    elif board[i][j] == 'k':
        k += 1

    while queue:
        p, q = queue.popleft()

        for x, y in zip(dx, dy):
            mx, my = q + x, p + y

            if 0 <= mx < C and 0 <= my < R and board[my][mx] != '#' and not visited[my][mx]:
                queue.append([my, mx])
                visited[my][mx] = 1

                if board[my][mx] == 'v':
                    v += 1
                elif board[my][mx] == 'k':
                    k += 1

    if k > v:
        return [k, 0]
    else:
        return [0, v]

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and not visited[i][j]:
            cnt = bfs(i, j)
            sheep += cnt[0]
            wolf += cnt[1]

print(sheep, wolf)