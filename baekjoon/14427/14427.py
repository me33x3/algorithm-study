import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        a, b = init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1)
        tree[node] = a if num_list[a] <= num_list[b] else b
    return tree[node]


def update(start, end, node, index):
    if not (start <= index <= end) or start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, index)
    update(mid + 1, end, node * 2 + 1, index)
    a, b = tree[node * 2], tree[node * 2 + 1]
    tree[node] = a if num_list[a] <= num_list[b] else b


n = int(input())
num_list = [0] + list(map(int, input().split()))
m = int(input())
tree = [0] * 2 ** (ceil(log2(n)) + 1)

init(1, n, 1)

for _ in range(m):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        num_list[cmd[1]] = cmd[2]
        update(1, n, 1, cmd[1])
    else:
        print(tree[1])