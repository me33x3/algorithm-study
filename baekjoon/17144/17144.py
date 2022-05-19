import sys
input = sys.stdin.readline

def clean():
    for i in range(2):
        N = cleaner[i]
        x, y = N, 0

        d, tmp = 1, 0
        start, end = (N, R) if i else (-1, N)

        for _ in range(2):
            while 0 <= y + d < C:
                y += d
                room[x][y], tmp = tmp, room[x][y]

            if i == 0:
                d *= -1

            while start < x + d < end:
                x += d
                room[x][y], tmp = tmp, room[x][y]

            if i == 1:
                d *= -1

def spread():
    tmp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                amount = room[x][y] // 5
                cnt = 0

                for nx, ny in zip(dx, dy):
                    mx, my = x + nx, y + ny

                    if 0 <= mx < R and 0 <= my < C and room[mx][my] != -1:
                        tmp[mx][my] += amount
                        cnt += 1

                room[x][y] -= amount * cnt

    for x in range(R):
        for y in range(C):
            room[x][y] += tmp[x][y]

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner = [i, i + 1]
        break

for t in range(T):
    spread()
    clean()

print(sum(map(sum, room)) + 2)