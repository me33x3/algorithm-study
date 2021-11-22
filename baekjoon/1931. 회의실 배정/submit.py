import sys
input = sys.stdin.readline

N = int(input())

conferences = []
for _ in range(N):
    conferences.append(list(map(int, input().split())))

conferences.sort(key=lambda x:(x[1], x[0]))
res, end = 0, 0

for c in conferences:
    if end <= c[0]:
        end = c[1]
        res += 1

print(res)