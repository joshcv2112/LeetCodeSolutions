# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/
# PASSED

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    digits = break_digits(n)
    found_happy_number = False
    for i in range(0, 10):
        digits = break_digits(n)
        n = get_magic_number(digits)
        print n
        if n == 1:
            return True

def break_digits(n):
    n_str = str(n)
    digit_arr = []
    for i in range(0, len(n_str)):
        digit_arr.append(int(n_str[i]))
    return digit_arr

def get_magic_number(digits):
    sq_sum = 0
    for d in digits:
        sq_sum += (d * d)
    return sq_sum

isHappy(19)