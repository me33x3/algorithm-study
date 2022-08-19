from collections import deque

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def check(x, y):
    num = 0

    while num < len(start):
        sx, sy = start[num]
        if x == sx and y == sy:
            return num
        num += 1

    return -1

def find(i, j):
    num = check(i, j)
    if num >= 0:
        return [num, 0]

    q = deque([[i, j, 0]])

    v = [[0] * n for _ in range(n)]
    v[i][j] = 1

    depth = 0
    passenger = []

    while q:
        x, y, dist = q.popleft()

        if dist >= fuel:
            break

        if depth < dist:
            if passenger:
                passenger.sort()
                return [passenger[0][-1], dist]

            depth += 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and not v[nx][ny]:
                v[nx][ny] = 1
                q.append([nx, ny, dist + 1])

                num = check(nx, ny)
                if num >= 0:
                    passenger.append([nx, ny, num])

    return [-1, -1]


def move(sx, sy, ex, ey):
    q = deque([[sx, sy, 0]])

    v = [[0] * n for _ in range(n)]
    v[sx][sy] = 1

    while q:
        x, y, dist = q.popleft()

        if dist >= fuel:
            break

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and not v[nx][ny]:
                if nx == ex and ny == ey:
                    return dist + 1

                v[nx][ny] = 1
                q.append([nx, ny, dist + 1])

    return -1


n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

bx, by = map(lambda x: int(x) - 1, input().split())

start, end = [], []
for _ in range(m):
    sx, sy, ex, ey = map(lambda x: int(x) - 1, input().split())
    start.append([sx, sy])
    end.append([ex, ey])

while start:
    num, dist = find(bx, by)

    if dist < 0:
        break

    bx, by = start[num]
    fuel -= dist

    dist = move(*start[num], *end[num])

    if dist < 0:
        break

    bx, by = end[num]
    fuel += dist

    start.pop(num)
    end.pop(num)

print(-1 if start else fuel)