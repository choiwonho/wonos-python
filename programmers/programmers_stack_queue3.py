'''
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
'''

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    # 대기 트럭  deque([7, 4, 5, 6])
    truck_weights_deque = deque(truck_weights)

    # 다리 위에 올라갈 수 있는 길이 (예시 2 이므로  deque([0, 0]))
    trucks_on_bridge_deque = deque([0] * bridge_length)

    # deque([0, 7])  <- answer 초기값이 1인 이유 (한번 이동했기 때문)
    trucks_on_bridge_deque[-1] = truck_weights_deque.popleft()

    # deque 만큼 반복
    while truck_weights_deque:
        if sum(trucks_on_bridge_deque) - trucks_on_bridge_deque[0] + truck_weights_deque[0] > weight:
            trucks_on_bridge_deque.popleft()
            trucks_on_bridge_deque.append(0)
            answer = answer + 1
        else:
            trucks_on_bridge_deque.popleft()
            trucks_on_bridge_deque.append(truck_weights_deque.popleft())
            answer = answer + 1

            # 마지막 남아있는 다리위에 있는 트럭이 다 지나가게 하기 위해서
    answer = answer + bridge_length

    return answer

if __name__ == "__main__":
  truck_weights = [7, 4, 5, 6]
  solution(2, 10, truck_weights)