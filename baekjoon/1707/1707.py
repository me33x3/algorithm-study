import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(n, group):
        visited[n] = group

        for i in graph[n]:
            if not visited[i]:
                if not dfs(i, -group):
                    return False
            elif visited[n] == visited[i]:
                return False

        return True

for _ in range(int(input())):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipartite = True
    for i in range(1, v + 1):
        if not visited[i]:
            bipartite = dfs(i, 1)

            if not bipartite:
                break

    print('YES' if bipartite else 'NO')