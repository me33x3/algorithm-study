from itertools import combinations

def solution(orders, course):
    candidates = {}

    for order in orders:
        for n in course:
            if n > len(order):
                break
            for item in list(combinations(order, n)):
                key = ''.join(item)

                if key in candidates:
                    candidates[key] += 1
                else:
                    candidates[key] = 1

    return [k for k, v in candidates.items() if v > 1]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4])) # ["WX", "XY"]