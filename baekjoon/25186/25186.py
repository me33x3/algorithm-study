n = int(input())
d = list(map(int, input().split()))
S = sum(d)
print('Happy' if S == 1 or S // 2 >= max(d) else 'Unhappy')