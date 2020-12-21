# A = 고정비용, B = 가변비용, C = 가격
A, B, C = map(int, input().split())
'''
이익(E) = (1대 당 가격 C - 1대 당 생산비 B) * k 대 - 고정 비용 A
E = (C - B) * k - A
'''
if B >= C:
    print(-1)
else:
    print(int(A // (C - B) + 1))

