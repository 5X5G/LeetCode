#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

#First
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         s = s.replace('"',"")
#         romanMap ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         romanList = ["I","V","X","L","C","D","M"]
#         num = 0
#         for index in range(len(s)-1):
#             if((romanList.index(s[index]) - romanList.index(s[index+1]))  < 0):
#                 num += -romanMap[s[index]]
#             else:
#                 num += romanMap[s[index]]
                
#         return num + romanMap[s[len(s)-1]]

# #Second
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('"',"")
        romanMap ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        for index in range(len(s)-1):
            if((romanMap[s[index]] - romanMap[s[index+1]])  < 0):
                num += -romanMap[s[index]]
            else:
                num += romanMap[s[index]]
                
        return num + romanMap[s[len(s)-1]]

#Third  
"""
不可用!!!!!!!!思维有问题，发现规律乘2再乘5，不能简单用pow实现
"""
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         s = s.replace('"',"")
#         romanList = ["I","V","X","L","C","D","M"]
#         num = 0
#         ground = 1
#         preIndex= 0
#         for index in range(len(s)-1):
#             preIndex= romanList.index(s[index])            
#             if(preIndex > 0):
#                 if(preIndex % 2 == 0):
#                     ground = 2
#                 else:
#                     ground = 5
#             if(preIndex - romanList.index(s[index+1]) < 0):
#                 num += -pow(ground,preIndex)
#             else:
#                 num += pow(ground,preIndex)
        
#         preIndex=romanList.index(s[len(s)-1])
#         if(preIndex > 0):
#                 if(preIndex % 2 == 0):
#                     ground = 2
#                 else:
#                     ground = 5
#         return num + pow(ground,romanList.index(s[len(s)-1]))

# ss = Solution()
# ss.romanToInt('"IX"')
