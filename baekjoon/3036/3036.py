def GCD(a, b):
    while a % b:
        a, b = b, a % b
    return b

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    divisor = GCD(max(rings[0], rings[i]), min(rings[0], rings[i]))
    print("/".join(map(str, [rings[0]//divisor, rings[i]//divisor])))