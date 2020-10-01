number = int(input())
if number < 10:
    a, b = 0, str(number)
else:
    a, b = str(number)[0], str(number)[-1]

result = int(a) + int(b)

sum_number = str(result)

count = 1
while True:

    if int(sum_number) == 0:
        break

    a, b = int(b), sum_number[-1]

    result = int(a) + int(b)
    sum_number = str(result)
    check_result = str(a) + str(b)
    if number == int(check_result):
        break
    else:
        count += 1
        continue

print(count)