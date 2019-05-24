#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if(len(strs) == 0):
            return ""
        
        sShort = strs[0]
        for s in strs:
            if(len(sShort) > len(s)):
                sShort = s
        strs.remove(sShort)
        target = sShort
        for length in range(len(sShort),-1,-1):
            for i in range(len(sShort)-length):                                
                for s in strs:    
                    target = sShort[i:length-i+1]            
                    if(s.find(target) < 0):
                        target = ""
                        break
                if(target != ""):
                    return target                        
        
        return target

s = Solution()
l = ["flower","flow","flight"]
s.longestCommonPrefix(l)
