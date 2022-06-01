from collections import deque

def bfs(i, j, pattern):
    visited[i][j] = True
    dx = [0, 0] if pattern == '-' else [1, -1]
    dy = [1, -1] if pattern == '-' else [0, 0]
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if not visited[mx][my] and room[mx][my] == pattern:
                    visited[mx][my] = True
                    queue.append([mx, my])

n, m = map(int, input().split())
room = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j, room[i][j])
            cnt += 1

print(cnt)