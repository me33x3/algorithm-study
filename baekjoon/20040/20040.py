import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        root[y] = x
    else:
        root[x] = y

n, m = map(int, input().split())
root = [i for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())

    if find(u) == find(v):
        print(i + 1)
        break
    union(u, v)
else:
    print(0)