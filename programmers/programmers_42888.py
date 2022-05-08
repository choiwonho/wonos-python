def solution(record):
    id_dic = {}
    answer = []

    for change in record:
        id_dic[change.split()[1]] = change.split()[-1]

    for message in record:
        if "Enter" in message:
            answer.append(id_dic[message.split()[1]] + "님이 들어왔습니다.")
        elif "Leave" in message:
            answer.append(id_dic[message.split()[1]] + "님이 나갔습니다.")
        else:
            continue
    return answer