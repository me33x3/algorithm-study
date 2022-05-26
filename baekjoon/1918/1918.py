infix = input()
stack = []
postfix = ''

for ch in infix:
    if ch.isalpha():
        postfix += ch
    else:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        elif ch in ('*', '/'):
            while stack and stack[-1] in ('*', '/'):
                postfix += stack.pop()
            stack.append(ch)
        elif ch in ('+', '-'):
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(ch)

while stack:
    postfix += stack.pop()

print(postfix)