N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cards.sort()
for num in nums:
    l, r = 0, N - 1
    while l <= r:
        m = (l + r) // 2

        if num > cards[m]:
            l = m + 1
        elif num < cards[m]:
            r = m - 1
        else:
            print('1', end=' ')
            break
    if l > r: print('0', end=' ')
