import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    move = int(board[x][y])
    for d in range(4):
        nx, ny = dx[d], dy[d]
        mx, my = x + (nx * move), y + (ny * move)

        if 0 <= mx < n and 0 <= my < m and board[mx][my] != 'H' and dp[mx][my] < cnt + 1:
            if v[mx][my]:
                print(-1)
                exit()
            else:
                v[mx][my] = True
                dp[mx][my] = cnt + 1
                dfs(mx, my, cnt + 1)
                v[mx][my] = False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
v = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0
dfs(0, 0, 1)
print(answer)