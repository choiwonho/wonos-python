'''
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.
'''
import heapq

def solution(operations):
    answer = []

    while operations:
        data = operations.pop(0)

        if "I" in data:
            answer.append(int(data.split(" ")[1]))
        elif "-1" in data:
            if len(answer) == 0:
                continue
            answer.remove(min(answer))
        else:
            if len(answer) == 0:
                continue
            answer.remove(max(answer))

    if len(answer) == 0:
        result = [0,0]
    else:
        result = [max(answer), min(answer)]
    return result



if __name__ == '__main__':
    #operations = ["I 7","I 5","I -5","D -1"]
    operations = ["I 16","D 1"]
    result = solution(operations)
    print(result)