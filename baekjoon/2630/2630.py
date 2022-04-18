def solution(x, y, n):
    color = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                solution(x, y, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return

    res[color] += 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0]

solution(0, 0, n)
print(res[0])
print(res[1])