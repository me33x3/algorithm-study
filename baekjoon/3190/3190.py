from collections import deque

n, k = int(input()), int(input())

apples = []
for _ in range(k):
    apples.append(list(map(int, input().split())))

L = int(input())

direction = dict()
for _ in range(L):
    x, c = input().split()
    direction[int(x)] = c

board = [[False] * (n + 1) for _ in range(n + 1)]
board[1][1] = True
mx, my = 1, 0
sec = 0

queue = deque([[1, 1]])
while queue:
    x, y = queue.popleft()

    sec += 1
    if sec in direction:
        mx, my = my, mx
        if direction[sec] == 'L':
            if my: my *= -1
        else:
            if mx: mx *= -1

    tx, ty = x + mx, y + my

    print(mx, my, tx, ty)

    if 1 <= tx <= n and 1 <= ty <= n and not board[tx][ty]:
        board[tx][ty] = True
        if [tx, ty] not in apples:
            board[x][y] = False
        queue.append([tx, ty])
    else:
        break

print(sec)
