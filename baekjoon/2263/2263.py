import sys
sys.setrecursionlimit(10**6)

def traversal(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    left, right = pos[root] - in_start, in_end - pos[root]
    print(root, end=' ')

    traversal(in_start, in_start + left - 1, post_start, post_start + left - 1)
    traversal(in_end - right + 1, in_end, post_end - right, post_end - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0] * (n + 1)
for i, j in enumerate(in_order):
    pos[j] = i

traversal(0, n - 1, 0, n - 1)