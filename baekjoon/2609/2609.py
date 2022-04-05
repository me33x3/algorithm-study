a, b = map(int, input().split())

res, i = 1, 2
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        a //= i
        b //= i
        res *= i
    else:
        i += 1

print(res)
print(res * a * b)