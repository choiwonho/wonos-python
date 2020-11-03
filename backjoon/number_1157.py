from collections import Counter
word = list(map(str, input().strip().upper()))
count = Counter(word).most_common(1)

check_count = Counter(word).most_common(2)

if check_count[0][1] == check_count[1][1]:
    result = "?"
else:
    result = check_count[0][0].upper()

print(result)

