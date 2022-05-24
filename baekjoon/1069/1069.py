x, y, d, t = map(int, input().split())
dist = (x * x + y * y) ** 0.5

res = 0
if dist >= d:
    res = min((dist // d) * t + (dist % d), (dist // d + 1) * t)
else:
    res = min(float(t * 2), d - dist + t)
print(min(res, dist))