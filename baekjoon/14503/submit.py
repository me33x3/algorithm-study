from collections import deque

n, m = map(int, input().split())
robot = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
clean = [[False] * m for _ in range(n)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = 0
queue = deque([robot])

while queue:
    r, c, d = queue.popleft()

    if not clean[r][c]:
        clean[r][c] = True
        cnt += 1

    flag = True
    for i in range(4):
        md = (d - (i + 1)) % 4
        mr, mc = r + dr[md], c + dc[md]

        if not board[mr][mc] and not clean[mr][mc]:
            queue.append([mr, mc, md])
            flag = False
            break

    if flag:
        mr, mc = r + dr[d] * -1, c + dc[d] * -1
        if not board[mr][mc]:
            queue.append([mr, mc, d])

print(cnt)