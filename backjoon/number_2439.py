N = int(input())
SPACE = " "
ASTERISK = "*"

for i in range(1, N+1):
    space_count = N - i
    print (SPACE * space_count + ASTERISK * i)

