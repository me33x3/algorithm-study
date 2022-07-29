from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()

        for i, coord in enumerate(coords):
            if not v[i]:
                nx, ny = coord
                dist = abs(x - nx) + abs(y - ny)

                if dist <= 1000:
                    v[i] = 1
                    queue.append([nx, ny])

        if v[-1]:
            return "happy"

    return "sad"

for _ in range(int(input())):
    n = int(input())

    queue = deque([list(map(int, input().split()))])
    coords = [list(map(int, input().split())) for _ in range(n + 1)]
    v = [0] * (n + 1)

    print(bfs())