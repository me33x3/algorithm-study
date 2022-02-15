h, m = map(int, input().split())
t = int(input())

h = (m + t) // 60 + h
m = (m + t) % 60

print(h - 24 if h >= 24 else h, m)