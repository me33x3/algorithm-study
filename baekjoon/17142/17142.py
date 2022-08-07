import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
inf = sys.maxsize

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(active):
    v = [[-1] * N for _ in range(N)]
    queue = deque()
    res = 0

    for x, y in active:
        queue.append([x, y])
        v[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < N and 0 <= my < N and board[mx][my] != 1:
                if v[mx][my] < 0:
                    v[mx][my] = v[x][y] + 1
                    queue.append([mx, my])

                    if board[mx][my] == 0:
                        res = max(res, v[mx][my])

    return res if list(sum(v, [])).count(-1) == wall_cnt else inf

N, M = map(int, input().split())

board, virus = [], []
answer,wall_cnt = inf, 0

for i in range(N):
    board.append(list(map(int, input().split())))

    for j in range(N):
        if board[i][j] == 1:
            wall_cnt += 1
        elif board[i][j] == 2:
            virus.append([i, j])

for active in combinations(virus, M):
    answer = min(answer, bfs(active))

print(answer if answer != inf else -1)