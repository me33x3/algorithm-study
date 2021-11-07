from itertools import combinations

def solution(nums):
    answer = 0

    for n in combinations(nums, 3):
        n = sum(n)
        flag = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = 0
                break
        answer += flag

    return answer

print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4