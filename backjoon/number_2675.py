    T = int(input())

    for i in range(T):
        R,S = input().split(" ")
        new_word = ""
        for word in S:
            new_word += word * int(R)



        print (new_word)

