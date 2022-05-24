import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for i in range(1, n + 1):
    print(n - sum([matrix[i][j] + matrix[j][i] for j in range(1, n + 1)]) - 1)