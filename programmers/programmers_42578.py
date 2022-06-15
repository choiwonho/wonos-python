from collections import Counter


def solution(clothes):
    # 일단 각 카테고리(모자, 안경, 상의 등)별로 아이템의 갯수를 구한다.
    counter_each_category = Counter([categoty for _, categoty in clothes])
    # Counter({'headgear': 2, 'eyewear': 1})
    all_possible = 1
    # 각 카테고리별로 가지고있는 아이템의 수에 1을 더해서 다 곱해준다.
    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)

    # 모든 경우의 수에서 아무런 아이템도 착용하지 않는 경우 하나를 빼고 리턴해준다
    return all_possible - 1