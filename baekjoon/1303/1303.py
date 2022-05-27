from collections import deque

def bfs(i, j):
    color = ground[i][j]
    queue = deque([[i, j]])
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if ground[my][mx] == color and not v[my][mx]:
                    v[my][mx] = True
                    queue.append([my, mx])
                    cnt += 1

    return cnt

n, m = map(int, input().split())
ground = [list(input()) for _ in range(m)]

power = dict(zip(['W', 'B'], [0, 0]))
v = [[False] * n for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(m):
    for j in range(n):
        if not v[i][j]:
            v[i][j] = True
            power[ground[i][j]] += bfs(i, j) ** 2

print(power['W'], power['B'])