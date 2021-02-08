N = int(input().strip())

default_num = 6
result = 1
count = 1
number = 1

while True:
    if N > number:
        number = (default_num * count) + number
        count += 1
        result += 1
    else:
        print(result)
        break



