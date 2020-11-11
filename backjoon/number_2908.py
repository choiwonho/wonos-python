A, B = list(map(str, input().split()))

compare_a = ''.join(reversed(A))
compare_b = ''.join(reversed(B))

result = ''
if int(compare_a) > int(compare_b):
    result = compare_a
else:
    result = compare_b

print(result)