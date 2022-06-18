import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
belt.extend(belt)

d = defaultdict(int)
left, right = 0, k
kind = 0

d[c] = 1
for i in range(k):
    d[belt[i]] += 1

while right < len(belt):
    kind = max(kind, len(d))

    d[belt[left]] -= 1
    d[belt[right]] += 1

    if not d[belt[left]]:
        del d[belt[left]]

    left += 1
    right += 1

print(kind)