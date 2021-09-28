question_count = int(input())

for i in range(question_count):
    cnt = 0
    total_cnt = 0
    question_array = list(input())
    for j in question_array:

        if j == "O":
            cnt += 1
            total_cnt += cnt
        else:
            cnt = 0
    print(total_cnt)


