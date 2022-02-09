N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

answer = 8 * 8

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        tmp = [0, 0]

        for k in range(8):
            idx = k % 2

            for target, a, b in zip(board[i + k][j:j + 8], list('WBWBWBWB'), list('BWBWBWBW')):
                if target != a:
                    tmp[idx] += 1

                if target != b:
                    tmp[idx - 1] += 1

        answer = min(answer, tmp[0], tmp[1])

print(answer)