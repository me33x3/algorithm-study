def solution(n, times):
    times.sort()
    left, right = 1, times[-1] * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        t = sum([mid // time for time in times])

        if t < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = min(answer, mid)

    return answer

print(solution(6, [7, 10])) # 28