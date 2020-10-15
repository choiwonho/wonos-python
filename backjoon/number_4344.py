question_count = int(input())

for x in range(question_count):
    second_data = list(map(int, input().split(" ")))
    student_count = second_data[0]
    total_score = sum(second_data) - student_count
    average = int(total_score / student_count)
    ratio_cnt = 0
    for i in range(1, student_count + 1):
        if second_data[i] > average: ratio_cnt += 1

    ratio = '%.3f' %  round(float(ratio_cnt / student_count) * 100, 3)
    print(str(ratio) + "%")
