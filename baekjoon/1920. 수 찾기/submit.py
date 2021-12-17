import sys
input = sys.stdin.readline

def search(num):
    left, right = 0, N - 1
    mid = (left + right) // 2

    while left <= right:
        if A[mid] < num:
            left = mid + 1
        elif A[mid] > num:
            right = mid - 1
        else:
            return 1

        mid = (left + right) // 2

    return 0

N = int(input())
A = list(map(int, input().split()))
input()

A.sort()
for i in list(map(int, input().split())):
    print(search(i))