def dfs(idx, pwd):
    for i in range(idx, C - (L - len(pwd)) + 1):
        tmp = pwd + alphas[i]

        if len(tmp) == L:
            cnt = [0, 0]
            for ch in tmp:
                if ch in vowels:
                    cnt[0] += 1
                else:
                    cnt[1] += 1

                if cnt[0] >= 1 and cnt[1] >= 2:
                    print(tmp)
                    break
        else:
            dfs(i + 1, tmp)

L, C = map(int, input().split())
alphas = sorted(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
dfs(0, '')