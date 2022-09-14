import sys, math
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        leaf[start] = node
    else:
        mid = (start + end) // 2
        init(start, mid, node*2)
        init(mid+1, end, node*2+1)


def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


def modify(node, diff):
    while node > 0:
        tree[node] += diff
        node //= 2


n, m = map(int, input().split())
data = [0] * (n + 1)
tree = [0] * 2 ** (math.ceil(math.log2(n)) + 1)
leaf = [0] * (n + 1)

init(1, n, 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a:
        modify(leaf[b] // 2, c - tree[leaf[b]])
        tree[leaf[b]] = c
    else:
        if b > c:
            b, c = c, b
        print(query(1, n, 1, b, c))