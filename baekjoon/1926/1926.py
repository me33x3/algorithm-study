from collections import deque

def bfs(i, j):
    area = 1
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if draw[mx][my] == 1 and not v[mx][my]:
                    area += 1
                    v[mx][my] = True
                    queue.append([mx, my])

    return area

n, m = map(int, input().split())
draw = [list(map(int, input().split())) for _ in range(n)]
v = [[False] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

cnt, area = 0, 0
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1 and not v[i][j]:
            v[i][j] = True
            area = max(area, bfs(i, j))
            cnt += 1

print(cnt)
print(area)