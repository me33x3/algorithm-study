import sys
sys.setrecursionlimit(10 ** 6)

def post_order(start, end):
    if start > end:
        return

    idx = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            idx = i
            break

    post_order(start + 1, idx - 1)
    post_order(idx, end)
    print(tree[start])

tree = []
while True:
    try:
        node = int(input())
        tree.append(node)
    except:
        break

post_order(0, len(tree) - 1)