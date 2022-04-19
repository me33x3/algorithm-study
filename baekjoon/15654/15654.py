from itertools import permutations

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

for permute in list(permutations(arr, m)):
    print(' '.join(map(str, permute)))