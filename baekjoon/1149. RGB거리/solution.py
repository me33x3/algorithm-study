n = int(input())
rgb = []

for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n):
    r, g, b = rgb[i - 1]
    rgb[i][0] += min(g, b)
    rgb[i][1] += min(r, b)
    rgb[i][2] += min(r, g)

print(min(rgb[-1]))