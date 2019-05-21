#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

#first
# class Solution(object):
#     def twoSum(self, nums, target):
#         for index1 in range(len(nums)):
#             for index2 in range(len(nums)):
#                 if(index2 > index1 ):
#                     sum = nums[index1] + nums[index2]
#                     if(sum == target):
#                         return [index1,index2]

# second                 
class Solution(object):
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            num = nums[index]
            if target-num in nums and nums.index(target-num) != index:
                return [index,nums.index(target-num)]
