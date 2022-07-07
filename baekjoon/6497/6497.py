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

    return rx != ry

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    answer = 0
    root = [i for i in range(m)]
    routes = []

    for _ in range(n):
        routes.append(list(map(int, input().split())))
        answer += routes[-1][-1]

    routes.sort(key=lambda x: x[-1])

    for x, y, z in routes:
        if union(x, y):
            answer -= z

    print(answer)