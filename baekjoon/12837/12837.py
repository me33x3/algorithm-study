import sys
from math import ceil, log2
input = sys.stdin.readline


def update(start, end, node, index):
    if not start <= index <= end:
        return

    if start == end:
        tree[node] = balance[index]
    else:
        mid = (start + end) // 2
        update(start, mid, node * 2, index)
        update(mid + 1, end, node * 2 + 1, index)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


n, q = map(int, input().split())
balance = [0] * (n + 1)
tree = [0] * 2 ** (ceil(log2(n)) + 1)

for _ in range(q):
    a, b, c = map(int, input().split())

    if a == 1:
        balance[b] += c
        update(1, n, 1, b)
    else:
        print(query(1, n, 1, b, c))