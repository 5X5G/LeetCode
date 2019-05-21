#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

"""
idea   
循环遍历nums,使用一个哈希表来存储<每个值所需要匹配的值，自身下标>，
然后依次遍历，每次nums中的值都会与哈希表做包含判断，自己的index()方法耗费太多time了
"""

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
