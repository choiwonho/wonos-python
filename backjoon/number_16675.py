ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

'''
이기는 조건 => (ML + 2) % 3
    가위 : S, 0 => 바위 : R 2
    보 : P, 1 => 가위 : S 0
    바위 : R, 2 => 보 : P 1
'''

if ML == MR and (ML + 2) % 3 in [TL, TR]:
	print("TK")
elif TL == TR and (TL + 2) % 3 in [ML, MR]:
	print("MS")
else:
	print('?')

