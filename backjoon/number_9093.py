T = int(input())

def reverse(sentence):
    words = list(sentence.split())
    reverse_sentence = list()

    for word in words:
        reverse_sentence.append(word[::-1])

    result = " ".join(reverse_sentence)

    return result



for _ in range(T):
    sentence = input().rstrip()
    print(reverse(sentence))