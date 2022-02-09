from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

queue = deque()
store = []
for h in range(H):
    box = []
    for n in range(N):
        box.append(list(map(int, input().split())))
        for m in range(M):
            if box[n][m] == 1:
                queue.append([h, n, m])
    store.append(box)

answer = 0
dx, dy, dz = [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1]
while True:
    tmp = deque()

    while queue:
        h, n, m = queue.popleft()
        for x, y, z in zip(dx, dy, dz):
            mx, my, mz = x + m, y + n, z + h

            if mx > -1 and mx < M and my > -1 and my < N and mz > -1 and mz < H:
                if store[mz][my][mx] == 0:
                    store[mz][my][mx] = 1
                    tmp.append([mz, my, mx])

    if not tmp:
        break

    answer += 1
    queue = tmp

print(answer if all(0 not in line for box in store for line in box) else -1)