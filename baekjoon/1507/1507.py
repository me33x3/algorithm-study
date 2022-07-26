N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
chk = [[1] * N for _ in range(N)]

for i in range(N):
    for a in range(N):
        for b in range(N):
            if i == a or i == b or a == b:
                continue

            tmp = graph[a][i] + graph[i][b]
            if graph[a][b] == tmp:
                chk[a][b] = 0
            elif graph[a][b] > tmp:
                print(-1)
                exit()

answer = 0

for i in range(N):
    for j in range(i, N):
        if chk[i][j]:
            answer += graph[i][j]

print(answer)