# https://leetcode.com/problems/remove-vowels-from-a-string/submissions/
# SOLVED

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = ''
        for char in S:
            if (char not in vowels):
                result += char
        return result