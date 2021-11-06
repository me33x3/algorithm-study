def solution(n):
    numbers = [ 4, 1, 2 ]
    base = len(numbers)

    res = []

    while n:
        res.append(numbers[n % base])
        share = (n - 1) // base

        if share > base:
            n = share
            continue
        elif share > 0:
            res.append(numbers[share % base])
        n = 0

    return ''.join(map(str, res[::-1]))

print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
print(solution(4)) # 11
print(solution(14)) # 112