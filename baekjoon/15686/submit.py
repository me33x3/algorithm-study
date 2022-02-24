from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

home_list, chicken_list = [], []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home_list.append([i, j])
        elif board[i][j] == 2:
            chicken_list.append([i, j])

answer = float('inf')
for pick in combinations(chicken_list, M):
    temp = 0
    for home in home_list:
        temp += min([abs(home[0] - r) + abs(home[1] - c) for r, c in pick])
    answer = min(answer, temp)

print(answer)