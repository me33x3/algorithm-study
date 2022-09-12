import sys, math
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def find(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return find(start, mid, node*2, left, right) + find(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, diff):
    if not (start <= index <= end):
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


n, q = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
size = 2 ** (math.ceil(math.log2(n)) + 1)
tree = [0] * size

init(1, n, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())

    if x > y:
        x, y = y, x

    print(find(1, n, 1, x, y))
    update(1, n, 1, a, b - num_list[a])
    num_list[a] = b