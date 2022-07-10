score = dict(zip(['F', 'D', 'C', 'B', 'A'], range(5)))
grade = list(input())

answer = float(score[grade[0]])

if grade[0] != 'F':
    if grade[1] == '+':
        answer += 0.3
    elif grade[1] == '-':
        answer -= 0.3

print(answer)