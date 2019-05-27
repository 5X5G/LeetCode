#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

"""
栈思想
"""

class Solution:
    def isValid(self, s: str) -> bool:    
        s = s.replace('"',"")
        strMap = {")":"(", "}":"{", "]":"["}         
        stackList = []
        for char in s:
            if(strMap.get(char)):
                if not (stackList and stackList.pop() == strMap[char]):
                    return False
            else:
                stackList.append(char)
        return not stackList
