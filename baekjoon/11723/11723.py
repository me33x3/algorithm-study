import sys
input = sys.stdin.readline

s = {i+1: False for i in range(20)}
for _ in range(int(input())):
    order = input().strip()

    if order == 'all':
        s = {i+1: True for i in range(20)}
    elif order == 'empty':
        s = {i+1: False for i in range(20)}
    else:
        order, n = order.split()
        n = int(n)
        if order == 'add':
            s[n] = True
        elif order == 'remove':
            s[n] = False
        elif order == 'toggle':
            s[n] = False if s[n] else True
        else:
            print(1 if s[n] else 0)