t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    cnt, move, moved = 0, 1, 0

    while moved < dist:
        cnt += 1
        moved += move
        if cnt % 2 == 0:
            move += 1

    print(cnt)