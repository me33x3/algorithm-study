n, m = map(int, input().split())
dividend, divisor = 1, 1
for i in range(m):
    dividend *= n - i
    divisor *= i + 1
print(dividend // divisor)