def is_pseudo(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return chk(s, left + 1, right) or chk(s, left, right - 1)

def chk(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

for _ in range(int(input())):
    s = input()

    if s == s[::-1]:
        print(0)
    elif is_pseudo(s):
        print(1)
    else:
        print(2)