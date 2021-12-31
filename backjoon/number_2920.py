input_number = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if input_number[i] > input_number[i-1]:
        descending = False
    elif input_number[i] < input_number[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
