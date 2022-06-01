def dfs(x, y):
    global peak
    visited[x][y] = True

    for nx, ny in zip(dx, dy):
        mx, my = x + nx, y + ny

        if 0 <= mx < n and 0 <= my < m:
            if not visited[mx][my] and mountain[x][y] == mountain[mx][my]:
                dfs(mx, my)
            elif mountain[x][y] < mountain[mx][my]:
                peak = False

n, m = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            peak = True
            dfs(i, j)
            cnt += 1 if peak else 0

print(cnt)