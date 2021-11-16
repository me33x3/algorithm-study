from collections import deque

M, N = map(int, input().split())

store, queue = [], deque()
for n in range(N):
    store.append(list(map(int, input().split())))

    for m in store[-1]:
        if m == 1:
            queue.append([n, m])

answer = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while queue:
    n, m = queue.popleft()
    tmp = deque()

    for x, y in zip(dx, dy):
        mx, my = n + x, m + y

        if mx > -1 and mx < N and my > -1 and my < M:
            if store[mx][my] == 0:
                store[mx][my] = 1
                tmp.append([mx, my])

    if tmp:
        answer += 1
        queue = tmp

print(answer if all(0 not in l for l in store) else -1)