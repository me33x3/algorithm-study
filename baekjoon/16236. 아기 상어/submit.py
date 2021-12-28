from collections import deque

def bfs(curr):
    queue, visited = deque([curr]), set([(curr[0], curr[1])])
    dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1]
    shark, cnt, t, res = 2, 0, 0, 0
    eat = False

    while queue:
        size = len(queue)
        queue = deque(sorted(queue))
        for _ in range(size):
            p, q = queue.popleft()

            if 0 < board[p][q] < shark:
                queue.clear()
                visited.clear()
                board[p][q] = 0
                cnt += 1
                eat = True
                res = t
                if shark == cnt:
                    shark += 1
                    cnt = 0

            for x, y in zip(dx, dy):
                mx, my = q + x, p + y
                if 0 <= mx < N and 0 <= my < N and (my, mx) not in visited:
                    if board[my][mx] <= shark:
                        queue.append([my, mx])
                        visited.add((my, mx))

            if eat:
                eat = False
                break

        t += 1

    return res

N = int(input())
board, curr = [], []
for i in range(N):
    board.append([])
    for num in input().split():
        num = int(num)
        if num == 9:
            board[i].append(0)
            curr = [i, len(board[i]) - 1]
        else:
            board[i].append(num)
print(bfs(curr))