# 완주하지 못한 선수
import collections

def solution(particpant, complection):
    answer = collections.Counter(particpant) - collections.Counter(complection)
    return list(answer.keys())[0]