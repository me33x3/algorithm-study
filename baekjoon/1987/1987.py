import sys
input = sys.stdin.readline


def dfs(x, y, move):
    global answer
    answer = max(move, answer)
    for i in range(4):
        mx, my = x + dx[i], y + dy[i]

        if 0 <= mx < C and 0 <= my < R and not visited[board[my][mx]]:
            visited[board[my][mx]] = True
            dfs(mx, my, move + 1)
            visited[board[my][mx]] = False

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
visited = [False] * 26
visited[board[0][0]] = True
answer = 0

dx, dy = [0, 0, -1 , 1], [-1, 1, 0, 0]
dfs(0, 0, 1)
print(answer)