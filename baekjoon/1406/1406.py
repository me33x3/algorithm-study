l, r = list(input()), []

for _ in range(int(input())):
    order = input().split()

    if order[0] == 'L':
        if l:
            r.append(l.pop())
    elif order[0] == 'D':
        if r:
            l.append(r.pop())
    elif order[0] == 'B':
        if l:
            l.pop()
    else:
        l.append(order[1])

print(''.join(l + r[::-1]))