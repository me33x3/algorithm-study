from collections import deque

M, N = map(int, input().split())

store, queue = [], deque()
for n in range(N):
    store.append(list(map(int, input().split())))

    for m in range(M):
        if store[n][m] == 1:
            queue.append([n, m])

answer = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while True:
    tmp = deque()
    while queue:
        n, m = queue.popleft()

        for x, y in zip(dx, dy):
            mx, my = m + x, n + y

            if mx > -1 and mx < M and my > -1 and my < N:
                if store[my][mx] == 0:
                    store[my][mx] = 1
                    tmp.append([my, mx])

    if not tmp:
        break

    answer += 1
    queue = tmp

print(answer if all(0 not in l for l in store) else -1)