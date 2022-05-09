from collections import deque

def bfs():
    queue = deque([[1, 0]])
    v = [False] * 101

    while queue:
        curr, cnt = queue.popleft()

        for move in range(1, 7):
            tmp = curr + move

            if tmp in ladders:
                tmp = ladders[tmp]
            elif tmp in snakes:
                tmp = snakes[tmp]

            if not v[tmp]:
                if tmp == 100:
                    return cnt + 1
                queue.append([tmp, cnt + 1])
                v[tmp] = True

N, M = map(int, input().split())
ladders, snakes = {}, {}

for _ in range(N):
    k, v = map(int, input().split())
    ladders[k] = v

for _ in range(M):
    k, v = map(int, input().split())
    snakes[k] = v

print(bfs())