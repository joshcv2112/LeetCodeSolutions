# https://leetcode.com/problems/fizz-buzz/
# SOLVED

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                arr.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                arr.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                arr.append('FizzBuzz')
            else:
                arr.append(str(i))
        return arr

s = Solution()
print (s.fizzBuzz(50))