def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0
    temp = ''

    while n > 0:
        temp = str(n % k) + temp
        n //= k

    i = 0
    for j, digit in enumerate(temp):
        if digit == '0':
            num = temp[i:j]
            if num:
                answer += 1 if isPrime(int(num)) else 0
            i = j + 1

    if i != len(temp):
        answer += 1 if isPrime(int(temp[i:])) else 0

    return answer

print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2