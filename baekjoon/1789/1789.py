s = int(input())
tmp, n, i = 0, 0, 1

while s > tmp:
    if (s - tmp) / i != 2:
        tmp += i
        n += 0 if tmp > s else 1
    i += 1

print(n)