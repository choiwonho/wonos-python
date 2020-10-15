def solution(array, commands):
    answer = []
    for i in commands:
        temp_array = array[i[0] - 1  : i[1]]
        temp_array = sorted(temp_array)
        find_index = i[-1] - 1
        answer.append(temp_array[find_index])

    return answer


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    result = solution(array, commands)
    print(result)