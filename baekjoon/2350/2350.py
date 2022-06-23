import sys
from collections import deque, defaultdict
input = sys.stdin.readline
inf = sys.maxsize

def find(i):
    if i != root[i]:
        root[i] = find(root[i])
    return root[i]

def bfs(start, end):
    queue = deque([[start, inf]])
    visited = {start}

    while queue:
        curr, w = queue.popleft()

        for next, nw in v[curr]:
            if next not in visited:
                if end == next:
                    return min(w, nw)

                visited.add(next)
                queue.append([next, min(w, nw)])


n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2], reverse=True)

root = [i for i in range(n + 1)]
v = defaultdict(list)
for i, j, w in edges:
    a, b = find(i), find(j)

    if a == b:
        continue

    if a > b:
        root[a] = b
    else:
        root[b] = a

    v[i].append((j, w))
    v[j].append((i, w))

for _ in range(k):
    print(bfs(*map(int, input().split())))