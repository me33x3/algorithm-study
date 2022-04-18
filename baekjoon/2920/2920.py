n = list(map(int, input().split()))

c_major = list(range(1, 9))
if c_major == n:
    print('ascending')
elif c_major[::-1] == n:
    print('descending')
else:
    print('mixed')