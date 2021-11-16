from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v)
    graph[v-1].append(u)

def bfs():
    answer = 0
    yet, visited = list(range(1, N+1)), list()

    while yet:
        visited = [yet.pop(0)]
        queue = deque(graph[visited[0]-1])

        while queue:
            v = queue.popleft()
            if v not in visited:
                queue.extend(graph[v-1])
                visited.append(v)
                yet.remove(v)

        answer += 1

    print(answer)

bfs()