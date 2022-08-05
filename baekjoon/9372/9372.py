import sys
input = sys.stdin.readline

def dfs(curr, cnt):
    visited[curr] = 1

    for next in tree[curr]:
        if not visited[next]:
            cnt = dfs(next, cnt + 1)

    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())

    tree = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [0] * (N + 1)
    print(dfs(1, 0))