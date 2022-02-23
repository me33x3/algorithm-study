def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())

nums = []
for i in range(M, N + 1):
    if isPrime(i):
        nums.append(i)

if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)