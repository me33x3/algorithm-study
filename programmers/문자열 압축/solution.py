def solution(s):
    length = len(s)
    answer = []

    answer.append(len(s))

    for i in range(1, length // 2 + 1):
        index = 0
        compress = ''

        while index < length:
            j = index + i
            tmp = s[index:j]
            count = 1

            while j <= length - i:
                if tmp == s[j:j + i]:
                    count += 1
                    j += i

                else:
                    break

            if count > 1:
                compress += str(count)
            compress += tmp
            index = j

        answer.append(len(compress))

    return min(answer)