n, m, broken = int(input()), int(input()), []
if m:
    broken = list(input().split())
res = abs(100 - n)

for i in range(1000001):
    flag = True
    for digit in str(i):
        if digit in broken:
            flag = False
            break
    if flag:
        res = min(res, abs(i - n) + len(str(i)))

print(res)