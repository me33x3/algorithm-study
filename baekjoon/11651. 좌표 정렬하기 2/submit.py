coords = [list(map(int, input().split())) for _ in range(int(input()))]
coords.sort(key=lambda x:(x[1], x[0]))

for x, y in coords:
    print(x, y)