def solution(price, money, count):
    N = money - sum([i * price for i in range(1, count+1)])

    return 0 if N > 0 else N * -1

print(solution(3, 20, 4)) # 10