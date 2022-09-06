import sys
input = sys.stdin.readline


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    rx, ry = find(x), find(y)

    if rx != ry:
        if rx < ry:
            root[ry] = rx
        else:
            root[rx] = ry

    return rx != ry


n = int(input())
lx, ly, lz = [], [], []
cost = []
root = [i for i in range(n)]
answer = 0

for i in range(n):
    x, y, z = map(int, input().split())
    lx.append((x, i))
    ly.append((y, i))
    lz.append((z, i))

lx.sort()
ly.sort()
lz.sort()

for l in lx, ly, lz:
    for i in range(n-1):
        cost.append([l[i][1], l[i+1][1], abs(l[i][0] - l[i+1][0])])

cost.sort(key=lambda x: x[-1])

for a, b, c in cost:
    if union(a, b):
        answer += c

print(answer)