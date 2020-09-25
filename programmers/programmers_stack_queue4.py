'''
문제 설명
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.
'''


def solution(priorities, location):
    answer = 0

    # 인쇄 대기목록이 남아있다면 반복
    while len(priorities) != 0:
        # 1. 대기목록의 가장 앞에있는 문서가 나머지 문서들보다 중요도가 높은 경우
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)  # 먼저 인쇄 == 가장 앞에있는 것 삭제
            if location == 0:
                return answer
            else:
                location -= 1
        # 2. 대기목록의 가장 앞에있는 문서가 중요도가 가장 높지 않은 경우
        else:
            priorities.append(priorities.pop(0))  # 문서를 대기목록 맨 뒤로 이동
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer



if __name__ == '__main__':
    priorities = [2, 1, 3, 2] #[1, 1, 9, 1, 1, 1]
    location = 2
    result = solution(priorities, location)
    print(result)