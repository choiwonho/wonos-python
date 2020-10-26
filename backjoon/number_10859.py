from string import ascii_lowercase
S = input().lower()

alphabet_list = list(ascii_lowercase)

for i in alphabet_list:
    try:
        print(S.index(i), end=' ')
    except:
        print(-1, end=" ")