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

    return answer