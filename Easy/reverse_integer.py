# https://leetcode.com/problems/reverse-integer/
#

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """      
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        x_str = str(x)
        rev_str = ""
        for i in range(len(x_str)-1,-1,-1):
            rev_str += x_str[i]
        x = int(rev_str)
        
        if x > 2147483647 or x < -2147483647:
            return 0
        if is_negative:
            x *= -1
        return x



s = Solution()
print s.reverse(123)
print s.reverse(-123)
print s.reverse(120)