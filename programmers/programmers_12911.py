def solution(n):
    bin_n = format(n, 'b')
    count_one = bin_n.count('1')
    big_num = n + 1

    while True:

        bin_big_num = format(big_num, 'b')

        if bin_big_num.count('1') == count_one:
            break

        big_num += 1

    return big_num