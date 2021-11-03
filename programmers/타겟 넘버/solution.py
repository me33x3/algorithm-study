def solution(numbers, target):
    values = [ 0 ]

    for n in numbers:
        for i in range(len(values)):
            values.append(values[i] + n)
            values[i] -= n

    return sum([1 for v in values if v == target])

print(solution([1, 1, 1, 1, 1], 3)) # 5