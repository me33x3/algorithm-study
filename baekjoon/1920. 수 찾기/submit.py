import sys
input = sys.stdin.readline

input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))

for i in B:
    print(1 if i in A else 0)