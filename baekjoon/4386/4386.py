def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

root = [i for i in range(n + 1)]
edges = []
cost = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5
        edges.append([dist, i, j])
edges.sort()

for d, i, j in edges:
    ri, rj = find(i), find(j)

    if ri != rj:
        if ri > rj:
            root[ri] = rj
        else:
            root[rj] = ri

        cost += d

print(cost)