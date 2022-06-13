import collections

def solution(particpant, complection):
    answer = collections.Counter(particpant) - collections.Counter(complection)
    print (answer)
    return list(answer.keys())[0]