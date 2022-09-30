import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = numbers[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)


def update(start, end, node, left, right, val):
    if left > end or right < start:
        return

    if left <= start and end <= right:
        tree[node] += val
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, left, right, val)
    update(mid + 1, end, node * 2 + 1, left, right, val)


def query(start, end, node, index, lazy):
    if not start <= index <= end:
        return 0

    lazy += tree[node]
    if start == end:
        return lazy

    mid = (start + end) // 2
    return query(start, mid, node * 2, index, lazy) + query(mid + 1, end, node * 2 + 1, index, lazy)


n = int(input())
numbers = [0] + list(map(int, input().split()))
m = int(input())

size = 2 ** (ceil(log2(n)) + 1)
tree = [0] * size
lazy = [0] * size

init(1, n, 1)

for _ in range(m):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        update(1, n, 1, *cmd[1:])
    else:
        print(query(1, n, 1, cmd[1], 0))