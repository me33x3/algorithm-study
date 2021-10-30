def solution(word):
    answer = 0
    N = 5
    pattern = [ 1 ]

    for _ in range(1, N):
        pattern.insert(0, pattern[0] * N + 1)

    for i, char in enumerate(word):
        answer += "AEIOU".index(char) * pattern[i] + 1

    return answer

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189