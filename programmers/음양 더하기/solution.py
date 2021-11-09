def solution(absolutes, signs):
    return sum([absolute if sign else absolute * -1 for absolute, sign in zip(absolutes, signs)])

print(solution([4, 7, 12], [True, False, True])) # 9
print(solution([1, 2, 3], [False, False, True])) # 0