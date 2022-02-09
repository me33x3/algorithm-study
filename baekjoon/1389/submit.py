from collections import deque

def bfs(target):
    num = [0 for _ in range(N + 1)]
    queue = deque([conn[target]])
    v = [target]

    term = 1
    while queue:
        l = []
        for i in queue.popleft():
            if i not in v:
                num[i] = term
                v.append(i)
                for j in conn[i]:
                    l.append(j)
        if l:
            queue.append(l)

        term += 1

    return sum(num)

N, M = map(int, input().split())
conn = dict(zip(list(range(1, N + 1)), [[] for _ in range(N)]))

for _ in range(M):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)

answer, kb = 0, N ** 2
for i in range(1, N + 1):
    temp = bfs(i)
    if temp < kb:
        kb = temp
        answer = i

print(answer)