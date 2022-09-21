import sys
from math import ceil, log2
input = sys.stdin.readline
inf = sys.maxsize


def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1))
    return tree[node]


def update(start, end, node, index):
    if not start <= index <= end:
        return

    if start == end:
        tree[node] = num_list[index]
    else:
        mid = (start + end) // 2
        update(start, mid, node * 2, index)
        update(mid + 1, end, node * 2 + 1, index)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(start, end, node, left, right):
    if left > end or right < start:
        return inf

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(query(start, mid, node * 2, left, right), query(mid + 1, end, node * 2 + 1, left, right))


n = int(input())
num_list = [0] + list(map(int, input().split()))
m = int(input())
tree = [0] * 2 ** (ceil(log2(n)) + 1)

init(1, n, 1)

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        num_list[b] = c
        update(1, n, 1, b)
    else:
        print(query(1, n, 1, b, c))