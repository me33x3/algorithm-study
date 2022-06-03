from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < n and not visited[mx][my]:
                visited[mx][my] = True
                queue.append([mx, my])

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
m = max(map(max, matrix))
cnt = 0

for num in range(0, m):
    visited = []
    tmp = 0
    for i in range(n):
        visited.append([])
        for j in range(n):
            visited[i].append(False if matrix[i][j] > num else True)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                tmp += 1

    cnt = max(cnt, tmp)

print(cnt)