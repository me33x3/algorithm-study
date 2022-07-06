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

    return rx != ry

n, m = map(int, input().split())
coords = [list(map(int, input().split())) for _ in range(n)]

root = [i for i in range(n)]
edges = []
dist = 0

for _ in range(m):
    union(*map(lambda x: int(x) - 1, input().split()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if find(i) != find(j):
            d = ((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) ** 0.5
            edges.append([d, i, j])
edges.sort()

for d, i, j in edges:
    if union(i, j):
        dist += d

print(format(dist, ".2f"))