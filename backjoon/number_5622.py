dial_str = input().strip()

dial_alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in dial_str:
    for j in dial_alphabet:
        if i in j:
            result += dial_alphabet.index(j) + 3
print(result)
