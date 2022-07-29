from collections import deque, defaultdict

def bfs():
    v = [0] * (n + 1)
    v[a] = 1

    queue = deque([[a, 0]])
    while queue:
        curr, degree = queue.popleft()

        if curr == b:
            return degree

        for next in family[curr]:
            if not v[next]:
                v[next] = 1
                queue.append([next, degree + 1])

    return -1

n = int(input())
a, b = map(int, input().split())

family = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

print(bfs())