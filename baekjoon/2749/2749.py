n = int(input())

mod = 10 ** 6
p = mod // 10 * 15
fibo = [0, 1]

for i in range(2, n % p + 1):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % mod)

print(fibo[-1])