def solution(record):
    message = []
    user = dict()
    printer = { 'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for log in record:
        log = log.split(' ')
        if log[0] != 'Leave':
            user[log[1]] = log[2]

    for log in record:
        status, id = log.split(' ')[:2]
        if status != 'Change':
            message.append(user[id] + printer[status])

    return message

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])) # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
# print(solution(["Enter uid0606 Gimoi", "Enter uid4567 Prodo", "Leave uid0606", "Enter uid1234 Prodo", "Change uid1234 OhYeah"]))