#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        for time in range(len(strX)//2):
            if(strX[time] != strX[-time-1]):
                return False
        return True
        

