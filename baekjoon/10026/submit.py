def dfs(n, m):
    stack = [[n, m]]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while stack:
        n, m = stack.pop()
        for x, y in zip(dx, dy):
            mx, my = m + x, n + y
            if 0 <= mx < N and 0 <= my < N:
                if not visited[my][mx] and img[n][m] == img[my][mx]:
                    stack.append([my, mx])
                    visited[my][mx] = 1

N = int(input())
imgs = []
imgs.append([list(input()) for _ in range(N)])
imgs.append([['R' if c == 'G' else c for c in line] for line in imgs[0]])

for img in imgs:
    visited = [[0] * N for _ in range(N)]
    part = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j)
                part += 1
    print(part, end=' ')