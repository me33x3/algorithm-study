from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def numbering(num, r, c):
    q = deque([[r, c]])

    while q:
        x, y = q.popleft()
        land.append([x, y])

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
                if board[nx][ny] == 1:
                    board[nx][ny] = num
                    q.append([nx, ny])

                v[nx][ny] = 1


def bridge(x, y):
    a = board[x][y]

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        dist = 0
        b = a

        while 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny]:
                b = board[nx][ny]
                break

            nx += dx[d]
            ny += dy[d]
            dist += 1

        if a != b and dist >= 2:
            edges.append([dist, a, b])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

num = 1
v = [[0] * m for _ in range(n)]
land = []

for r in range(n):
    for c in range(m):
        if board[r][c] == 1 and not v[r][c]:
            v[r][c] = 1
            board[r][c] = num
            numbering(num, r, c)
            num += 1

root = [i for i in range(num)]
edges = []
num -= 2

for r, c in land:
    bridge(r, c)

edges.sort()
answer, cnt = 0, 0

for w, a, b in edges:
    A, B = find(a), find(b)

    if A != B:
        if A < B:
            root[B] = A
        else:
            root[A] = B

        answer += w
        cnt += 1

    if cnt == num:
        break

print(answer if cnt == num else -1)