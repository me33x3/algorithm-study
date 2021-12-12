import re

def solution(new_id):
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id.lower())
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = new_id[:15] if new_id else 'a'
    new_id = re.sub('[.]$', '', new_id)
    new_id = new_id if len(new_id) >= 3 else new_id + ''.join([new_id[-1] for _ in range(3 - len(new_id))])

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
print(solution("z-+.^.")) # "z--"
print(solution("=.=")) # "aaa"
print(solution("123_.def")) # "123_.def"
print(solution("abcdefghijklmn.p")) # "abcdefghijklmn"