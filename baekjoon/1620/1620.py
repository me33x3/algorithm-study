import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book = {}

for i in range(1, n + 1):
    book[input().rstrip()] = i
keys = list(book.keys())

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(keys[int(q) - 1])
    else:
        print(book[q])