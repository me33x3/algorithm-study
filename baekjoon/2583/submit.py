from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(i, j):
    queue = deque([[j, i]])
    res = 1

    while queue:
        x, y = queue.popleft()

        for tx, ty in zip(dx, dy):
            mx, my = x + tx, y + ty

            if 0 <= mx < n and 0 <= my < m:
                if not board[my][mx] and not visited[my][mx]:
                    visited[my][mx] = True
                    queue.append([mx, my])
                    res += 1

    return res

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

visited = [[False] * n for _ in range(m)]
areas = []
for i in range(m):
    for j in range(n):
        if not board[i][j] and not visited[i][j]:
            visited[i][j] = True
            areas.append(bfs(i, j))

areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))