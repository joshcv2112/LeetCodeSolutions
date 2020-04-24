# https://leetcode.com/problems/two-sum/
# Solved, but not optimized. Current solution is O(n) time.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

s = Solution()
print s.twoSum([2, 11, 15, 7], 9)
print s.twoSum([3, 2, 4], 6)

