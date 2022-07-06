import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx, ry = find(x), find(y)

    if rx > ry:
        root[rx] = ry
    else:
        root[ry] = rx

def has_path(x, y):
    return find(x) == find(y)

for t in range(int(input())):
    n = int(input())
    k = int(input())

    root = [i for i in range(n)]
    for _ in range(k):
        union(*map(int, input().split()))

    print(f'Scenario {t + 1}:')

    m = int(input())
    for _ in range(m):
        print(1 if has_path(*map(int, input().split())) else 0)
    print()