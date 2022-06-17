def solution(array, commands):
    answer = []
    for i in commands:
        temp_array = array[i[0] - 1  : i[1]]
        temp_array = sorted(temp_array)
        find_index = i[-1] - 1
        answer.append(temp_array[find_index])

    return answer