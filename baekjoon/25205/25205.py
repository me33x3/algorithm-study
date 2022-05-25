n = int(input())
s = input()
vowels = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm'}
print(0 if s[-1] in vowels else 1)