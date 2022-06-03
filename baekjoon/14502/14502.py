import copy
from collections import deque

def spread():
    global answer

    tmp_lab = copy.deepcopy(lab)

    queue = deque([])
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny

            if 0 <= mx < n and 0 <= my < m and tmp_lab[mx][my] == 0:
                tmp_lab[mx][my] = 2
                queue.append([mx, my])

    cnt = 0
    for line in tmp_lab:
        cnt += line.count(0)

    answer = max(answer, cnt)

def build(cnt):
    if cnt == 3:
        spread()
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build(cnt + 1)
                lab[i][j] = 0

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0
build(0)
print(answer)