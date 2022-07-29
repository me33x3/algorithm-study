from collections import deque

def bfs():
    v = [0] * (F + 1)
    v[S] = 1

    queue = deque([[S, 0]])
    while queue:
        curr, cnt = queue.popleft()

        if curr == G:
            return cnt

        for next in [curr + U, curr - D]:
            if 0 < next <= F and not v[next]:
                v[next] = 1
                queue.append([next, cnt + 1])

    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs())