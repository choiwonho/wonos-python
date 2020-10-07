from collections import Counter

A = int(input())
B = int(input())
C = int(input())

mulriply_result = A * B * C

result = Counter(str(mulriply_result))

for i in range(10):
  print(result[str(i)])