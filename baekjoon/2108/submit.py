import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = sorted(int(input()) for _ in range(n))
most = Counter(nums).most_common(2)

print(round(sum(nums) / n))
print(nums[n // 2])
print(most[1][0] if n > 1 and most[0][1] == most[1][1] else most[0][0])
print(nums[-1] - nums[0])