def find(name):
    if name != root[name]:
        root[name] = find(root[name])
    return root[name]

def union(a, b):
    root_a, root_b = find(a), find(b)

    if root_a != root_b:
        root[root_b] = root_a
        cnt[root_a] += cnt[root_b]

    return cnt[root_a]

for _ in range(int(input())):
    f = int(input())
    root, cnt = dict(), dict()

    for _ in range(f):
        a, b = input().split()

        for name in [a, b]:
            if name not in root:
                root[name] = name
                cnt[name] = 1

        print(union(a, b))