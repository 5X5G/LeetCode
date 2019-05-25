#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

s="AB"
print(s[1:2])

class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace('"',"")
        strMap = {"(":")", "{":"}", "[":"]"}         
        if(len(s)%2 >0):
            return False
        index = 0
        while index < len(s):
            if s[index] != strMap[s[0]]:
                index += 1
                continue
            else:
                s = s[1:index]+s[-(len(s)-1-index):]
                index = 0
        if(index == len(s)-1):
            return False
        return True

so= Solution()
so.isValid("()")
