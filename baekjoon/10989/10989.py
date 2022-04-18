import sys
input = sys.stdin.readline

n = int(input())
count_list = [0] * 10001

for _ in range(n):
    count_list[int(input())] += 1

for i in range(1, 10001):
    for _ in range(count_list[i]):
        print(i)