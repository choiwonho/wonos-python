'''
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
'''

'''
from itertools import permutations

def solution(numbers):
    convert_to_string = list(map(str, numbers))
    combination_data = list(map(''.join, permutations(convert_to_string)))
    convert_to_int = list(map(int, combination_data))
    max_num = max(convert_to_int)

    return str(max_num)

'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    numbers = [6, 10, 2]
    solution(numbers)