from collections import deque

def backtracking():
    queue = deque([[i] for i in range(10)])
    cnt = 0

    while queue:
        num = queue.popleft()

        if cnt == N:
            return ''.join(map(str, num))

        cnt += 1
        for i in range(10):
            if num[-1] > i:
                queue.append(num + [i])

    return -1

N = int(input())
print(backtracking())