import itertools

def solution(k, dungeons):
    answer = 0

    for permutaions in itertools.permutations(dungeons):
        fatigue, count = k, 0

        for need, consume in permutaions:
            if fatigue >= need:
                fatigue -= consume
                count += 1
            else:
                break

        answer = max(answer, count)

        if answer == len(dungeons):
            break

    return answer

print(solution(80, [ [ 80, 20 ], [ 50, 40 ], [ 30, 10 ] ])) # 3