# Instructions
# Given a string of digits, calculate the largest product for a contiguous substring of digits of length n.
# For example, for the input '1027839564', the largest product for a series of 3 digits is 270 (9 * 5 * 6), and the largest product for a series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).
# Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically consecutive.
# For the input '73167176531330624919225119674426574742355349194934', the largest product for a series of 6 digits is 23520.
# For a series of zero digits, the largest product is 1 because 1 is the multiplicative identity. (You don't need to know what a multiplicative identity is to solve this problem; it just means that multiplying a number by 1 gives you the same number.)

input = '1027839564'


def digit(input, digit):
    x = []
    answer = 0
    for nums in input:
        x.append(int(nums))
    print(x)
    for i in range(0, len(x)):
        m = 1
        for j in range(0, digit):
            if (i+j >= len(x)):
                m *= 1
            else:
                m *= x[i+j]
        if m > answer:
            answer = m
    return answer


print(digit(input, 3))
