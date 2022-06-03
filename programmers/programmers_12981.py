def solution(n, words):
    word_list = list()
    order, rotation = 0, 0

    word_list.append(words[0])
    last_word = words[0][-1]

    for i in range(1, len(words)):
        if words[i] not in word_list and words[i][0] == last_word:
            word_list.append(words[i])
            last_word = words[i][-1]

        else:
            order = (i % n) + 1
            rotation = (i // n) + 1
            break

    return [order, rotation]