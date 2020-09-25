N,X = list(map(int, input().split()))
A = list(map(int, input().split()))

#A = list(map(int, input().split()))
#A = random.sample(range(1, 10001), int(N))

result_list = []

for i in A:
  if(i < X): print(i, end = ' ')