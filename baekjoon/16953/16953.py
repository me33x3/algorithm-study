from collections import deque

def bfs():
    queue = deque([[a, 1]])

    while queue:
        num, cnt = queue.popleft()

        for tmp in (num * 2, num * 10 + 1):
            if tmp <= b:
                if tmp == b:
                    return cnt + 1
                queue.append([tmp, cnt + 1])

    return -1

a, b = map(int, input().split())
print(bfs())