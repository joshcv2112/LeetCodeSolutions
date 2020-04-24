# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
# Solved

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = self.get_digits(n)
        product = self.get_product_of_digits(digits)
        sum = self.get_sum_of_digits(digits)
        return product - sum
        

    def get_digits(self, n):
        n_str = str(n)
        digits = []
        for digit in n_str:
            digits.append(int(digit))
        return digits
    
    def get_product_of_digits(self, digits):
        product = 1
        for digit in digits:
            product *= digit
        return product
    
    def get_sum_of_digits(self, digits):
        sum = 0
        for digit in digits:
            sum += digit
        return sum
        
s = Solution()
print s.subtractProductAndSum(234)
print s.subtractProductAndSum(4421)