bar = list(input())
answer = 0
stack = []

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    else:
        stack.pop()
        answer += len(stack) if bar[i - 1] == '(' else 1

print(answer)