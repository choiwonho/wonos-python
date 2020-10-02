number = int(input())
second = input().split(" ")
second = list(map(int, second))

sort_data = sorted(second)

min_data = sort_data[0]
max_data = sort_data[-1]

print(str(min_data) + " " + str(max_data))