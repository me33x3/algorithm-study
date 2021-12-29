def solution(gems):
    answer = [1, len(gems)]
    shortest = answer[1] - answer[0]
    type = len(set(gems))
    start, end = 0, 0
    buy = {}

    while end < len(gems):
        if gems[end] not in buy:
            buy[gems[end]] = 1
        else:
            buy[gems[end]] += 1

        end += 1

        if len(buy) == type:
            while start < end:
                if buy[gems[start]] > 1:
                    buy[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1, end]
                else:
                    break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # 	[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]