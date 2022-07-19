import sys
inf = sys.maxsize

def floyd_warshall():
    for i in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                board[a][b] = min(board[a][b], board[a][i] + board[i][b])

for _ in range(int(input())):
    N, M = map(int, input().split())

    board = [[inf] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        board[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        board[a][b] = board[b][a] = c

    floyd_warshall()

    K = int(input())
    room = list(map(int, input().split()))

    answer, val = 0, inf

    for i in range(1, N + 1):
        tmp = 0
        for j in room:
            tmp += board[j][i]

        if tmp < val:
            val = tmp
            answer = i

    print(answer)