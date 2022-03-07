import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    for i in a[x]:
        if visited[i]:
            continue
        visited[i] = True

        if w[i] == 0 or dfs(w[i]):
            w[i] = x
            return True
    return False

n, m = map(int, input().split())
a = {}
w = [0] * (m + 1)

for i in range(1, n + 1):
    a[i] = list(map(int, input().split()))[1:]

answer = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    answer += 1 if dfs(i) else 0
print(answer)