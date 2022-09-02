n = int(input())
data = [list(input()) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
answer = 'YES'

for i in range(n):
    for j in range(n):
        if data[i][j] == 'Y' and data[j][i] == 'N':
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] and dist[k][j]:
                dist[i][j] = 1

for i in range(n):
    if dist[i][i]:
        answer = 'NO'
        break

print(answer)