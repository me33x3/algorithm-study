import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

l, r = 1, max(trees)
while l <= r:
    m = (l + r) // 2
    len = sum([tree - m if tree - m > 0 else 0 for tree in trees])

    if M <= len:
        l = m + 1
    else:
        r = m - 1

print(r)