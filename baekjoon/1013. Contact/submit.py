for _ in range(int(input())):
    s = input()
    flag = True

    while flag and s:
        if s[:2] == '01':
            s = s[2:]
        elif s[:3] == '100':
            s = s[3:]
            i = s.find('1')

            if i >= 0:
                j = s[i+1:].find('0') + i + 1

                if j > i:
                    if i + 1 == j or s[j:j+2] == '01':
                        s = s[j:]
                    else:
                        s = s[j-1:]
                else:
                    s = ''
            else:
                flag = False
        else:
            flag = False

    print('YES' if flag else 'NO')