input_list = list()
for i in range(10):
  i = int(input()) % 42
  input_list.append(i)
print(len(set(input_list)))