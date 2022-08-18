from copy import deepcopy

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def dfs(board, depth):
    global answer

    if depth == len(cctv):
        answer = min(answer, sum(board[i].count(0) for i in range(n)))
        return

    x, y = cctv[depth]
    num = board[x][y]

    for directions in cctv_direction[num]:
        board_copy = deepcopy(board)

        for d in directions:
            nx, ny = x, y

            while True:
                nx += dx[d]
                ny += dy[d]

                if 0 <= nx < n and 0 <= ny < m and board_copy[nx][ny] != 6:
                    if not board_copy[nx][ny]:
                        board_copy[nx][ny] = '#'
                else:
                    break

        dfs(board_copy, depth + 1)

n, m = map(int, input().split())
board, cctv = [], []
answer = int(1e9)

for i in range(n):
    board.append(list(map(int, input().split())))

    for j in range(m):
        if 0 < board[i][j] < 6:
            cctv.append([i, j])

dfs(board, 0)
print(answer)