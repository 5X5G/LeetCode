#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

"""
idea
栈的思想：后进先出
第一遍熟练度不高，转成字符串来运算，但是耗费内存比较多
第二遍考虑直接用数字来操作，但是还是需要2个变量分别来存放正负和下标
"""

#first
# class Solution:
#     def reverse(self, x: int) -> int:
#         numstr = str(x)
#         nums = 0
#         for index in range(len(numstr)):
#             if(x<0 and index == 0):
#                 continue
#             if(numstr[index] != "0"):
#                 numstr = numstr[index:len(numstr)]
#                 break
#         for index in range(len(numstr)):
#             nums += int(numstr[index])*pow(10,index)
#         if(nums < -pow(2,31) or nums > pow(2,31)-1):
#             return 0
#         if(x < 0):
#             return 0-nums
#         else:
#             return nums

#second
class Solution:
    def reverse(self, x: int) -> int:
        nonPositive = x>=0
        x= abs(x)
        nums = 0
        while x%10 == 0 and x != 0:
            x //= 10        
        while x != 0:
            nums += x%10 *pow(10,len(str(x))-1)
            x//=10
        if(not nonPositive):
            nums =0-nums  
        if(nums < -pow(2,31) or nums > pow(2,31)-1):
            return 0
        else:
            return nums
            

