N = int(input())
cnt = 0

for i in range(N):
    word = input().strip()
    check = True
    for index in range(len(word) - 1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]):
                check = False
    if check is True:
        cnt += 1


print (cnt)