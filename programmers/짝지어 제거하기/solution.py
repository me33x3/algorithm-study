def solution(s):
    answer = 1

    while s and answer:
        for i in range(len(s)):
            if i == len(s) - 1:
                answer = 0
            elif s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                break

    return answer

print(solution('baabaa')) # 1
print(solution('cdcd')) # 0