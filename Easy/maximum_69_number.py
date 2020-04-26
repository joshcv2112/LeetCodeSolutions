# https://leetcode.com/problems/maximum-69-number/submissions/
# Solved

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        flag = False
        new_str = ""
        for i in range(len(num_str)):
            if num_str[i] == "6" and not flag:
                new_str += "9"
                flag = True
            else:
                new_str += num_str[i]
        return int(new_str)
                


s = Solution()
print (s.maximum69Number(9669))
print (s.maximum69Number(9996))
print (s.maximum69Number(9999))