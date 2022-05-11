from collections import deque

n, k = map(int, input().split())
v = [float('inf')] * 200001
v[n] = 0

queue = deque([n])
while queue:
    curr = queue.popleft()

    if curr == k:
        print(v[curr])
        break

    move = curr * 2
    if move <= 200000 and v[move] > v[curr]:
        queue.appendleft(move)
        v[move] = v[curr]

    move = curr - 1
    if move >= 0 and v[move] > v[curr]:
        queue.append(move)
        v[move] = v[curr] + 1

    move = curr + 1
    if move <= 200000 and v[move] > v[curr]:
        queue.append(move)
        v[move] = v[curr] + 1