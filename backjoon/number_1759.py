from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

# 가능한 암호를 사전순으로 정렬
array = input().split(' ')
array.sort()

# 길이가 1인 모든 암호 조합을 확인
for password in combinations(array, l):
    # 모음의 개수 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1


    # 최소 한 개의 모음과 두 개의 자음이 있는 경우 출력
    if count >= 1 and count <= l -2:
        print(''.join(password))