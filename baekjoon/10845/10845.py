import sys
input = sys.stdin.readline

queue = []
for _ in range(int(input())):
    order = input().rstrip()

    if order == 'pop':
        print(queue.pop(0) if queue else -1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(0 if queue else 1)
    elif order == 'front':
        print(queue[0] if queue else -1)
    elif order == 'back':
        print(queue[-1] if queue else -1)
    else:
        queue.append(order.split()[1])