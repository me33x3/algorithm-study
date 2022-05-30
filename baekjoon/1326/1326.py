from collections import deque

def bfs():
    visited = [False] * n
    visited[a] = True

    queue = deque([[a, 0]])
    while queue:
        pos, jump = queue.popleft()

        for i in range(n):
            if not visited[i] and abs(pos - i) % stones[pos] == 0:
                if i == b:
                    return jump + 1

                visited[i] = True
                queue.append([i, jump + 1])

    return -1

n = int(input())
stones = list(map(int, input().split()))
a, b = map(lambda x: int(x) - 1, input().split())

print(bfs())