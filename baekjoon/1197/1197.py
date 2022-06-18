def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])

root = [i for i in range(v + 1)]
answer = 0

for a, b, c in edges:
    A, B = find(a), find(b)

    if A != B:
        if A < B:
            root[B] = A
        else:
            root[A] = B
        answer += c

print(answer)