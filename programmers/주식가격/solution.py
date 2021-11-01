def solution(prices):
    N = len(prices)
    answer = list(range(N - 1, -1, -1))

    for i in range(N - 1):
        for j in range(i, N):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break

    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([5, 8, 6, 2, 4, 1])) # [3, 1, 1, 2, 1, 0]