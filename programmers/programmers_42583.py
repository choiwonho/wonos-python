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
    current_weight = 0
    while truck_weights_deque:
        current_weight -= trucks_on_bridge_deque[0]
        if current_weight + truck_weights_deque[0] > weight:
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