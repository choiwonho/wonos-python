'''
문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.


스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
'''

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


if __name__ == "__main__":
    arr = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    data = solution(arr)
    print(data)

