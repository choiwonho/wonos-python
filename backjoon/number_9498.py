test_result = int(input())

if(test_result >= 90 and test_result <= 100):
    print("A")
elif(test_result >= 80 and test_result < 90):
    print("B")
elif(test_result >= 70 and test_result < 80):
    print("C")
elif(test_result >=60 and test_result < 70):
    print("D")
else:
    print("F")