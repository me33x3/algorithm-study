import sys
input = sys.stdin.readline

def check():
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1][:len(numbers[i])]:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    numbers = sorted([input().strip() for _ in range(int(input()))])
    print(check())