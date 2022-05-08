n, m = map(int, input().split())
six = one = float('inf')

for _ in range(m):
    x, y = map(int, input().split())
    six = min(six, x)
    one = min(one, y)

print(min(six, one * 6) * (n // 6) + min(six, one * (n % 6)))