#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

for i in range(20,10):
    print(i)

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        target = ""
        sShort = strs[0]
        for s in strs:
            if(len(sShort) > len(s)):
                sShort = s
        strs.remove(sShort)               
        for length in range(len(sShort)):
            for i in range(length):
                target = sShort[i:length-i]
                for s in strs:                    
                    if(s.find(target) < 0):
                        target = ""
                        break
                if(target != ""):
                    return target                        
        
        return ""

s = Solution()
l = ["flower","flow","flight"]
s.longestCommonPrefix(l)
