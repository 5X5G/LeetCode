#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

class Solution:
    def reverse(self, x: int) -> int:
        numstr = str(x)
        nums = 0
        for index in range(len(numstr)):
            if(x<0 and index == 0):
                continue
            if(numstr[index] != "0"):
                numstr = numstr[index:len(numstr)]
                break
        for index in range(len(numstr)):
            nums += int(numstr[index])*pow(10,index)
        if(nums < -pow(2,31) or nums > pow(2,31)-1):
            return 0
        if(x < 0):
            return 0-nums
        else:
            return nums

