import sys
input = sys.stdin.readline

n, m = map(int, input().split())

base = set()
for _ in range(n):
    base.add(input().rstrip())

cnt = 0
for _ in range(m):
    target = input().rstrip()
    if target in base:
        cnt += 1

print(cnt)