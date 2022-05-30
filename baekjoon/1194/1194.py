from collections import deque

def bfs():
    while queue:
        x, y, key, move = queue.popleft()

        for nx, ny in zip(dx, dy):
            mx, my = x + nx, y + ny
            tmp_key = key

            if 0 <= mx < n and 0 <= my < m and maze[mx][my] != '#' and not visited[mx][my][key]:
                has_key = True
                if maze[mx][my] == '1':
                    return move + 1
                elif maze[mx][my].isupper():
                    has_key = key & (1 << ord(maze[mx][my]) - ord('A'))
                elif maze[mx][my].islower():
                    tmp_key = key | (1 << ord(maze[mx][my]) - ord('a'))

                if has_key:
                    visited[mx][my][tmp_key] = True
                    queue.append([mx, my, tmp_key, move + 1])

    return -1

n, m = map(int, input().split())
maze = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[[False] * 64 for _ in range(m)] for _ in range(n)]
queue = deque([])
for i in range(n):
    maze.append(list(input()))
    for j in range(m):
        if maze[-1][j] == '0':
            queue.append([i, j, 0, 0])
            visited[i][j][0] = True
print(bfs())