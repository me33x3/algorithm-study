dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    grid[y][x] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for c in curve:
        x += dx[c]
        y += dy[c]
        grid[y][x] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            answer += 1

print(answer)