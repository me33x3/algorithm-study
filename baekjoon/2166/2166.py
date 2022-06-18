n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

a, b = 0, 0
for i in range(-1, n - 1):
    a += coords[i][0] * coords[i + 1][1]
    b += coords[i][1] * coords[i + 1][0]

print(round(abs(a - b) / 2, 1))