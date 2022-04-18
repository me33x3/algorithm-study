from collections import deque

N, K = map(int, input().split())
q = deque(list(range(1, N + 1)))

print('<', end='')
while len(q) > 1:
    for k in range(K):
        i = q.popleft()
        if k + 1 < K:
            q.append(i)
        else:
            print(i, end=', ')
print('%d>' % q.popleft())