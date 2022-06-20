from collections import deque

def bfs(c):
    queue = deque([start])
    visited = {start}

    while queue:
        u = queue.popleft()

        for v, w in bridge[u]:
            if w >= c and v not in visited:
                visited.add(v)
                queue.append(v)

    return True if end in visited else False

n, m = map(int, input().split())
bridge = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))

start, end = map(int, input().split())
left, right = 1, 10 ** 9
answer = 0

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)