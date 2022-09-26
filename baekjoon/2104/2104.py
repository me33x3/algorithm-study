import sys
from math import ceil, log2
sys.setrecursionlimit(10 ** 6)


def init(s, e, i):
    if s == e:
        tree[i] = [arr[s], s]
    else:
        m = (s + e) // 2

        tl = init(s, m, i * 2)
        tr = init(m + 1, e, i * 2 + 1)

        tree[i][0] = tl[0] + tr[0]
        tree[i][1] = tl[1] if arr[tl[1]] <= arr[tr[1]] else tr[1]
    return tree[i]


def find(l, r):
    global answer

    if l > r:
        return

    v, m = query(1, n, 1, l, r)
    answer = max(answer, v * arr[m])

    find(l, m - 1)
    find(m + 1, r)


def query(s, e, i, l, r):
    if l > e or r < s:
        return [0, 0]
    if l <= s and e <= r:
        return tree[i]

    m = (s + e) // 2

    tl = query(s, m, i * 2, l, r)
    tr = query(m + 1, e, i * 2 + 1, l, r)

    if not tl[1]:
        return tr
    elif not tr[1]:
        return tl
    else:
        return [tl[0] + tr[0], tl[1] if arr[tl[1]] <= arr[tr[1]] else tr[1]]


n = int(input())
arr = [0] + list(map(int, input().split()))
tree = [[0, 0] for _ in range(2 ** (ceil(log2(n)) + 1))]
answer = 0

init(1, n, 1)
find(1, n)

print(answer)