def get_min(out_t, in_t):
    out_h, out_m = map(int, out_t.split(':'))
    in_h, in_m = map(int, in_t.split(':'))
    return (out_h * 60 + out_m) - (in_h * 60 + in_m)

def solution(fees, records):
    d, res = {}, {}
    answer = []

    for record in records:
        t, num, st = record.split()

        if st == 'IN':
            d[num] = t
        else:
            if num in res:
                res[num] += get_min(t, d[num])
            else:
                res[num] = get_min(t, d[num])
            del d[num]

    for num, t in d.items():
        if num in res:
            res[num] += get_min("23:59", t)
        else:
            res[num] = get_min("23:59", t)

    for num in sorted(res.keys()):
        answer.append(fees[1])
        res[num] -= fees[0]

        if res[num] > 0:
            answer[-1] += res[num] // fees[2] * fees[3]
            answer[-1] += fees[3] if res[num] % fees[2] else 0

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) # [0, 591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"])) # [14841]