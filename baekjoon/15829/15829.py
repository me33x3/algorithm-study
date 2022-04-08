L = int(input())
S = input()

answer = 0
for i in range(L):
    answer += (ord(S[i]) - 96) * (31 ** i) % 1234567891
print(answer)