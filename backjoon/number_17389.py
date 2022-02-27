N = int(input())
S = input()

bonus_point = 0
total_point = 0

for idx, i in enumerate(S):
    if i == 'O':
        total_point += (idx + 1) + bonus_point
        bonus_point += 1
    else:
        bonus_point = 0

print(total_point)