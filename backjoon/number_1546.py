subject_count = int(input())
subject_score = list(map(int, input().split(" ")))

max_score = max(subject_score)
lie_score = list()
total_score = 0
for i in subject_score:
    total_score += (i/max_score*100)

print(total_score/subject_count)
