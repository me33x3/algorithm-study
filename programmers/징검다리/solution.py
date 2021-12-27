def solution(distance, rocks, n):
    rocks.extend([0, distance])
    rocks.sort()

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        curr, cnt = 0, 0

        for i in range(1, len(rocks)):
            if rocks[i] - curr < mid:
                cnt += 1
            else:
                curr = rocks[i]

        if n >= cnt:
            left = mid + 1
        else:
            right = mid - 1

    return right

print(solution(25, [2, 14, 11, 21, 17], 2)) # 4