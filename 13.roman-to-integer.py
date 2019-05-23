#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap ={"I":1,"V":5,"X":10,"L":50,"C":100,"D"：500，"M":1000}
        romanList = ["I","V","X","L","C","D""M"]
        num = 0
        index = 0
        while index < len(str)-1：
            if(romanList[index] < romanList[index] ):

