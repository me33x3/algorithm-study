MAX = 50

n = int(input())
graph = [[MAX] * (n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

while True:
    x, y = map(lambda x: int(x) - 1, input().split())
    if x < 0:
        break
    graph[x][y] = graph[y][x] = 1

for i in range(n):
    for x in range(n):
        for y in range(n):
            graph[x][y] = min(graph[x][y], graph[x][i] + graph[i][y])

_max = MAX
candidate = []

for i in range(n):
    tmp = max(graph[i])
    if tmp < _max:
        candidate = [i + 1]
        _max = tmp
    elif tmp == _max:
        candidate.append(i + 1)

print(_max, len(candidate))
print(*candidate)