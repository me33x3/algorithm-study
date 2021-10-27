import itertools

def solution(k, dungeons):
    answer = 0
    permutations = list(itertools.permutations(list(range(len(dungeons)))))

    for p in permutations:
        fatigue = k
        tmp = 0

        for i in p:
            if dungeons[i][0] <= fatigue:
                fatigue -= dungeons[i][1]
                tmp += 1
            else:
                break

        if tmp > answer:
            answer = tmp

        if len(dungeons) == answer:
            break

    return answer

print(solution(80, [ [ 80, 20 ], [ 50, 40 ], [ 30, 10 ] ]))