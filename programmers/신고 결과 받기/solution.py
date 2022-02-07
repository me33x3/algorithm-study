def solution(id_list, report, k):
    d = dict(zip(id_list, [[] for _ in range(len(id_list))]))
    count = dict(zip(id_list, [0 for _ in range(len(id_list))]))

    for line in report:
        id, target = line.split()
        if target not in d[id]:
            d[id].append(target)
            count[target] += 1

    return [sum([1 for user in d[id] if count[user] >= k]) for id in id_list]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # [0, 0]