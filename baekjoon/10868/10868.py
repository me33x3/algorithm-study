import sys, math
input = sys.stdin.readline
inf = sys.maxsize


def init(start, end, node):
    if start == end:
        tree[node] = num_list[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1))
    return tree[node]


def find(start, end, left, right, node):
    if left > end or right < start:
        return inf
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(find(start, mid, left, right, node*2), find(mid+1, end, left, right, node*2+1))


n, m = map(int, input().split())
num_list = [0] + [int(input()) for _ in range(n)]
size = 2 ** (math.ceil(math.log2(n)) + 1) - 1
tree = [0] * size

init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(find(1, n, a, b, 1))