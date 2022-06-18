import sys
sys.setrecursionlimit(10 ** 6)

def dfs(u):
    for v in sub[u]:
        compliment[v] += compliment[u]
        dfs(v)

n, m = map(int, input().split())

sub = {i: [] for i in range(1, n + 1)}
for b, p in zip(range(2, n + 1), list(map(int, input().split()))[1:]):
    sub[p].append(b)

compliment = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

dfs(1)
print(*compliment[1:])