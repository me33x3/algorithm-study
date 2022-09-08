import sys, math
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2) * init(mid+1, end, node*2+1) % 1000000007
    return tree[node]


def update(start, end, node, idx, val):
    if idx < start or end < idx:
        return

    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        update(start, mid, node*2, idx, val)
        update(mid+1, end, node*2+1, idx, val)
        tree[node] = tree[node*2] * tree[node*2+1] % 1000000007


def find(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return find(start, mid, node*2, left, right) * find(mid+1, end, node*2+1, left, right) % 1000000007


n, m, k = map(int, input().split())
num_list = [0] + [int(input()) for _ in range(n)]
size = 2 ** (math.ceil(math.log2(n)) + 1)
tree = [0] * size

init(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, n, 1, b, c)
        num_list[b] = c
    else:
        print(find(1, n, 1, b, c))