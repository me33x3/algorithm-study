import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop() if len(stack) else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if len(stack) else 1)
    elif command[0] == 'top':
        print(stack[-1] if len(stack) else -1)