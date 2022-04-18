def dfs(stack):
    while stack:
        x, y = stack.pop()

        if x == C - 1:
            return True

        for dy in [-1, 0, 1]:
            mx = x + 1
            my = y + dy

            if mx < C and 0 <= my < R and board[my][mx] != 'x' and not visited[my][mx]:
                visited[my][mx] = True
                stack.append([mx, my])
                if dfs(stack):
                    return True

    return False

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

answer = 0

for i in range(R):
    if dfs([[0, i]]):
        answer += 1

print(answer)