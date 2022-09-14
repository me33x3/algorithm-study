import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def update_lazy(start, end, node):
    if lazy[node]:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def update_range(start, end, node, left, right, value):
    update_lazy(start, end, node)

    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * value
        if start != end:
            lazy[node * 2] += value
            lazy[node * 2 + 1] += value
    else:
        mid = (start + end) // 2
        update_range(start, mid, node * 2, left, right, value)
        update_range(mid + 1, end, node * 2 + 1, left, right, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, left, right):
    update_lazy(start, end, node)

    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


n, m, k = map(int, input().split())
data = [0] + [int(input()) for _ in range(n)]
size = 2 ** (ceil(log2(n)) + 1)
tree = [0] * size
lazy = [0] * size

init(1, n, 1)

for _ in range(m + k):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        update_range(1, n, 1, *cmd[1:])
    else:
        print(query(1, n, 1, *cmd[1:]))