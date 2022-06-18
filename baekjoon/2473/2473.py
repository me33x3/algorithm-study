import sys

n = int(input())
liquids = sorted(map(int, input().split()))

m = sys.maxsize
answer = [0, 0, 0]

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        s = liquids[i] + liquids[left] + liquids[right]

        if m > abs(s):
            m = abs(s)
            answer = [liquids[i], liquids[left], liquids[right]]

        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            break

print(*answer)