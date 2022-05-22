n = int(input())

graph, friends = [], []
for _ in range(n):
    graph.append(list(input()))
    friends.append(list())
    for v in graph[-1]:
        friends[-1].append(1 if v == 'Y' else 0)

for c in range(n):
    for a in range(n):
        for b in range(n):
            if a != b and graph[a][c] == 'Y' and graph[c][b] == 'Y':
                friends[a][b] = 1

print(max(map(sum, friends)))