S = input()
target = input()
stack = []

for i in range(len(S)):
    stack.append(S[i])
    if stack[-1] == target[-1] and ''.join(stack[-len(target):]) == target:
        del stack[-len(target):]

print(''.join(stack) if stack else 'FRULA')