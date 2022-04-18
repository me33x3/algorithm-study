def get_prime_list(x):
    is_prime = [False, False] + [True] * (x - 1)
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, x + 1, i):
                is_prime[j] = False
    return [num for num, flag in enumerate(is_prime) if flag]

n = int(input())
prime_list = get_prime_list(n)

cnt = 0
l, r = 0, 0
while r <= len(prime_list):
    total = sum(prime_list[l:r])
    if total >= n:
        l += 1
        cnt += 1 if total == n else 0
    else:
        r += 1
print(cnt)