# https://leetcode.com/problems/defanging-an-ip-address/
# PASSED

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defang_ip = ''
        for char in address:
            if char == '.':
                defang_ip += '[.]'
            else:
                defang_ip += char
        return defang_ip
        
s = Solution()
print s.defangIPaddr('1.1.1.1')
print s.defangIPaddr('255.100.50.0')