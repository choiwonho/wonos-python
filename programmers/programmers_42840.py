def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]

    answer_result = []

    for idx, answer in enumerate(answers):
        if answer == person1[idx % len(person1)]:
            result[0] += 1
        if answer == person2[idx % len(person2)]:
            result[1] += 1
        if answer == person3[idx % len(person3)]:
            result[2] += 1

    for idx, score in enumerate(result):
        if score == max(result):
            answer_result.append(idx + 1)

    return answer_result