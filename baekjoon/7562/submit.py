from collections import deque

def bfs(I, current, target):
    dx, dy = [-2, -1, 1, 2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]
    board = [[0] * I for _ in range(I)]

    res = 0
    queue = deque([current])

    while queue:
        cx, cy = queue.popleft()

        if [cx, cy] == target:
            print(board[cy][cx])
            break

        for x, y in zip(dx, dy):
            mx, my = cx + x, cy + y

            if 0 <= mx < I and 0 <= my < I and not board[my][mx]:
                board[my][mx] = board[cy][cx] + 1
                queue.append([mx, my])

for _ in range(int(input())):
    bfs(int(input()), list(map(int, input().split())), list(map(int, input().split())))