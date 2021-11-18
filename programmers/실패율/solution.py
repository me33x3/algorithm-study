def solution(N, stages):
    answer = dict()
    player = len(stages)

    for stage in range(1, N + 1):
        if player:
            count = stages.count(stage)
            answer[stage] = count / player
            player -= count
        else:
            answer[stage] = 0

    return sorted(answer, key=lambda x:answer[x], reverse=True)

print(solution(5, [2,1,2,6,2,4,3,3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]