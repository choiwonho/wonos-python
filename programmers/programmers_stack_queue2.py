'''
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
'''
from collections import deque
from operator import add


def solution(progresses, speeds):
    answer = []

    que_progresses = deque(progresses)  # 작업 개수 리스트를 큐로 변환
    que_speeds = deque(speeds)  # 작업 속도 리스트를 큐로 변환

    while que_progresses:
        count = 0  # 배포마다 기능이 몇 개인지 저장하는 변수
        que_len = len(que_progresses)

        # 기능 개발이 한개만 남았을 경우 날짜와 상관없이 무조건
        # 하나만 배포하므로 answer에 1을 추가해주고 종료
        if que_len == 1:
            answer.append(1)
            break

        # 개발 진행도 + 개발 속도 -> 개발 진행도 갱신
        que_progresses = deque(map(add, que_progresses, que_speeds))

        # 개발진행이 완료 되었으면 배포
        while que_progresses:
            if que_progresses[0] >= 100:
                que_progresses.popleft()
                que_speeds.popleft()
                count += 1
            else:
                break

        if count != 0:
            answer.append(count)
    print(answer)
    return answer


if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    solution(progresses,speeds)