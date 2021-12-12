def solution(d, budget):
    d.sort()

    sum, answer = 0, 0
    for price in d:
        sum += price
        if sum > budget:
            break
        answer += 1

    return answer

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4