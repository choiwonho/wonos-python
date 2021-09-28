n = int(input())

result_num = 99

if len(str(n)) < 3:
    print(n)
else:
    for x in range(100, n+1):
        result = list(map(int, str(x)))
        if result[0] - result[1] == result[1] - result[2]:
            result_num += 1

    print(result_num)




