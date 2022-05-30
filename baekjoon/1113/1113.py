from collections import deque

def bfs(i, j, num):
    cnt = 1
    visited[i][j] = True
    wall = False
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m:
                if not visited[mx][my] and pool[mx][my] <= num:
                    visited[mx][my] = True
                    queue.append([mx, my])
                    cnt += 1
            else:
                wall = True

    return 0 if wall else cnt

n, m = map(int, input().split())
pool = [list(map(int, list(input()))) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0

for num in range(1, 9):
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if pool[i][j] <= num and not visited[i][j]:
                answer += bfs(i, j, num)

print(answer)