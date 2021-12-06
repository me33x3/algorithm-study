def solution1(numbers, hand):
    answer = ""
    numpad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    curr = [[0, 3], [2, 3]]
    for num in numbers:
        if num in numpad[0]:
            answer += "L"
            curr[0] = [0, numpad[0].index(num)]
        elif num in numpad[2]:
            answer += "R"
            curr[1] = [2, numpad[2].index(num)]
        else:
            pos = [1, numpad[1].index(num)]
            l, r = abs(pos[0] - curr[0][0]) + abs(pos[1] - curr[0][1]), abs(pos[0] - curr[1][0]) + abs(pos[1] - curr[1][1])

            if l < r or (l == r and hand == "left"):
                answer += "L"
                curr[0] = pos
            else:
                answer += "R"
                curr[1] = pos
    return answer

def solution2(numbers, hand):
    numbers = [11 if num == 0 else num for num in numbers]
    l_i, r_i = 10, 12
    left, mid, right = [1, 4, 7], [2, 5, 8, 0], [3, 6, 9]
    answer = ''

    for num in numbers:
        if num in left:
            answer += 'L'
            l_i = num
        elif num in right:
            answer += 'R'
            r_i = num
        else:
            x, y = divmod(num - 1, 3)
            l_x, l_y = divmod(l_i - 1, 3)
            r_x, r_y = divmod(r_i - 1, 3)

            l_d, r_d = abs(l_x - x) + abs(l_y - y), abs(r_x - x) + abs(r_y - y)

            if l_d > r_d or (l_d == r_d and hand=="right"):
                answer += 'R'
                r_i = num
            else:
                answer += 'L'
                l_i = num
    return answer

# solution1
print(solution1([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution1([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"

# solution1
print(solution2([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution2([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"