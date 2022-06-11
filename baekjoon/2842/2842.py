from collections import deque

def bfs():
    queue = deque()
    cnt = 0

    if heights[left] <= altitude[px][py] <= heights[right]:
        queue.append([px, py])
        v = [[False] * n for _ in range(n)]
        v[px][py] = True

    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < n:
                if heights[left] <= altitude[mx][my] <= heights[right]:
                    if not v[mx][my]:
                        if village[mx][my] == 'K':
                            cnt += 1
                        v[mx][my] = True
                        queue.append([mx, my])

    return 1 if kcnt == cnt else 0

n = int(input())
village = [list(input()) for _ in range(n)]
altitude = [list(map(int, input().split())) for _ in range(n)]

px, py, kcnt = 0, 0, 0
heights = []

for i in range(n):
    for j in range(n):
        if village[i][j] == 'P':
            px, py = i, j
        elif village[i][j] == 'K':
            kcnt += 1
        heights.append(altitude[i][j])

heights = sorted(set(heights))

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
left, right = 0, 0
fatigue = int(1e9)

while left < len(heights) and right < len(heights):
    if bfs():
        fatigue = min(fatigue, heights[right] - heights[left])
        left += 1
    else:
        right += 1

print(fatigue)