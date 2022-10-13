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


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

direction = dict(zip(['U', 'D', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]))
root = [i for i in range(n * m)]
v = [0] * (n * m)

for r in range(n):
    for c in range(m):
        d = direction[board[r][c]]
        nr, nc = r + d[0], c + d[1]
        union(r * m + c, nr * m + nc)

for i in range(n * m):
    v[find(root[i])] = 1

print(sum(v))
