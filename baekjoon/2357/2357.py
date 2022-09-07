import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = [num_list[start]] * 2
    else:
        mid = (start + end) // 2
        child = init(start, mid, node*2) + init(mid+1, end, node*2+1)
        tree[node] = [min(child), max(child)]
    return tree[node]


def find(start, end, left, right, node):
    if left > end or right < start:
        return []

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    child = find(start, mid, left, right, node*2) + find(mid+1, end, left, right, node*2+1)
    return [min(child), max(child)]


n, m = map(int, input().split())
num_list = [0] + [int(input()) for _ in range(n)]
tree = [[] for _ in range(n * 4)]

init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*find(1, n, a, b, 1))