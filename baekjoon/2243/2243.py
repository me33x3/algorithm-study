import sys
from math import ceil, log2
input = sys.stdin.readline


def update(s, e, n, i, v):
    if not s <= i <= e:
        return

    if s == e:
        tree[n] += v
    else:
        m = (s + e) // 2
        update(s, m, n * 2, i, v)
        update(m + 1, e, n * 2 + 1, i, v)
        tree[n] = tree[n * 2] + tree[n * 2 + 1]


def query(s, e, n, i):
    if s == e:
        print(s)
        tree[n] -= 1
        return

    m = (s + e) // 2

    if tree[n * 2] >= i:
        query(s, m, n * 2, i)
    else:
        query(m + 1, e, n * 2 + 1, i - tree[n * 2])

    tree[n] = tree[n * 2] + tree[n * 2 + 1]


k = 10 ** 6
size = 2 ** (ceil(log2(k)) + 1)
tree = [0] * size

for _ in range(int(input())):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        query(1, k, 1, cmd[1])
    else:
        update(1, k, 1, *cmd[1:])