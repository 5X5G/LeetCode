#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums) -> int:
        count =0
        if(len(nums) > 0):
            count = 1
        for index in range(len(nums)):
            if(index +1 < len(nums) and nums[index] != nums[index+1]):
                count += 1
        return count    

so = Solution()
so.removeDuplicates([1,1])
