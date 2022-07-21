N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 2

for i in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][i] == 1 and graph[i][b] == 1:
                graph[a][b] = 1
            elif graph[a][i] == 2 and graph[i][b] == 2:
                graph[a][b] = 2

answer = 0

for i in range(1, N + 1):
    tmp = [0] * 3

    for j in range(1, N + 1):
        tmp[graph[i][j]] += 1

    if tmp[1] > (N // 2) or tmp[2] > (N // 2):
        answer += 1

print(answer)