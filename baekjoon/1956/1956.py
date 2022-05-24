import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
matrix = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

res = min([matrix[i][i] for i in range(1, V + 1)])
print(-1 if res == INF else res)