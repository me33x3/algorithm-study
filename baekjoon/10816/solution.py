import sys
input = sys.stdin.readline

def lower(n, l, r):
    tmp = r
    while l <= r:
        m = (l + r) // 2
        if n > cards[m]: l = m + 1
        else: r = m - 1

    return tmp - l + 1  if cards[l] == n else 0

def upper(n, l, r):
    tmp = l
    while l <= r:
        m = (l + r) // 2
        if n < cards[m]: r = m - 1
        else: l = m + 1

    return r - tmp + 1 if cards[r] == n else 0


N = int(input())
cards = list(map(int, input().split()))
input()
nums = list(map(int, input().split()))

cards.sort()
for num in nums:
    l, r = 0, N - 1
    cnt = 0

    while l <= r:
        m = (l + r) // 2

        if num > cards[m]:
            l = m + 1
        elif num < cards[m]:
            r = m - 1
        else:
            cnt = lower(num, l, m - 1) + upper(num, m + 1, r) + 1
            break
    print(cnt, end=' ')