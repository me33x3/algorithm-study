from collections import deque, defaultdict

n, m = map(int, input().split())
o = [int(input()) for _ in range(n)]
friends = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

res = True
visited = set()
for i in range(n):
    if i not in visited:
        visited.add(i)
        k = o[i]

        queue = deque([i])
        while queue:
            u = queue.popleft()

            for v in friends[u]:
                if v not in visited:
                    k += o[v]
                    visited.add(v)
                    queue.append(v)

        if k != 0:
            res = False
            break

print('POSSIBLE' if res else 'IMPOSSIBLE')