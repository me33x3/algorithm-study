import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def init(start, end, node):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        init(start, mid, node*2)
        init(mid+1, end, node*2+1)
        tree[node] = tree[node*2] if data[tree[node*2]] <= data[tree[node*2+1]] else tree[node*2+1]


def find(start, end, node, left, right):
    if left > end or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    a = find(start, mid, node*2, left, right)
    b = find(mid+1, end, node*2+1, left, right)

    if a < 0:
        return b
    elif b < 0:
        return a
    else:
        if data[a] <= data[b]:
            return a
        else:
            return b


def largest(left, right):
    m = find(1, n, 1, left, right)
    area = (right-left+1) * data[m]

    if left <= m-1:
        area = max(area, largest(left, m-1))
    if right >= m+1:
        area = max(area, largest(m+1, right))

    return area


while True:
    data = list(map(int, input().split()))

    if len(data) == 1:
        break

    n, data[0] = data[0], 0
    size = 2 ** (math.ceil(math.log2(n)) + 1)
    tree = [0] * size

    init(1, n, 1)
    print(largest(1, n))