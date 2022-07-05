import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if x != root[x]:
        tmp = find(root[x])
        dist[x] += dist[root[x]]
        root[x] = tmp
    return root[x]

def union(a, b, c):
    A, B = find(a), find(b)
    if A != B:
        root[B] = A
        dist[B] = dist[a] + c - dist[b]

while True:
    n, m = map(int, input().split())

    if n + m == 0:
        break

    root = [i for i in range(n + 1)]
    dist = [0 for i in range(n + 1)]

    for _ in range(m):
        work = input().split()

        if work[0] == '!':
            union(*map(int, work[1:]))
        else:
            a, b = map(int, work[1:])
            find(a)
            find(b)

            print(dist[b] - dist[a] if root[a] == root[b] else "UNKNOWN")