import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

n, m = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
routes.sort(key=lambda x: x[2])
root = [i for i in range(n + 1)]

res = []
for a, b, c in routes:
    A, B = find(a), find(b)

    if A != B:
        if A > B:
            root[A] = B
        else:
            root[B] = A
        res.append(c)

print(sum(res[:-1]))