from collections import deque

n, k = int(input()), int(input())

apples = []
for _ in range(k):
    apples.append(list(map(int, input().split())))

L = dict()
for _ in range(int(input())):
    x, c = input().split()
    L[int(x)] = c

snake = deque([(1, 1)])

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
queue = deque([[1, 1]])
d, sec = 1, 0

while queue:
    x, y = queue.popleft()

    mx, my = x + dx[d], y + dy[d]
    if 1 <= mx <= n and 1 <= my <= n and not (mx, my) in snake:
        snake.append((mx, my))

        if [mx, my] not in apples:
            snake.popleft()
        else:
            apples.pop(apples.index([mx, my]))

        queue.append([mx, my])
    else:
        break

    sec += 1
    if sec in L:
        if L[sec] == 'L':
            d = (d - 1 + 4) % 4
        else:
            d = (d + 1) % 4

print(sec + 1)