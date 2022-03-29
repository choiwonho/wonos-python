import math
from itertools import combinations


def is_prime(sum_num):
    # 2부터 sum_num의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(sum_num)) + 1):
        # sum_num이 해당 수로 나뉘어지면
        if sum_num % i == 0:
            return False
    return True


def solution(nums):
    list_num = list(combinations(nums, 3))

    prime_list = []
    for i in list_num:
        if is_prime(sum(i)):
            prime_list.append(sum(i))

    return len(prime_list)