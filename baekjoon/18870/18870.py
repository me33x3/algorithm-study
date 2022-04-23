import sys
input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))
d = {key:val for val, key in enumerate(sorted(set(coords)))}

for coord in coords:
    print(d[coord], end=' ')