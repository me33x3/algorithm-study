res = 0
for i in map(int, input().split()):
    res += i ** 2
print(res % 10)