from collections import deque

def bfs(r, c, d):
    queue = deque([[r, c, d]])
    t = 0

    while queue:
        r, c, d = queue.popleft()
        t += 1

    print(queue)

h, w = map(int, input().split())

# 0123 북동남서
r, c, d = map(int, input().split())

floor = [list(map(int, input().split())) for _ in range(h)]
print(bfs())