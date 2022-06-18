import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

n, m = map(int, input().split())
root = [i for i in range(n + 1)]

for _ in range(m):
    num, a, b = map(int, input().split())

    if num == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')