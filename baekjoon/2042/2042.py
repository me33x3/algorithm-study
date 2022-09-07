import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start+end)//2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)

    return tree[node]


def update(start, end, node, idx, val):
    if idx < start or idx > end:
        return

    tree[node] += val

    if start == end:
        return

    mid = (start+end)//2
    update(start, mid, node*2, idx, val)
    update(mid+1, end, node*2+1, idx, val)


def calc(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start+end)//2
    return calc(start, mid, node*2, left, right) + calc(mid+1, end, node*2+1, left, right)


n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
tree = [0] * (n * 4)

init(1, n, 1)

for i in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, n, 1, b, c - nums[b])
        nums[b] = c
    else:
        print(calc(1, n, 1, b, c))