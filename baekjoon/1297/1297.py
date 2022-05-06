d, h, w = map(int, input().split())
n = d / (h ** 2 + w ** 2) ** 0.5
print(int(h * n), int(w * n))